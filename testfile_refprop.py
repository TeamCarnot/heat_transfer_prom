# Import the main class from the Python library
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
import os
# Imports from the standard library
import glob

# Imports from conda-installable packages
import pandas

# Import numpy
import numpy as np

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Now we instantiate the library, and use the environment variable to
# explicitly state which path we want to use. It was decided to make
# the path handling explicit (though more verbose), because explicit
# is almost always better than implicit
RP = REFPROPFunctionLibrary(os.environ['RPPREFIX'])

# Now we tell REFPROP what the root directory is that it should use.  This root directory should contain, at least:
# A) REFPRP64.DLL (or REFPROP.dll for 32-bit windows, or librefprop.so or librefprop.dylib, for linux or OSX respectively)
# B) FLUIDS folder (case sensitive)
# C) MIXTURES folder (case sensitive)
RP.SETPATHdll(os.environ['RPPREFIX'])

# Get the unit system we want to use (we will revisit this GETENUM function later)
MOLAR_BASE_SI = RP.GETENUMdll(0, "MOLAR BASE SI").iEnum


# first example
p_Pa = 101.325
Q = 0
FLDpath = os.path.join(os.environ['RPPREFIX'],"FLUIDS","WATER.FLD")
r = RP.REFPROPdll(FLDpath,"PQ","T",MOLAR_BASE_SI,0,0,p_Pa,Q,[1.0])
print(r.Output[0])
RP.SETFLUIDSdll("Water");
l = RP.ABFLSHdll("PQ", p_Pa, Q, [1.0], 000)
print(l)


def fluid_properties_2p(ab: str, a: float, b: float, z: float, fluid: str):
    RP.SETFLUIDSdll(fluid)
    properties = RP.ABFLSHdll(ab, a, b, z, iFlags=030)
    properties_l = RP.ABFLSHdll(ab, a, b, z, iFlags=030)
    properties_v = RP.ABFLSHdll(ab, a, b, z, iFlags=030)



fluid_properties_nd("PQ", p_Pa, Q, [1.0],'water')