# UK Commercial Property DCF Lab

**Transparent, evidence-led explicit discounted cash-flow modelling for UK commercial property investment.**

> **Professional position:** this repository is an educational decision-support project. It is not a Red Book valuation, does not provide investment advice and does not replace inspection, verification, market evidence or professional judgement.

## Why this project exists

UK investment valuation has traditionally made extensive use of growth-implicit income-capitalisation models. RICS now encourages appropriate consideration of explicit DCF and greater transparency around valuation assumptions, while making clear that DCF is **not mandatory** and method/model selection remains a matter of professional judgement.

This project explores what that means in practice. It is deliberately built to demonstrate not merely the mathematics of discounting, but the harder valuation questions: **what cash flow should be modelled, why an assumption is market-consistent, what evidence supports it, how uncertainty changes the answer, and how the result should be cross-checked.**

## What the lab demonstrates

| Capability | What is demonstrated |
|---|---|
| Explicit DCF | Annual cash flows and terminal value discounted to present value |
| Growth-explicit analysis | Rental-growth assumptions exposed rather than buried in an all-risks yield |
| Multi-let modelling | Framework for unit/tenant-level lease events and aggregate property cash flow |
| Reversionary analysis | Passing rent considered separately from ERV |
| Sensitivity | Discount-rate and exit-yield matrix |
| Cross-checking | DCF designed to be reconciled against market transactions and implicit methods |
| Data governance | Public source, access date, measurement basis and evidence status recorded |
| Professional judgement | Missing assumptions remain unresolved rather than being invented |

## Flagship case study

### The Glade Business Centre — West Thurrock

A publicly marketed **10-unit, nine-tenant industrial estate** is used to frame a realistic multi-let DCF investigation. Public marketing information states 17,684 sq ft of ground-floor GIA plus first-floor accommodation, passing rent of £332,172 pa, WAULT of 3.95 years to expiries / 2.54 years to breaks, and a latest on-site letting above the average passing rent.

The case deliberately does **not** reverse-engineer a valuation to a known sale/asking figure. Instead it identifies what further evidence a valuer needs before adopting ERVs, rental growth, void assumptions, discount rate and exit yield.

➡️ See [`cases/glade_west_thurrock.md`](cases/glade_west_thurrock.md)

## Core model

The transparent Python engine in [`dcf_engine.py`](dcf_engine.py) implements:

- present-value discounting;
- explicit annual net cash flows;
- terminal value from terminal ERV and exit yield;
- sale-cost allowance;
- discount-rate × exit-yield sensitivity analysis;
- validation of key numerical inputs.

The code intentionally remains readable. A valuation model should be capable of being reviewed, challenged and reproduced.

```python
from dcf_engine import DCFInputs, dcf_value

inputs = DCFInputs(
    annual_cash_flows=[320_000, 335_000, 350_000, 365_000, 380_000],
    discount_rate=0.08,
    terminal_erv=400_000,
    exit_yield=0.0625,
    sale_cost_rate=0.015,
)

value = dcf_value(inputs)
```

These numbers are illustrative only; they are **not** assumptions for the Glade case.

## Valuation logic before code

```text
Purpose + basis of value + valuation date
                  ↓
Property / tenure / occupational interests
                  ↓
Verified passing income + lease events
                  ↓
Market evidence → ERV / growth / risk / costs
                  ↓
Explicit property cash flow
                  ↓
Discount rate + terminal value assumptions
                  ↓
Present value
                  ↓
Sensitivity + scenario analysis
                  ↓
Market / implicit-method cross-check
                  ↓
Professional reconciliation and conclusion
```

The important point is the final line. **The model calculates; the valuer concludes.**

## Market Value is not Investment Value

DCF describes a modelling technique; it does not determine the basis of value. A Market Value DCF requires assumptions consistent with market participants and market evidence. Investor-specific requirements can instead produce Investment Value/worth. The distinction is fundamental and is kept visible throughout this project.

## Data discipline

Only public or clearly synthetic information belongs in this repository. No employer, client, taxpayer/ratepayer, restricted, personal or otherwise confidential information is used. Public marketing evidence is attributed to its source and assumptions are distinguished from observed facts.

See [`docs/valuation_framework.md`](docs/valuation_framework.md) for the evidence, modelling and QA framework.

## Testing

```bash
python -m pip install -r requirements.txt
pytest -q
```

Tests cover core discounting and terminal-value logic and will expand alongside the lease-event engine.

## Roadmap

- **01 — Multi-let industrial:** unit-level lease-event engine, ERV evidence register and full sensitivity analysis.
- **02 — Rack-rented single let:** implicit capitalisation vs explicit DCF.
- **03 — Under-rented investment:** term/reversion cross-check and explicit rental-growth treatment.
- **04 — Over-rented investment:** hardcore/top-slice cross-check and downside/reletting scenario.
- **05 — Vacancy / capex:** void, incentives, letting costs and refurbishment scenarios.
- **06 — Evidence analytics:** comparable transactions, assumption provenance and confidence/quality flags.

## Reference framework

The project should be read alongside the current RICS Valuation – Global Standards and RICS practice information on discounted cash-flow valuation. RICS states that explicit DCF is increasingly considered in appropriate circumstances, while the valuer retains responsibility for selecting the appropriate approach, method and model.

- RICS DCF hub: https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/valuation-standards/discounted-cash-flow-valuation
- RICS, *Discounted cash flow valuations* practice information (2023): https://www.rics.org/content/dam/ricsglobal/documents/standards/Discounted-cash-flow-valuations-1.pdf
- RICS APC overview of valuation approaches and methods: https://ww3.rics.org/uk/en/journals/property-journal/apc-5-valuation-methods.html

## Author's objective

The purpose of the lab is to develop and demonstrate a disciplined approach to **valuation, market evidence and data**: transparent assumptions, reproducible calculations, appropriate challenge and clear recognition of model limitations.

---

**Disclaimer:** Educational research only. Nothing in this repository is a valuation, offer, recommendation or advice to transact. Property information can change and public marketing particulars may be incomplete. Any professional valuation requires an appropriate instruction, investigations, evidence, assumptions, competence, inspection where appropriate, and compliance with the standards applicable to that instruction.
