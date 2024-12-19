import pytest
import numpy as np

# Import module
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from ocean_tools import find_mld

def test_find_mld():
    # Create a fake density profile
    density = np.linspace(1026.5, 1027.5, 100)

    # Add a mixed layer
    density[:30] = 1026.5
    depth = np.arange(0, 200, 2)
    reference_index = 5

    # Call the function
    index, mld = find_mld(density, depth, reference_index)

    # Assertions
    assert index == 30, f"Expected index 30, got {index}"
    assert mld == 60, f"Expected mld 60, got {mld}"
