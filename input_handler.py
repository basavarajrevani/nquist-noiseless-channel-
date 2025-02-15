from utils import validate_positive_float, validate_positive_int

def get_user_inputs():
    """
    Get and validate user inputs for bandwidth and levels.
    
    Returns:
        tuple: A tuple containing bandwidth (float) and levels (int).
    """
    # Get bandwidth
    bandwidth = input("Enter the channel bandwidth (Hz): ")
    bandwidth = validate_positive_float(bandwidth, "Bandwidth must be a positive number.")
    
    # Get levels
    levels = input("Enter the number of distinct signal levels: ")
    levels = validate_positive_int(levels, "Levels must be a positive integer.")
    
    return bandwidth, levels
