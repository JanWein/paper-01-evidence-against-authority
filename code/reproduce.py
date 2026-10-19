"""R2: endogenous corrective evidence and action-contingent trail audits.
Run with Python >=3.10; standard library only. All examples are synthetic.
"""
from pathlib import Path
import csv,json,math,random
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'results';OUT.mkdir(exist_ok=True)

def primitives(mu=.5,pH=.85,pL=.6,r=.8,lam=1.5,C=.15):
 p=mu*pH+(1-mu)*pL;h=r-p
 dH=pH*(1-r)+(1-pH)*r;dL=pL*(1-r)+(1-pL)*r;d=mu*dH+(1-mu)*dL
 mC=mu*dH/d;A=mu-mC;L=lam*d*A;g=h/d
 pF=p*r/(p*r+(1-p)*(1-r));mF=mu*(1-dH)/(1-d)
 assert 0<mu<1 and .5<pL<pH<1 and p<r<1 and C>h
 assert 0<lam and lam*(mF-mC)<2*p-1 and L<h
 return dict(mu=mu,pH=pH,pL=pL,r=r,lam=lam,C=C,p=p,h=h,dH=dH,dL=dL,d=d,mC=mC,mF=mF,A=A,L=L,g=g,pF=pF)

def equilibrium(P,tau,power=1.):
 # F(c)=(c/C)^power, c in [0,C]; uniform iff power=1.
 def rhs(q):return max(0.,min(1.,(P['h']-(1-tau)*P['L']/(1-P['d']*q))/P['C']))**power
 lo,hi=0.,1.
 for _ in range(100):
  mid=(lo+hi)/2
  if mid>rhs(mid):hi=mid
  else:lo=mid
 q=(lo+hi)/2;cut=P['C']*q**(1/power)
 mN=P['mu']*(1-q*P['dH'])/(1-q*P['d'])
 return dict(q=q,cutoff=cut,mN=mN,D=mN-P['mC'],accuracy=P['p']+P['h']*q,
             acquisition_cost=P['C']*power/(power+1)*q**((power+1)/power),audits=tau*(1-P['d']*q))

def tau_of_q(P,q):return 1-(P['h']-P['C']*q)*(1-P['d']*q)/P['L']
def Hprime(P,q):
 d,C,h,L=P['d'],P['C'],P['h'],P['L'];t=1-d*q
 return -d+(C*t*t+2*d*(h-C*q)*t)/L

def policy(P,kappa):
 q0=equilibrium(P,0)['q'];qf=P['h']/P['C'];d,C,h,L=P['d'],P['C'],P['h'],P['L']
 # Global extrema of a cubic on the exact compact feasible interval.
 a=-3*kappa*C*d*d/L
 b=-C+kappa*(4*C*d+2*d*d*h)/L
 c=h+kappa*d-kappa*(C+2*d*h)/L
 cand=[q0,qf]
 if abs(a)<1e-15:
  if abs(b)>1e-15:cand.append(-c/b)
 else:
  disc=b*b-4*a*c
  if disc>=0:cand.extend([(-b-math.sqrt(disc))/(2*a),(-b+math.sqrt(disc))/(2*a)])
 cand=[q for q in cand if q0-1e-12<=q<=qf+1e-12]
 def value(q):return h*q-C*q*q/2-kappa*tau_of_q(P,q)*(1-d*q)
 best=max(cand,key=value);tau=max(0.,min(1.,tau_of_q(P,best)))
 e=equilibrium(P,tau)
 t0=1-d*q0;x0=L*d/(C*t0*t0);kcrit=L*L/(t0*(L*d+C*t0*t0))
 return dict(kappa=kappa,q0=q0,qFB=qf,q_star=best,tau_star=tau,x0=x0,kappa_critical=kcrit,net_gain_over_no_audit=value(best)-value(q0),
             welfare=P['p']+value(best),audit_rate=e['audits'],Hprime_FB=Hprime(P,qf),candidates=len(cand))

def dump(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
P=primitives();policies=[policy(P,k) for k in [0,.005,.01,.02,.03,.05,.1]]
dump('optimal_policies.csv',policies)
dump('acquisition_path.csv',[dict(tau=t/100,**equilibrium(P,t/100)) for t in range(101)])
# Validate all four terminal action plans for both acquisition decisions,
# integrating audit/no-audit and true type/state, not using cutoff formula for payoffs.
def terminal_payoff(P,q,tau,e,plan,cost=0):
 mN=P['mu']*(1-q*P['dH'])/(1-q*P['d']);out=0.
 # plan=(action when z confirms, action when z contradicts), 0=retain,1=reverse.
 # no evidence uses plan[0]. Evaluator audits only retain actions.
 for typ,pt,wt in [(1,P['pH'],P['mu']),(0,P['pL'],1-P['mu'])]:
  for theta in [0,1]:
   s=1 # condition on s; state mass normalized given s.
   ws=pt if theta==s else 1-pt
   for z in ([0,1] if e else [None]):
    wz=(P['r'] if z==theta else 1-P['r']) if e else 1.
    rev=plan[int(z!=s)] if e else plan[0]
    a=1-s if rev else s
    if rev:rep=P['mC']
    else:
     ma=(P['mC'] if z!=s else P['mF']) if e else P['mu']
     rep=(1-tau)*mN+tau*ma
    out+=wt*ws*wz*((a==theta)+P['lam']*rep)
 return out-cost*e
rng=random.Random(81701);max_res=0.;n=0;plan_checks=0;grid_gap=0.; regular_policy_checks=0
for j in range(400):
 mu=rng.uniform(.15,.85);pL=rng.uniform(.53,.68);pH=rng.uniform(.78,.93);p=mu*pH+(1-mu)*pL
 r=rng.uniform(max(p+.02,.77),.98);d=p*(1-r)+(1-p)*r;g=(r-p)/d
 dH=pH*(1-r)+(1-pH)*r;dL=pL*(1-r)+(1-pL)*r
 mc=mu*dH/d;mf=mu*(1-dH)/(1-d);aa=mu-mc
 lam=.75*min((2*p-1)/(mf-mc),(r-p)/(d*aa));C=rng.uniform(1.2,3)*(r-p)
 pp=primitives(mu,pH,pL,r,lam,C);tau=rng.random();ee=equilibrium(pp,tau)
 res=abs(ee['cutoff']-pp['h']+(1-tau)*pp['L']/(1-pp['d']*ee['q']));max_res=max(max_res,res);assert res<1e-12
 # All feasible no-information and acquired terminal plans, for below/above cutoff costs.
 for cc in [ee['cutoff']*.5,(ee['cutoff']+C)/2]:
  opts=[]
  for e in [0,1]:
   for plan in ([(0,0),(1,1)] if e==0 else [(0,0),(0,1),(1,0),(1,1)]):
    opts.append((terminal_payoff(pp,ee['q'],tau,e,plan,cc),e,plan))
  target=terminal_payoff(pp,ee['q'],tau,int(cc<ee['cutoff']),(0,1) if cc<ee['cutoff'] else (0,0),cc)
  assert target>=max(v[0] for v in opts)-1e-12
  plan_checks+=len(opts)
 kappa=rng.uniform(.00001,.1);opt=policy(pp,kappa)
 gridmax=-1e99
 for i in range(1001):
  t=i/1000;ev=equilibrium(pp,t);val=pp['p']+pp['h']*ev['q']-ev['acquisition_cost']-kappa*ev['audits']
  gridmax=max(gridmax,val)
 assert opt['welfare']>=gridmax-1e-12
 grid_gap=max(grid_gap,opt['welfare']-gridmax)
 if opt['x0']<(math.sqrt(17)-3)/4:
  if kappa>=opt['kappa_critical']:assert abs(opt['q_star']-opt['q0'])<1e-9
  else:assert 0<opt['tau_star']<1
  regular_policy_checks+=1
 # Nonuniform cost distributions are checked without uniform-policy formula.
 for pw in [.6,2.]:
  ev=equilibrium(pp,tau,pw);assert abs(ev['cutoff']-pp['h']+(1-tau)*pp['L']/(1-pp['d']*ev['q']))<1e-12
 n+=1
# Finite private-own-ability counterexample, with all plan deviations.
qL=2/3;m0=1/(2-qL);lam=.2;c=.05
assert abs(m0-.75)<1e-12
assert abs((.8-.6)-c-lam*m0)<1e-12
assert -c-lam*m0<0 # H has no accuracy benefit from buying r<pH.
# Known-own-ability example: check every terminal action plan after acquisition.
own_plan_checks=0
for pt in [.85,.60]:
 base=pt+lam*m0
 assert (1-pt)+lam*1 < base # even the best off-path uninformed reversal posterior
 vals=[]
 for plan in [(0,0),(0,1),(1,0),(1,1)]:
  val=0.
  for theta in [0,1]:
   for z in [0,1]:
    w=(pt if theta==1 else 1-pt)*(.8 if z==theta else .2)
    rev=plan[int(z!=1)];a=0 if rev else 1
    val+=w*(a==theta)
  vals.append(val-c) # fully documented acquired reputation zero
  own_plan_checks+=1
 assert max(vals)<=base+1e-12
# Paired participant-level precision sensitivity, not observed pilot variance.
precision=[]
for N in [160,200,240,320]:
 for sd in [.25,.35,.5,1.]:
  se=sd/math.sqrt(N)
  precision.append(dict(participants=N,paired_sd=sd,se_difference=se,mde80=2.80158521811*se))
dump('small_design_precision.csv',precision)
summary=dict(version='R2',real_observations=0,parameter_cases=n,terminal_plan_deviations_checked=plan_checks,
 maximum_cutoff_residual=max_res,global_optimum_crosschecks=n,regular_policy_threshold_checks=regular_policy_checks,grid_points_per_case=1001,
 maximum_analytic_over_grid_gap=grid_gap,baseline_parameters=P,policy_examples=policies,
 known_ability_terminal_plans_checked=own_plan_checks,own_ability_counterexample=dict(qH=0,qL=qL,posterior_no_acquisition=m0,posterior_acquisition=0))
(OUT/'verification.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
