"""Transparent commercial-property DCF engine.

Educational decision-support code. It does not produce an RICS valuation.
All assumptions must be evidenced and reviewed by a competent valuer.
"""
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class DCFInputs:
    annual_cash_flows: Sequence[float]
    discount_rate: float
    terminal_erv: float
    exit_yield: float
    sale_cost_rate: float = 0.0


def present_value(amount: float, rate: float, year: int) -> float:
    if rate <= -1:
        raise ValueError("discount rate must be greater than -100%")
    if year < 0:
        raise ValueError("year must be non-negative")
    return amount / ((1.0 + rate) ** year)


def terminal_value(terminal_erv: float, exit_yield: float, sale_cost_rate: float = 0.0) -> float:
    if exit_yield <= 0:
        raise ValueError("exit yield must be positive")
    if terminal_erv < 0:
        raise ValueError("terminal ERV cannot be negative")
    if not 0 <= sale_cost_rate < 1:
        raise ValueError("sale cost rate must be between 0 and 1")
    gross = terminal_erv / exit_yield
    return gross * (1.0 - sale_cost_rate)


def dcf_value(inputs: DCFInputs) -> float:
    """Return the present value of annual net cash flows plus terminal value.

    Cash flows are assumed to occur at each year end. The terminal value is
    received at the end of the final explicit forecast year.
    """
    if not inputs.annual_cash_flows:
        raise ValueError("at least one annual cash flow is required")
    pv_income = sum(
        present_value(cf, inputs.discount_rate, year)
        for year, cf in enumerate(inputs.annual_cash_flows, start=1)
    )
    tv = terminal_value(inputs.terminal_erv, inputs.exit_yield, inputs.sale_cost_rate)
    return pv_income + present_value(tv, inputs.discount_rate, len(inputs.annual_cash_flows))


def sensitivity_matrix(
    annual_cash_flows: Sequence[float],
    terminal_erv: float,
    discount_rates: Iterable[float],
    exit_yields: Iterable[float],
    sale_cost_rate: float = 0.0,
) -> dict[float, dict[float, float]]:
    """Return values indexed by discount rate, then exit yield."""
    return {
        dr: {
            ey: dcf_value(DCFInputs(annual_cash_flows, dr, terminal_erv, ey, sale_cost_rate))
            for ey in exit_yields
        }
        for dr in discount_rates
    }
