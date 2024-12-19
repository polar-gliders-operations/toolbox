import pytest
import numpy as np
import os
import sys

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(parent_dir)

from ocean_tools import grid2d

def test_grid2d_with_custom_params():
    # Test with custom parameters
    V, X, Y = grid2d(np.arange(100), np.arange(100), np.arange(100), xi=2, yi=5, fn=np.nanmean)

    # Validate outputs
    assert isinstance(V, np.ndarray), "V should be a numpy array"
    assert isinstance(X, np.ndarray), "X should be a numpy array"
    assert isinstance(Y, np.ndarray), "Y should be a numpy array"
    assert V.shape == X.shape == Y.shape, "Output shapes of V, X, and Y should match"

def test_grid2d_with_defaults():
    # Test with default parameters
    V, X, Y = grid2d(np.arange(100), np.arange(100), np.arange(100))

    # Validate outputs
    assert isinstance(V, np.ndarray), "V should be a numpy array"
    assert isinstance(X, np.ndarray), "X should be a numpy array"
    assert isinstance(Y, np.ndarray), "Y should be a numpy array"
    assert V.shape == X.shape == Y.shape, "Output shapes of V, X, and Y should match"
