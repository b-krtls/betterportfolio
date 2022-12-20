# :TODO:

import logging 
import typing
import pandas as pd

from .parse_time_period import parse_time_period

logger = logging.getLogger(__name__)
logger.setLevel("ERROR") #DEBUG
logger.addHandler(logging.StreamHandler())

class TimeSeries:
    # :NOTE:
    # datetime strftime() format
    def __init__(self,
                 time_data: pd.Series,
                 value_data: pd.Series,
                 metadata: dict) -> None:
        self.time_data = time_data
        self.value_data = value_data
        self.metadata = metadata

        self.time_string = self.metadata["time_string"]
        (
        self._time_frame,
        self._time_coefficient,
        self._time_magnitude
        ) = parse_time_period(self.time_string)

    def convert_time_scale(self, new_time_period):
        tf, c, m = parse_time_period(self._time_frame)
        tf_new, p_new, m_new = parse_time_period(new_time_period)
        
        if m < m_new:
            # :TODO: Implement conversion logic.
            pass
        else:
            # Larger timeframe magnitude to smaller timeframe conversion 
            #   is erronous
            raise ValueError(f"Conversion to \
                \"new_time_period\":{new_time_period} \
                is not plausible since it is smaller than original data"
            )
            
    
