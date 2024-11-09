import numpy as np

def coriolis_parameter(lat,omega=7.2921e-5):
    """Computes the coriolis parameter for a given latitude
    Input: latitude,
     omega is the Earth's angular velocity in rad/s """
    
    return 2*omega*np.deg2rad(lat)

