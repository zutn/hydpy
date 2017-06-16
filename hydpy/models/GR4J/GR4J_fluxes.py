# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:11:03 2017

@author: bodereau
"""
# import...
# ...standard library
from __future__ import division, print_function
# ...HydPy specific
from hydpy.core import sequencetools

class en(sequencetools.FluxSequence):
    """net evaporations [mm]"""
    NDIM, NUMERIC = 0, False

class pn(sequencetools.FluxSequence):
    """net precipitations [mm]"""
    NDIM, NUMERIC = 0, False

class es(sequencetools.FluxSequence):
    """net evaporations that influences the soil-moisture storage [mm]"""
    NDIM, NUMERIC = 0, False

class ps(sequencetools.FluxSequence):
    """net precipitations that influences the soil-moisture storage [mm]"""
    NDIM, NUMERIC = 0, False

class perc(sequencetools.FluxSequence):
    """percolation between the upper and the lower layer [mm] """
    NDIM, NUMERIC = 0, False

class pf(sequencetools.FluxSequence):
    """Pn-Ps+Perc [mm]"""
    NDIM, NUMERIC = 0, False

class f(sequencetools.FluxSequence):
    """water mass exchanged between the upper and lower zone [mm]"""
    NDIM, NUMERIC = 0, False

class quh1(sequencetools.FluxSequence):
    """rapid flow [mm]"""
    NDIM, NUMERIC = 0, False

class quh2(sequencetools.FluxSequence):
    """slow flow [mm]"""
    NDIM, NUMERIC = 0, False

class qr(sequencetools.FluxSequence):
    """routing storage outflow [mm]"""
    NDIM, NUMERIC = 0, False

class qd(sequencetools.FluxSequence):
    """flow component [mm]"""
    NDIM, NUMERIC = 0, False

class q(sequencetools.FluxSequence):
    """total flow [m³/s]"""
    NDIM, NUMERIC = 0, False

class FluxSequences(sequencetools.FluxSequences):
    """Input all fluxes of GR4J Model."""
    _SEQCLASSES = (en, pn, es, ps, perc, pf, f, quh1, quh2, qr, qd, q)