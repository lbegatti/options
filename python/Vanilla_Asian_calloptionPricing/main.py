from pricingExercise.payoffClass import Payoff
from pricingExercise.option import Option
from pricingExercise.gbm import GBM
from pricingExercise.blackscholes import BS

# We make some assumptions about the option
strike = 105
spot = 110
expiry = 1
sigma = 0.15
r = 0.02
paths = 1500
timesteps = 126

# Instantiate class constructors and price the option
call = Payoff(strike=strike)
gbm = GBM(spot=spot, r=r, sigma=sigma, paths=paths, timesteps=timesteps)
european_call = gbm.option_value(Option(payoff_type=call, expiry=expiry, option_type='european'))
analytical_price = BS(spot, strike, expiry, r, sigma).call_price()
asian_call = gbm.option_value(Option(payoff_type=call, expiry=expiry, option_type='asian'))

print("The Monte Carlo price is: {}".format(round(european_call, 2)))
print("The analytical price is: {}".format(round(analytical_price, 2)))
print("The Monte Carlo Asian price is: {}".format(round(asian_call, 2)))

""" Notes 
Asian pricer < European price. This makes sense based on the model assumptions we have, 
there is positive interest rate (drift) and high volatility so S_T will with high probability be higher than all 
the previous values so therefore the AVERAGE(S_t) is most likely lower than S_T and thereby will the price
you pay also be lower.
"""
