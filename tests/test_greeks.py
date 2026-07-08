import numpy as np
from quantlib.pricing.black_scholes import (
    call_price, delta_call, delta_put,
    gamma, vega, theta_call, theta_put, rho_call, rho_put, put_price
)

S, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.2
eps = 1e-4

def test_delta_call_finite_difference():
    analytic = delta_call(S, K, T, r, sigma)
    price_up = call_price(S + eps, K, T, r, sigma)
    price_down = call_price(S - eps, K, T, r, sigma)
    numerical = (price_up - price_down) / (2 * eps)
    assert np.isclose(analytic, numerical, rtol=1e-3)

def test_delta_put_finite_difference():
    analytic = delta_put(S, K, T, r, sigma)
    price_up = put_price(S + eps, K, T, r, sigma)
    price_down = put_price(S - eps, K, T, r, sigma)
    numerical = (price_up - price_down) / (2 * eps)
    assert np.isclose(analytic, numerical, rtol=1e-3)

def test_gamma_finite_difference():
    analytic = gamma(S, K, T, r, sigma)
    price_up = call_price(S + eps, K, T, r, sigma)
    price = call_price(S, K, T, r, sigma)
    price_down = call_price(S - eps, K, T, r, sigma)
    numerical = (price_up - 2*price + price_down) / (eps**2)
    assert np.isclose(analytic, numerical, rtol=1e-3)

def test_vega_finite_difference():
    analytic = vega(S, K, T, r, sigma)
    vol_up = sigma + 0.0001
    vol_down = sigma - 0.0001
    price_up = call_price(S, K, T, r, vol_up)
    price_down = call_price(S, K, T, r, vol_down)
    numerical = (price_up - price_down) / (0.0002 * 100)
    assert np.isclose(analytic, numerical, rtol=1e-3)

def test_theta_call_finite_difference():
    analytic = theta_call(S, K, T, r, sigma)
    price_up = call_price(S, K, T - eps, r, sigma)
    price = call_price(S, K, T, r, sigma)
    numerical = (price_up - price) / (eps * 365)
    assert np.isclose(analytic, numerical, rtol=1e-3)

def test_rho_call_finite_difference():
    analytic = rho_call(S, K, T, r, sigma)
    rate_up = r + 0.0001
    rate_down = r - 0.0001
    price_up = call_price(S, K, T, rate_up, sigma)
    price_down = call_price(S, K, T, rate_down, sigma)
    numerical = (price_up - price_down) / (0.0002 * 100)
    assert np.isclose(analytic, numerical, rtol=1e-3)