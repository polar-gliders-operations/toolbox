import pytest
import numpy as np

# import module
import sys
import os

parent_dir = os.path.dirname('../')
sys.path.append(parent_dir)

from ocean_tools import find_mld

# make a fake density profile

density = np.linspace(1026.5,1027.5,100)

# add a mixed layer
density[:30]=1026.5
depth = np.arange(0,200,2)
reference_index = 5

index, mld = find_mld(density, depth, reference_index)
assert index == 30
assert mld == 60