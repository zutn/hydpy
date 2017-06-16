# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:42:27 2017

@author: bodereau
"""

# import...
# ...from standard library
from __future__ import division, print_function
 # ...HydPy specific
from hydpy.core import sequencetools

class s(sequencetools.StateSequence):
    """Water level in soil-moisture storage"""
    NDIM, NUMERIC, SPAN = 1, False, (0., None)

class r(sequencetools.StateSequence):
    """Water level in routine storage"""
    NDIM, NUMERIC, SPAN = 1, False, (0., None)

class StateSequences(sequencetools.StateSequences):
    """Input sequences of the GR4J model."""
    _SEQCLASSES = (s, r)