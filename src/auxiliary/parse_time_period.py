import logging

logger = logging.getLogger(__name__)
logger.setLevel("ERROR") #DEBUG
logger.addHandler(logging.StreamHandler())

def parse_time_period(time_period:str):
    # Compatible time_period chars:
    compatible_chars = [
        "s",  # Second
        "m",  # Minute
        "h",  # Hour
        "d",  # Day
        "w",  # Week
        "M",  # Month
        "y",  # Year
    ]

    chars_in_second = {
        "s": 1,  # Second
        "m": 60,  # Minute
        "h": 3600,  # Hour
        "d": 86400,  # Day
        "w": 604800,  # Week
        "M": 2592000,  # Month
        "y": 31536000,  # Year
    }

    time_frame = time_period[-1]
    if time_frame in compatible_chars:
        pass
    else:
        raise ValueError(f"\"time_period\":{time_period} contains\
            invalid character.")
        
    dummy = time_period[0:-1]
    if len(dummy)>0:
        coefficient = float(dummy)
    else:
        coefficient = 1
    del dummy

    magnitude = chars_in_second[time_frame]*coefficient

    # How many seconds is explained in the contained time_period
    return time_frame, coefficient, magnitude
