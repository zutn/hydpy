# -*- coding: utf-8 -*-

# imports...
# ...standard library
from __future__ import division, print_function
# ...HydPy specific
from hydpy.core import modeltools
from hydpy.cythons import modelutils
#from hydpy.models.GR4J import *
import numpy as np

def calc_pn_en_v1(self):
    inp = self.sequences.inputs.fastaccess
    flu = self.sequences.fluxes.fastaccess
    if inp.p >= inp.e:
        flu.pn = inp.p-inp.e
        flu.en = 0.
    else:
        flu.en = inp.e-inp.p
        flu.pn = 0.

def calc_es_ps_v1(self):
    flu = self.sequences.fluxes.fastaccess
    sta = self.sequences.states.fastaccess
    con = self.sequences.control.fastaccess
    flu.ps = flu.pn*(1-(sta.s/con.x1)**2)/(1+flu.pn*(1+(sta.s/con.x1)))
    flu.es = flu.en*(sta.s/con.x1)*(2.-(sta.s/con.x1)/(1.+(sta.s/con.x1)*(2.-(sta.s/con.x1))))

def calc_perc_v1(self):
    flu = self.sequences.fluxes.fastaccess
    sta = self.sequences.states.fastaccess
    con = self.sequences.control.fastaccess
    flu.perc = sta.s+(1-(1+(0.44*sta.s/con.x1)**4)**(-0.25))

def calc_s_v1(self):
    flu = self.sequences.fluxes.fastaccess
    sta = self.sequences.states.fastaccess
    sta.s = sta.s-flu.perc

def calc_pf_v1(self):
    flu = self.sequences.fluxes.fastaccess
    flu.pf = flu.perc+flu.pn-flu.ps

def calc_sh1_v1(self):
    """To define a floy rate values at a time precisly for the upper """
    inp = self.sequences.inputs.fastaccess
    con = self.sequences.control.fastaccess
    log = self.sequences.logs.fastaccess
    for k in range(0, len(inp.e)):
        if k == 0:
            log.sh1[k] = 0
        elif 0 < k and k <= con.x4:
            log.sh1[k] = (k/con.x4)**(2.5)
        else:
            log.sh1[k] = 1

def calc_sh2_v1(self):
    inp = self.sequences.inputs.fastaccess
    con = self.sequences.control.fastaccess
    log = self.sequences.logs.fastaccess
    for k in range(0, len(inp.e)):
        if k == 0:
            log.sh2[k] = 0
        elif 0 < k and k <= con.x4:
            log.sh2[k] = 0.5*(k/con.x4)**(2.5)
        elif con.x4 < k and k <= 2*con.x4:
            log.sh2[k] = 1-0.5*(k/con.x4)**(2.5)
        else:
            log.sh1[k] = 1

def calc_uh1_v1(self):
    log = self.sequences.logs.fastaccess
    inp = self.sequences.inputs.fastaccess
    for k in range(0, len(inp.e)):
        log.uh1[k]=log.sh1[k]-log.sh1[k-1]

def calc_uh2_v1(self):
    log = self.sequences.logs.fastaccess
    inp = self.sequences.inputs.fastaccess
    for k in range(0, len(inp.e)):
        log.uh2[k]=log.sh2[k]-log.sh2[k-1]

def calc_quh1_v1(self):
    inp = self.sequences.inputs.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    log = self.sequences.logs.fastaccess
    for k in range(0, len(inp.e)):
        flu.quh1[k] = der.uh1[k]*flu.pf+log.quh1[0]

def calc_quh2_v1(self):
    inp = self.sequences.inputs.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    log = self.sequences.logs.fastaccess
    for k in range(0, len(inp.e)):
         flu.quh2[k] = der.uh2[k]*flu.pf+log.quh2[0]

def calc_f_v1(self):
    sta = self.sequences.states.fastaccess
    con = self.sequences.control.fastaccess
    flu = self.sequences.fluxes.fastaccess
    flu.f = con.x2*(sta.r/con.x3)**(3.5)

def calc_r_v1(self):
    sta = self.sequences.states.fastaccess
    flu = self.sequences.fluxes.fastaccess
    sta.r = np.max(sta.r,flu.quh1+flu.f)

def calc_qr_v1(self):
    sta = self.sequences.states.fastaccess
    con = self.sequences.control.fastaccess
    flu = self.sequences.fluxes.fastaccess
    flu.qr = sta.r*(1-(1+(sta.r/con.x3)**4)**(-0.25))

def calc_qd_v1(self):
    flu = self.sequences.fluxes.fastaccess
    flu.qd = np.max(flu.quh2+flu.f)

def calc_q_factor_v1(self):
    """converting the flow rate from mm/s to m³/s"""
    con = self.sequences.control.fastaccess
    der = self.sequences.derived.fastaccess
    der.qfactor=(con.Area*1000/der.QFactor.simulationstep.seconds)

def calc_q_v1(self):
    """Qd + Qr [mm]"""
    der = self.sequences.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    flu.q = (flu.qd+flu.qr)*der.qfactor

class Model(modeltools.Model):
    _RUNMETHODS = (calc_pn_en_v1,
                   calc_es_ps_v1,
                   calc_perc_v1,
                   calc_s_v1,
                   calc_pf_v1,
                   calc_sh1_v1,
                   calc_sh2_v1,
                   calc_uh1_v1,
                   calc_uh2_v1,
                   calc_quh1_v1,
                   calc_quh2_v1,
                   calc_f_v1,
                   calc_r_v1,
                   calc_qr_v1,
                   calc_qd_v1,
                   calc_q_v1,
                   calc_q_factor_v1)