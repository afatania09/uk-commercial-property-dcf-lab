import pytest
from reconciliation import capitalise_rent, implied_initial_yield, reconcile

def test_capitalise_rent():
    assert capitalise_rent(100_000, .05) == pytest.approx(2_000_000)

def test_implied_initial_yield():
    assert implied_initial_yield(300_000, 5_000_000) == pytest.approx(.06)

def test_reconciliation_variance():
    r=reconcile(5_100_000,5_000_000,5_050_000)
    assert r["dcf_vs_implicit_pct"] == pytest.approx(2.0)
