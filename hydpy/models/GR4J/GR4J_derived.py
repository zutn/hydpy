# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:21:22 2017

@author: bodereau
"""
# import...
# ...from standard library
from __future__ import division, print_function
# ...HydPy specific
from hydpy.core import parametertools

class qfactor(parametertools.SingleParameter):
    """Factor for converting mm/stepsize to m³/s."""
    NDIM, TYPE, TIME, SPAN = 0, float, None, (0., None)

class DerivedParameters(parametertools.SubParameters):
    """Derived parameters of HydPy-H-Land, indirectly defined by the user."""
    _SEQCLASSES = (qfactor,)

