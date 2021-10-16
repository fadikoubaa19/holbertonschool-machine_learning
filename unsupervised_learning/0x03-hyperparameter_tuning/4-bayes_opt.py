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
        """function acuiqs"""
        pl_1, pl_2 = self.gp.predict(self.X_s)

        if self.minimize is True:
            value = np.min(self.gp.Y)
            retour = value - pl_1 - self.xsi

        else:
            value = np.max(self.gp.Y)
            retour = pl_1 - value - self.xsi

        with np.errstate(divide='warn'):
            Z = retour / pl_2
            EI = retour * norm.cdf(Z) + pl_2 * norm.pdf(Z)

        X_next = self.X_s[np.argmax(EI)]

        return X_next, EI
