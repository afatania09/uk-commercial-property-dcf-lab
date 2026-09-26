"""Tenancy-level explicit DCF model for UK commercial property.

Educational decision-support code. It does not constitute a valuation.
Cash flows are modelled explicitly; assumptions must be supported by market evidence.
"""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Tenancy:
    unit: str
    passing_rent: float
    erv: float
    lease_years: float
    break_year: float | None = None
    void_months: int = 6
    rent_free_months: int = 3
    reletting_cost_pct_erv: float = 0.10
    annual_erv_growth: float = 0.025

    def validate(self) -> None:
        if min(self.passing_rent, self.erv, self.lease_years) < 0:
            raise ValueError(f"Negative input for {self.unit}")
        if self.void_months < 0 or self.rent_free_months < 0:
            raise ValueError("Void/rent-free periods cannot be negative")


def tenancy_cashflows(t: Tenancy, horizon: int = 10, assume_break_exercised: bool = False) -> list[float]:
    """Annual unlevered cash flow before property-level costs.

    Simplifying educational convention: lease event occurs at the end of the
    relevant model year. Following expiry/break, the unit is relet at grown ERV,
    after void, rent-free and reletting costs.
    """
    t.validate()
    event = t.break_year if (assume_break_exercised and t.break_year is not None) else t.lease_years
    flows: list[float] = []
    for year in range(1, horizon + 1):
        grown_erv = t.erv * ((1 + t.annual_erv_growth) ** (year - 1))
        if year <= event:
            flows.append(t.passing_rent)
            continue
        if year == int(event) + 1:
            void_loss = grown_erv * min(t.void_months, 12) / 12
            incentive = grown_erv * min(t.rent_free_months, 12) / 12
            reletting = grown_erv * t.reletting_cost_pct_erv
            flows.append(max(grown_erv - void_loss - incentive - reletting, -grown_erv))
        else:
            flows.append(grown_erv)
    return flows


def aggregate_cashflows(tenancies: Iterable[Tenancy], horizon: int = 10, assume_break_exercised: bool = False) -> list[float]:
    total = [0.0] * horizon
    for tenancy in tenancies:
        for i, cf in enumerate(tenancy_cashflows(tenancy, horizon, assume_break_exercised)):
            total[i] += cf
    return total


def terminal_value(next_year_income: float, exit_yield: float, selling_cost_pct: float = 0.01) -> float:
    if exit_yield <= 0:
        raise ValueError("Exit yield must be positive")
    gross = next_year_income / exit_yield
    return gross * (1 - selling_cost_pct)


def present_value(cashflows: list[float], discount_rate: float, terminal: float = 0.0) -> float:
    if discount_rate <= -1:
        raise ValueError("Discount rate must be greater than -100%")
    pv = sum(cf / ((1 + discount_rate) ** year) for year, cf in enumerate(cashflows, start=1))
    if terminal:
        pv += terminal / ((1 + discount_rate) ** len(cashflows))
    return pv


def sensitivity_grid(cashflows: list[float], terminal_income: float, discount_rates: Iterable[float], exit_yields: Iterable[float]) -> dict[tuple[float, float], float]:
    return {
        (dr, ey): present_value(cashflows, dr, terminal_value(terminal_income, ey))
        for dr in discount_rates
        for ey in exit_yields
    }
