import numpy as np
from quantlib.pricing.black_scholes import call_price, put_price

def test_call_price_at_the_money():
    S = 100.0
    K = 100.0
    T = 1.0
    r = 0.05
    sigma = 0.2
    expected = 10.450583572185565
    result = call_price(S, K, T, r, sigma)
    assert np.isclose(result, expected, rtol=1e-6)

def test_put_call_parity():
    S, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.2
    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)
    parity_diff = call - put - (S - K * np.exp(-r * T))
    assert np.isclose(parity_diff, 0.0, atol=1e-10)

def test_put_price_value():
    S, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.2
    expected_put = 5.573526022256971
    result = put_price(S, K, T, r, sigma)
    assert np.isclose(result, expected_put, rtol=1e-6)