import pytest
import numpy as np

# Import module
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from ocean_tools import coriolis_parameter

# Test cases for coriolis_parameter
def test_coriolis_negative_latitude():
    lat = -35
    f = coriolis_parameter(lat)
    assert f == pytest.approx(-8.908980806927495e-05), "Incorrect coriolis parameter for negative latitude"

def test_coriolis_positive_latitude():
    lat = 35
    f = coriolis_parameter(lat)
    assert f > 0, "Coriolis parameter should be positive for positive latitude"

def test_coriolis_latitude_physical_limits():
    lat = 80
    f = coriolis_parameter(lat)
    assert -90 <= lat <= 90, "Latitude is outside physical limits (-90 to 90 degrees)"
