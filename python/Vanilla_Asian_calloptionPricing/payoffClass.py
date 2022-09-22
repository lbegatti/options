class Payoff:
    def __init__(self, strike):
        self.strike = strike

    def payoff(self, spot: float):
        return max(spot - self.strike, 0)
