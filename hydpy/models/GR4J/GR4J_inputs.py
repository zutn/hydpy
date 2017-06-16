# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:19:44 2017

@author: bodereau
"""
# import...
# ...from standard library
from __future__ import division, print_function
# ...HydPy specific
from hydpy.core import sequencetools


class p(sequencetools.InputSequence):
    """Precipitation [mm]."""
    NDIM, NUMERIC = 0, False


class e(sequencetools.InputSequence):
    """Normal potential evaporation [mm]."""
    NDIM, NUMERIC = 0, False

class InputSequences(sequencetools.InputSequences):
    """Input sequences of the hland model."""
    _SEQCLASSES = (p, e)
