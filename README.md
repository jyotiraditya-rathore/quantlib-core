# quantlib-core

[![Tests](https://github.com/jyotiraditya-rathore/quantlib-core/actions/workflows/tests.yml/badge.svg)](https://github.com/jyotiraditya-rathore/quantlib-core/actions/workflows/tests.yml)

A quantitative finance library built  for option pricing and risk analysis.

## Black–Scholes Option Pricing

The Black–Scholes model assumes the stock price follows geometric brownian motion:

$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

Under the risk neutral measure (using the bank account as numeraire), the drift becomes the risk free rate $r$. The call option price is the discounted expected payoff

$$ C = e^{-rT} \mathbb{E}^Q[(S_T - K)^+] $$

Because $S_T$ is lognormal, the expectation evaluates to the closed form solution

$$ C = S_0 N(d_1) - K e^{-rT} N(d_2) $$

$$ d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T} $$

The put price follows from put call parity

$$ P = C - S_0 + K e^{-rT} $$

## Greeks

The library implements analytical first and second order Greeks:
- **Delta**: $\Delta_c = N(d_1)$, $\Delta_p = N(d_1) - 1$
- **Gamma**: $\Gamma = \frac{N'(d_1)}{S_0 \sigma \sqrt{T}}$
- **Vega**: $\mathcal{V} = S_0 N'(d_1) \sqrt{T} / 100$
- **Theta**: time decay (daily)
- **Rho**: sensitivity to the risk-free rate

All Greeks are verified against finite difference approximations in the test suite.

## Installation

```bash
git clone https://github.com/jyotiraditya-rathore/quantlib-core.git
cd quantlib-core
python -m venv .venv
.venv\Scripts\activate 
pip install -e ".[dev]"
pytest