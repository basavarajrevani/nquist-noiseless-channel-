import math

def calculate_data_rate(bandwidth, levels):
    """
    Calculate the maximum data rate using Nyquist theorem.
    
    Parameters:
        bandwidth (float): The bandwidth of the channel in Hz.
        levels (int): The number of distinct signal levels.
        
    Returns:
        float: Maximum data rate in bits per second.
    """
    if levels <= 1:
        raise ValueError("The number of levels must be greater than 1.")
    
    # Apply Nyquist formula
    data_rate = 2 * bandwidth * math.log2(levels)
    return data_rate
