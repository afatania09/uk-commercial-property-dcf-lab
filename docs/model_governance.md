# Model governance and valuation controls

This project is deliberately designed as **decision support**, not an automated valuation.

## Control framework

| Risk | Why it matters | Control |
|---|---|---|
| False precision | DCF can make uncertain assumptions look exact | Sensitivity tables and scenario ranges |
| Automation bias | A calculated number may be accepted uncritically | Mandatory valuer-judgement checkpoint |
| Weak ERV evidence | Reversion drives value | Record source, date, comparability and adjustment |
| Unsupported discount rate | Required return materially affects PV | Prefer market-derived/back-solved evidence; document rationale |
| Exit-yield optimism | Terminal value can dominate the result | Show terminal-value share and sensitise exit yield |
| Lease-event uncertainty | Breaks/expiries alter cash flow | Model explicit scenarios rather than certainty |
| Data error | Wrong rent/date/area propagates through model | Validation, source register and tests |
| Basis confusion | Market Value and Investment Value answer different questions | Declare basis and prevent investor-specific assumptions being presented as market evidence |

## Evidence hierarchy

1. Verified relevant transactions.
2. Verified comparable lettings and investment evidence.
3. Published market evidence with provenance.
4. Asking/marketing evidence, treated with appropriate caution.
5. Valuer assumptions, clearly labelled and justified.

## Reconciliation

A DCF output is not automatically the valuation conclusion. The valuer should:
- inspect the contribution of explicit income and terminal value;
- compare against relevant market transactions;
- cross-check against an appropriate growth-implicit method where useful;
- investigate material divergence rather than averaging mechanically;
- explain the adopted conclusion and uncertainty.

## Audit principle

For each material input record: **source → observation → adjustment → adopted input → rationale → sensitivity**.

No confidential VOA/HMRC, client or taxpayer/ratepayer information belongs in this public repository.
