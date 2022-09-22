from princingExercise.option import Option
import numpy as np
from math import exp, sqrt
import random


class GBM:
    def __init__(self, spot, r, sigma, paths, timesteps):
        self.spot = spot
        self.r = r
        self.sigma = sigma
        self.paths = paths
        self.timesteps = timesteps
        self.simulated_spot = np.zeros([self.timesteps, self.paths])
        self.option = None

    def simulate_spot(self):
        self.simulated_spot[0, ] = self.spot
        dt = self.option.expiry / self.timesteps
        moved_spot = (self.r - 0.5 * self.sigma*self.sigma)*dt
        for path in range(self.paths):
            for date in range(1, self.timesteps):
                self.simulated_spot[date, path] = self.simulated_spot[date-1, path] * exp(moved_spot + self.sigma*sqrt(dt) * random.gauss(0, 1))
        return None

    def option_value(self, option: Option):
        self.option = option
        self.simulate_spot()
        if option.option_type == 'european':
            option_value = sum([option.payoff(self.simulated_spot[-1, path]) for path in range(self.paths)]) / self.paths
        elif option.option_type == 'asian':
            avg_spot = self.simulated_spot.sum(axis=0) / self.timesteps
            option_value = sum([option.payoff(avg) for avg in avg_spot]) / self.paths
        else:
            raise ValueError('This option pricer only supports european and asian option types.')
        return exp(-self.r * self.option.expiry) * option_value
