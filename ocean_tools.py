import numpy as np

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


