import pytest
import numpy as np
import pandas as pd

# import module
import sys
import os

parent_dir = os.path.dirname('../')
sys.path.append(parent_dir)

from ocean_tools import grid2d

V,X,Y = grid2d(np.arange(100),np.arange(100),np.arange(100), xi=2, yi=5, fn=np.nanmean)
V,X,Y = grid2d(np.arange(100),np.arange(100),np.arange(100))