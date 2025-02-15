def validate_positive_float(value, error_message):
    """
    Validate if the input is a positive float.
    
    Parameters:
        value (str): Input string to validate.
        error_message (str): Error message to display if validation fails.
        
    Returns:
        float: Validated positive float.
    """
    try:
        val = float(value)
        if val <= 0:
            raise ValueError
        return val
    except ValueError:
        raise ValueError(error_message)

def validate_positive_int(value, error_message):
    """
    Validate if the input is a positive integer.
    
    Parameters:
        value (str): Input string to validate.
        error_message (str): Error message to display if validation fails.
        
    Returns:
        int: Validated positive integer.
    """
    try:
        val = int(value)
        if val <= 0:
            raise ValueError
        return val
    except ValueError:
        raise ValueError(error_message)
