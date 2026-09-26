import pytest

from dcf_engine import DCFInputs, dcf_value, present_value, terminal_value


def test_present_value():
    assert present_value(108, 0.08, 1) == pytest.approx(100)


def test_terminal_value():
    assert terminal_value(600_000, 0.06) == pytest.approx(10_000_000)


def test_simple_dcf():
    inputs = DCFInputs(
        annual_cash_flows=[100_000] * 10,
        discount_rate=0.08,
        terminal_erv=100_000,
        exit_yield=0.06,
    )
    assert dcf_value(inputs) > 0


def test_exit_yield_must_be_positive():
    with pytest.raises(ValueError):
        terminal_value(100_000, 0)
