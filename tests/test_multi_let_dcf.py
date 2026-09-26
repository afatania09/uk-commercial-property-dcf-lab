import pytest

from multi_let_dcf import Tenancy, aggregate_cashflows, present_value, tenancy_cashflows, terminal_value


def test_contractual_rent_before_expiry():
    t = Tenancy("Unit 1", 100_000, 120_000, lease_years=3)
    flows = tenancy_cashflows(t, horizon=3)
    assert flows == [100_000, 100_000, 100_000]


def test_reletting_year_reflects_costs():
    t = Tenancy("Unit 1", 100_000, 120_000, lease_years=1, void_months=3, rent_free_months=3, reletting_cost_pct_erv=0.10, annual_erv_growth=0)
    flows = tenancy_cashflows(t, horizon=2)
    assert flows[0] == 100_000
    assert flows[1] == pytest.approx(48_000)


def test_break_scenario_changes_cashflow():
    t = Tenancy("Unit 1", 100_000, 130_000, lease_years=5, break_year=2, annual_erv_growth=0)
    hold = tenancy_cashflows(t, horizon=4, assume_break_exercised=False)
    break_case = tenancy_cashflows(t, horizon=4, assume_break_exercised=True)
    assert hold != break_case


def test_aggregate_tenancies():
    a = Tenancy("A", 50_000, 60_000, lease_years=10)
    b = Tenancy("B", 70_000, 80_000, lease_years=10)
    assert aggregate_cashflows([a, b], horizon=2) == [120_000, 120_000]


def test_terminal_value_net_of_sale_costs():
    assert terminal_value(500_000, 0.05, 0.01) == pytest.approx(9_900_000)


def test_present_value_declines_as_discount_rate_rises():
    flows = [100_000] * 10
    assert present_value(flows, 0.07) > present_value(flows, 0.10)
