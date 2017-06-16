# -*- coding: utf-8 -*-

# import...
# ...from standard library
from __future__ import division, print_function
# ...HydPy specific
from hydpy.core import sequencetools


class quh1(sequencetools.LogSequence):
    """Whole outflow delayed by means of the unit hydrograph [mm]."""
    NDIM, NUMERIC, SPAN = 1, False, (0., None)

class quh2(sequencetools.LogSequence):
    """Whole outflow delayed by means of the unit hydrograph [mm]."""
    NDIM, NUMERIC, SPAN = 1, False, (0., None)

class sh1(sequencetools.LogSequence):
     NDIM, TYPE, TIME, SPAN = 1, float, None, (0., 1.)

class sh2(sequencetools.LogSequence):
     NDIM, TYPE, TIME, SPAN = 1, float, None, (0., 1.)

class uh1(sequencetools.LogSequence):
    """Unit hydrograph ordinates [-]."""
    NDIM, TYPE, TIME, SPAN = 1, float, None, (0., 1.)

class uh2(sequencetools.LogSequence):
    """Unit hydrograph ordinates [-]."""
    NDIM, TYPE, TIME, SPAN = 1, float, None, (0., 1.)

class LogSequences(sequencetools.LogSequences):
    """Log sequences of the GR4J model."""
    _SEQCLASSES = (quh1, quh2, sh1, sh2, uh1, uh2)