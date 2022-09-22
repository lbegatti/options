from scipy.stats import norm
import numpy as np


class BS:
    def __init__(self, spot, strike, expiry, r, sigma):
        self.spot = spot
        self.strike = strike
        self.expiry = expiry
        self.r = r
        self.sigma = sigma

    def d1(self):
        return(np.log(self.spot/self.strike)+(self.r+0.5*self.sigma*self.sigma)*self.expiry)/(self.sigma*np.sqrt(self.expiry))

    def d2(self):
        return self.d1()-self.sigma*np.sqrt(self.expiry)

    def call_price(self):
        return self.spot * norm.cdf(self.d1()) - self.strike * np.exp(-self.r * self.expiry) * norm.cdf(self.d2())
