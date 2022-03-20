"""
Collection of Numpy reduction functions, wrapped to fit Ivy syntax and signature.
"""

# global
import numpy as _np
import numpy.array_api as _npa


def einsum(equation, *operands):
    return _np.asarray(_np.einsum(equation, *operands))