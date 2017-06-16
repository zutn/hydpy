# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:04:15 2017

@author: bodereau
"""
#import...from standard library
from __future__ import division, print_function

#import ... from Hydpy library
from hydpy.core import parametertools

class Area(parametertools.SingleParameter):
    """Bassin area [km²]."""
    NDIM, TYPE, TIME, SPAN = 0, float, None, (1e-10, None)

class x1(parametertools.SingleParameter):
    """Maximum water level coefficient of the soil-moisture storage [mm]"""
    NDIM, TYPE, TIME, SPAN = 0, float, None, (1e-10, None)

class x2(parametertools.SingleParameter):
    """Groundwater exchange coefficient [mm] """
    NDIM, TYPE, TIME, SPAN = 0, float, None, (1e-10, None)

class x3(parametertools.SingleParameter):
    """Maximum water level coefficient of the routing storage [mm] """
    NDIM, TYPE, TIME, SPAN = 0, float, None, (1e-10, None)

class x4(parametertools.SingleParameter):
    """Time base of unit hydrograph [days] """
    NDIM, TYPE, TIME, SPAN = 0, float, None, (1e-10, None)

    def __call__(self, *args, **kwargs):
        """The prefered way to pass values to :class:`Parameter` instances
        within parameter control files.
        """
        parametertools.SingleParameter.__call__(self, *args, **kwargs)
        derived = self.subpars.pars.derived
        logs = self.subpars.pars.model.sequences.logs
        derived.uh.shape = self.values
        logs.quh.shape = self.value


class ControlParameters(parametertools.SubParameters):
    """Control parameters of HydPy-H-Land, directly defined by the user."""
    _PARCLASSES = (Area, x1, x2, x3, x4)