# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=wildcard-import
"""
The HydPy-A base model provides features to implement flood routing models
based on autoregressive (AR) and moving-average (MA) methods.
"""
# import...
# ...from standard library
from __future__ import division, print_function
# ...from HydPy
from hydpy.core.modelimports import *
# ...from arma
from hydpy.models.arma.arma_control import ControlParameters
from hydpy.models.arma.arma_derived import DerivedParameters
from hydpy.models.arma.arma_fluxes import FluxSequences
from hydpy.models.arma.arma_logs import LogSequences
from hydpy.models.arma.arma_inlets import InletSequences
from hydpy.models.arma.arma_outlets import OutletSequences
from hydpy.models.arma.arma_model import Model

autodoc_basemodel()
tester = Tester()
cythonizer = Cythonizer()
cythonizer.complete()
