import os
from os.path import basename, dirname, join as path_join
import sys
import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)  #DEBUG # ERROR #Warning #Critical #Info
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()  #; console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter("%(levelname)s:%(filename)s:%(message)s")
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logger.addHandler(console)

def get_directory_of(filepath, how_many_times = 0):
    if how_many_times <= 0:
        return dirname(filepath)
    else:
        return dirname(get_directory_of(filepath, how_many_times-1))
        
logger.debug(get_directory_of(__file__, 1))


path_ = path_join(get_directory_of(__file__, 1), "src")
logger.info(path_)
sys.path.append(path_)
logger.debug(f"Sys-path='{path_}'")

# Attempt import
try:
    from auxiliary.timeseries import TimeSeries
    logger.info("TimeSeries object imported successfully")
except Exception as e:
    logger.exception(e)

# Check for correct time_string parsing
ts = TimeSeries([], [], {"time_string":"4h"})
assert ts._time_frame == 'h'
assert ts._time_coefficient == 4 
assert ts._time_magnitude == 3600 * 4
logger.info("time_string is parsed and resolved successfully")

# :TODO: check for correct time_data and value_data assignment
# :TODO: check for correct convert_time_scale behavior


logger.info("Tests passed successfully")