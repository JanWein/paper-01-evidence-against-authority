# Compact experimental protocol, R2

Status: proposed study only. No participants recruited, no budget incurred, no experiment conducted, no registration or ethical clearance claimed.

## 1. Operational primary design

Use 200 adult participants in a within-participant controlled decision task. Each completes twelve primary cases, six under no retention audit (tauN=0) and six under guaranteed retention audit (tauN=1). Randomize policy order in balanced blocks and randomize cases to policy within precision/cost blocks. The primary unit is the participant; the primary estimand is the mean within-participant difference in the fraction of cases in which paid corrective evidence is purchased. Signal precision, cost distribution, initial diagnostic technology, accuracy pay, and rating-linked pay are held fixed. The actual evidence realization cannot be held known to the manager before the acquisition choice: that would remove the new margin. The controlled information object is the same corrective technology and pre-generated, concealed packets, not an algorithm assumed to be correct.

The twelve cases have independent latent diagnostic types, independent states, and independent evidence packets. Tell participants this explicitly. Different case types avoid the persistent-type learning problem from the previous protocol. Each case's evaluator sees only that case's permitted record, never the participant's other cases. A participant's expected reputation payoff is a bounded per-case study reward tied to the evaluator's rating. It does not affect employment or a real performance review. A role-assigned latent diagnostic quality is an induced-incentive analogue, not a claim about the participant's actual intelligence or managerial competence.

The experiment tests acquisition and information use under a documentation policy. It does not estimate profitability, the social resource cost of evidence, or the model's optimal audit cost kappa. Paid evidence fees in the experiment induce a private cost but are transfers within the experiment, not evidence of real investigation resource costs.

## 2. Cases, decisions, and timing

Design inputs for the main cases: prior high diagnostic type .5; first-diagnosis precision .85/.60; corrective precision .80; independent evidence conditional on state. Use an induced private acquisition fee uniformly drawn on [0,C] with C=.15 in normalized accuracy-pay units. The model's lambda=1.5 is a design ratio, not an estimated behavioral parameter. Choose and disclose bounded actual currency scaling only after budget approval; no money is committed by this protocol.

1. Consent and instructions state every observation, recording, payment, and confidentiality rule, with no personnel consequences.
2. Run comprehension exercises covering the probability tree, possible signal errors, acquisition fee, and evaluator access. Failures receive instruction before randomization. Predefine eligibility after a second failure, before treatment exposure.
3. The system generates an immutable initial diagnosis s, a state, and a sealed corrective signal. The participant records an initial probability and recommendation before seeing the private fee. The original s always remains visible to the evaluator, regardless of the participant's recommendation.
4. Announce the case's audit rule before acquisition and display the private fee. Ask whether the participant buys the corrective signal. The researcher logs fee and acquisition; the evaluator never sees the fee.
5. If purchased, display the packet and its known likelihoods. If not purchased, display an equally timed neutral screen. Record delivery, dwell time, and technical failures. Do not substitute a directional hint in the no-purchase case.
6. Allow either binary final action regardless of purchase or agreement between signals. Record final probability and action, with no action-space restriction.
7. Apply the announced audit rule after action: under tauN=1 retrieve the complete acquisition record for every retained diagnosis; under tauN=0 retrieve none. Do not audit reversals in either primary arm. All evaluators see s and a. When audited, evaluators also see e=0 or e=1 plus the actual z. Do not reveal state or latent type until ratings are locked.
8. A separate evaluator reports P(type=H); a proper scoring payment incentivizes evaluator accuracy. The participant receives the disclosed accuracy/rating-linked incentive via the selected payment component. Outcome and type feedback occurs only after all primary choices, avoiding feedback-driven case-to-case learning about the technology. Source types remain independent across cases.

For implementation, investigators need enough evaluator decisions or a separately consented evaluator pool. If evaluators rate multiple cases, randomize which cases and policies they see, keep participant identity hidden, and cluster inference or randomization at the actual independent evaluator units as required. Primary participant assignment and evaluator reuse cannot be assumed independent without inspecting the implementation graph.

## 3. Ready-to-use core materials

Common text: “Each case has one of two outcomes, initially equally likely. Your assigned diagnostic process has a higher or lower accuracy, with equal initial probabilities. Its diagnosis is correct in 85 or 60 out of 100 cases respectively. You and the evaluator are not told which accuracy applies in this case. Diagnostic types are drawn independently across cases. You can purchase an additional check, which is correct in 80 out of 100 cases and independent of the first diagnosis conditional on the true outcome. The fee is shown privately before you choose whether to buy.”

No-audit text: “The evaluator will see the original diagnosis and your final action. The evaluator will not see whether you purchased the additional check or what it said.”

Retention-audit text: “The evaluator will see the original diagnosis and your final action. If you keep the diagnosed action, the evaluator will also receive the complete record showing whether you purchased the check and, if purchased, exactly what it said. This record is transmitted regardless of whether it helps your assessment. If you reverse the diagnosed action, the evaluator will not receive an additional record.”

Acquisition text: “The additional check costs [fee]. Purchase it for this case? Its stated accuracy is unchanged by the recording rule.”

Evaluator text: “Report the probability that the case's initial diagnostic process had the higher accuracy. Use only the record displayed. The participant knew the record rule before deciding whether to purchase a check. Your assessment affects a bounded study reward and has no employment consequence.”

Private-belief questions are asked after the primary action in the main sample to avoid priming. An optional randomized process subsample can answer them before action, but its primary outcomes are reported separately because elicitation is itself an intervention.

Payments must be fully specified in consent before recruitment. Randomly select a case and an incentive component for payment to avoid hedging across reports and rating bonuses. Use binarized quadratic scoring for probability reports and evaluator type ratings, stating the expected-utility and compound-lottery assumptions. Exact currency conversion, attendance pay, and caps are pending budget approval, not silently invented here.

## 4. Outcomes, estimation, and precision

Primary: participant's purchase fraction under retention audit minus purchase fraction under no audit, averaged across participants. Analyze with a paired participant-level estimator, a two-sided .05 test, confidence interval, and a randomization test respecting case/block assignments. All randomized eligible participants remain in ITT; do not condition on successful evidence delivery or realized purchase.

Secondary family, Holm-adjusted: final action accuracy; expected benchmark regret using all evidence the participant actually received; and change in evaluator ratings conditional on pretreatment case characteristics. Because purchase is post-treatment, correction among buyers is descriptive selection, not a randomized comparison. A separately compulsory-evidence validation block of four matched-precision cases after the primary cases tests comprehension and ability to correct without selection into buying; it is secondary and not included in the main acquisition estimand. Do not call a purchase-rate increase an efficiency gain if resulting decisions worsen.

Model benchmark: integrate the known first-diagnosis likelihoods with the acquired signal when present. The realized state is observed for every case irrespective of action. A positive acquisition effect accompanied by accurate compulsory-evidence updating and an evaluator-posterior response is consistent with the model. It does not prove reputation uniquely: documentation can affect attention, perceived scrutiny, or demand. Hold layout and minimum screen time fixed; measure comprehension, reliability beliefs, and subjective expected ratings. The model illustration predicts a .3906 acquisition-rate change between the extreme policies, but that uncalibrated prediction is not treated as an effect-size estimate. A future placebo policy showing an unrelated record can further distinguish generic scrutiny but is not part of the primary two-arm budget.

For 200 independent participant differences, the normal-approximation MDE is 2.802*sigma_D/sqrt(200). At paired SDs .25, .35, and .50, the MDE is .0495, .0693, and .0991 respectively. The primary planning target is a twenty-percentage-point acquisition effect. This is a deliberately large mechanism-test target, not a promise to measure small organizational effects; it is not guaranteed by an unrun pilot. The rigorous support bound for a difference in [−1,1] permits SD up to one and MDE .1981. The design must report that conservative sensitivity rather than claiming precision without data.

If each participant's twelve decisions were independent conditional on stable subject effects, six per arm and illustrative purchase probabilities near .4/.5 imply within-person difference SD around .286. Allowing heterogeneous treatment responses and residual correlation motivates .35-.50 sensitivity values. Those values are assumptions, not pilot estimates. Run a separately authorized 30-person feasibility pilot to estimate completion, comprehension, and paired variance; do not pool its hypothesis-driven adjustments into the confirmatory sample. If SD materially exceeds .50, increase sample size before registration or narrow the target to a larger detectable effect. Evidence of organizational profitability would require a different field design and actual resource costs.

No real outcomes exist. All reporting cells remain unpopulated.

## 5. Attrition, interference, and falsification

Log nonresponse, technical delivery errors, and acquisition fees separately. Missing purchases are not coded as nonpurchase unless a prespecified behavioral “submitted purchase by deadline” composite is separately labeled. Report assignment-specific missingness and worst-case bounded-outcome sensitivity; imputation is secondary and must state assumptions.

No communication across participants is permitted during the controlled task. Case source types are independent; do not share outcomes until the primary block ends. If team communication or evaluator identities induce dependence, change randomization and clustering before launch. Record policy-order and trial effects, and report them as secondary rather than conditioning the primary sample on adaptation.

A narrow null on acquisition weakens the proposed upstream mechanism in this task. A documentation effect only on compulsory-evidence correction favors a continuation mechanism rather than the main acquisition-substitution prediction. Persistent errors in known-likelihood comprehension weaken the Bayesian interpretation. Rejection of lower-quality corrective signals with improved accuracy is efficient discretion, not failed updating. A future low-precision block should be prespecified separately and should never reward revisions merely for occurring.

## 6. Minimal data dictionary

| Variable | Definition | Timing |
|:--|:--|:--|
| participant_id, evaluator_id | pseudonymous identifiers | assignment |
| case_id, block, order | case and policy sequence | assignment |
| s, theta, type | initial diagnostic label, state, latent source quality | generated; truth concealed |
| z_sealed | pre-generated corrective signal, hidden until purchase | generated |
| pH,pL,r,mu | known design likelihoods | fixed |
| tauN,tauR | announced audit probabilities | before purchase |
| fee, C | private induced acquisition cost and support | before purchase |
| initial_action, initial_p | recommendation and probability | before fee |
| purchase | evidence acquisition decision | primary choice |
| delivered, dwell_ms | packet delivery and display duration | post-purchase |
| final_action, final_p | unrestricted action and probability | before audit |
| audit_done, audit_record | actual inspection and supplied record | after action |
| evaluator_H | probability initial type was H | before truth |
| missing_reason | technical, timeout, withdrawal, unknown | logged |
| accuracy, benchmark_regret | derived all-case scores | analysis |

Keep raw logs immutable and define derivation scripts before collection. Store no unnecessary identity or employment information. Publication of any participant data would need separate authorization and consent-compatible deidentification.

## 7. Optional legacy extension

The earlier eight-cell E-by-V-by-documentation interaction is retained only as `reviews/superseded_eight_cell_protocol.md`. Its roughly 25,116-dyad small-effect requirement is not the operational primary plan. The compact design here holds evidence technology fixed and tests paid acquisition, matching the revised theoretical margin. It sacrifices the legacy access-by-visibility interaction and cannot be reported as identifying that estimand.
