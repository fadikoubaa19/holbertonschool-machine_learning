#!/usr/bin/env python3
"""3-bayes_opt"""


import numpy as np
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """Create new class named bayesian"""
    def __init__(self, f, X_init, Y_init, bounds, ac_samples,
                 l=1, sigma_f=1, xsi=0.01, minimize=True):
        self.f = f

        self.X_s = np.linspace(bounds[0], bounds[1], ac_samples)[:, None]

        self.xsi = xsi

        self.minimize = minimize

        self.gp = GP(X_init, Y_init, l=l, sigma_f=sigma_f)

    def acquisition(self):
        """Calculate next best sample location"""
        rgb, _ = self.gp.predict(self.gp.X)
        delta, numt = self.gp.predict(self.X_s)
        plts = np.min(rgb)
        rsn = plts - delta - self.xsi
        if not self.minimize:
            rs = -rsn
        cr = rsn / nums
        rslt = rsn * norm.cdf(cr) + nums * norm.pdf(cr)
        return self.X_s[np.argmax(rslt)], rslt
