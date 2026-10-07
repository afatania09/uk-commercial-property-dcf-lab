"""Cross-check helpers for transparent investment valuation reconciliation."""

def years_purchase_perpetuity(yield_rate: float) -> float:
    if yield_rate <= 0:
        raise ValueError("yield must be positive")
    return 1.0 / yield_rate

def capitalise_rent(rent: float, yield_rate: float) -> float:
    if rent < 0:
        raise ValueError("rent cannot be negative")
    return rent * years_purchase_perpetuity(yield_rate)

def implied_initial_yield(net_income: float, price: float) -> float:
    if price <= 0:
        raise ValueError("price must be positive")
    return net_income / price

def reconcile(dcf: float, implicit: float, adopted: float) -> dict[str,float]:
    if min(dcf, implicit, adopted) <= 0:
        raise ValueError("values must be positive")
    return {
        "dcf": dcf,
        "implicit": implicit,
        "adopted": adopted,
        "dcf_vs_implicit_pct": (dcf / implicit - 1) * 100,
        "adopted_vs_dcf_pct": (adopted / dcf - 1) * 100,
        "adopted_vs_implicit_pct": (adopted / implicit - 1) * 100,
    }
