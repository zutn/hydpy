# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:53:07 2017

@author: bodereau
"""

# import...
# ...from standard library
from __future__ import division, print_function
# ...third party
import numpy
from numpy import nan
# ...HydPy specific
# Load the required `magic` functions into the local namespace.
from hydpy.core.magictools import parameterstep
from hydpy.core.magictools import simulationstep
from hydpy.core.magictools import controlcheck
from hydpy.core.magictools import Tester
#from hydpy.cythons.modelutils import Cythonizer


from hydpy.models.GR4J.GR4J_parameters import Parameters
from hydpy.models.GR4J.GR4J_control import ControlParameters
from hydpy.models.GR4J.GR4J_sequences import Sequences
from hydpy.models.GR4J.GR4J_inputs import InputSequences
from hydpy.models.GR4J.GR4J_fluxes import FluxSequences
from hydpy.models.GR4J.GR4J_states import StateSequences
from hydpy.models.GR4J.GR4J_logs import LogSequences
from hydpy.models.GR4J.GR4J_model import Model
from hydpy.models.GR4J.GR4J_derived import DerivedParameters

tester = Tester()
#cythonizer = Cythonizer()
#cythonizer.complete()