#!/usr/bin/env python3
""" function that  that calculates the PDF at a data point"""
import numpy as np

    def pdf(self, x):
        """
        function that calc pdf at data point
        x : contain data point
        x in 2 cases:
        if not numpy raise TypeEroor or if not shape raise valueEroor
        """

        # if x isnt np.ndarray raise Type Error includded with msg
        if type(x) is not np.ndarray:
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]

        # if x isnt the shap of d,i raise Value error includded with msg
        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # Compute the derterminant of an array
        det = np.linalg.det(self.cov)

        # reverse matrix using inv multiplicative
        inv = np.linalg.inv(self.cov)

        # product of arrays using dot
        first_phase = 1 / ((2 * np.pi)**(d/2) * np.sqrt(det))
        sec_phase = np.dot((x-self.mean).T, inv)
        third_phase = np.dot(sec_phase, (x - self.mean) / -2)
        pdf = first_phase * np.exp(third_phase)

        # Return the value of PDF
        return pdf[0][0]
