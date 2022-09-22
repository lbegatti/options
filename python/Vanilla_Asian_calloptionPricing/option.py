from pricingExercise.payoffClass import Payoff

class Option:
    def __init__(self, payoff_type: Payoff, expiry, option_type):
        self.expiry = expiry
        self.payoff_type = payoff_type
        self.option_type = option_type

    def payoff(self, spot):
        return self.payoff_type.payoff(spot)
