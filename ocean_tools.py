import numpy as np
import pandas as pd

def coriolis_parameter(lat,omega=7.2921e-5):
    """Computes the coriolis parameter for a given latitude
    Input: latitude,
     omega is the Earth's angular velocity in rad/s
    Output: Coriolis parameter """
    
    return 2*omega*np.deg2rad(lat)


def find_mld(density_array,depth_array,reference_index):
    """Find the index and corresponding mixed layer depth of a density profile
    following de Boyer Montegut (2004)
    Input: Array of density in the vertical (kg/m3),
    Array of depths in the vertical (m),
    Index corresponding to reference depth
    Output: Float of MLD and index integer"""

    index=(np.abs(density_array[:]-density_array[reference_index])>=0.03).argmax()
    mld=depth_array[index]

    return index, mld


def grid2d(x, y, v, xi=1, yi=1, fn='median'):
    """
    Grids numpy arrays in 2-dimensions with a function of choice.
    Pretty quick and flexible - that's the point.
    
    Inputs:
    x, y, v: np.array
        x coordinates, y coordinates and values to be gridded.
    xi, yi: int or np.array (default = 1)
        defines bins of output grid. If int, spacing between min and max, 
        or array defines bins directly.
    fn: function or string (default = 'median')
        function to be applied to aggregated data per bin, for example mean, median, var.
        Can also take anonymous functions for more complex operations.
        
    Outputs:
    grid:
        gridded values.
    X, Y:
        gridded coordinates the same size as grid.
        
    Bastien Y. Queste - bastien.queste@gu.se
    www.FLOW-Lab.org - 2024-12-02
    """
    if np.size(xi) == 1:
        xi = np.arange(np.nanmin(x), np.nanmax(x)+xi, xi)
    if np.size(yi) == 1:
        yi = np.arange(np.nanmin(y), np.nanmax(y)+yi, yi)

    raw = pd.DataFrame({'x':x,'y':y,'v':v}).dropna()

    grid = np.full([np.size(yi),np.size(xi)], np.nan)
    
    raw['xbins'],xbin_iter = pd.cut(raw.x, xi,retbins=True,labels=False,right=False)
    raw['ybins'],ybin_iter = pd.cut(raw.y, yi,retbins=True,labels=False,right=False)

    _tmp = raw.groupby(['xbins','ybins'])['v'].agg(fn)
    grid[_tmp.index.get_level_values(1).astype(int),_tmp.index.get_level_values(0).astype(int)] = _tmp.values

    XI,YI = np.meshgrid(xi, yi, indexing='ij')
    return grid,XI.T,YI.T
