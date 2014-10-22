import sys
import string
import logging

def mapper():
    '''
    In this exercise, we want to compute the average value of the
    ENTRIESn_hourly column broken down by different weather types.  We will
    define a weather type based on the combination of the columns fog and rain
    (which are boolean values).  So for example, one output of our reducer
    would be the average hourly riders across all hours when it was raining and
    not foggy.

    Each line of input will look like a row from our final Subway-MTA dataset, in csv format.
    You can check out the input csv file and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    
    Note that this is a comma-separated file.

    This mapper should
    1) return the weather type as the key - use the given helper function to format the
        weather type correctly
    2) the number in the ENTRIEsn_hourly column as the value
    3)  The key and the value should be separated by a tab.
        For example: fog-norain\t12345

    An example output line to the reducer would look like this:
    fog-norain    12345
    
    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    '''

    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that you should output.  The variables passed in
    # can be booleans, ints (0 for false and 1 for true) or floats (0.0 for
    # false and 1.0 for true), but the strings '0.0' and '1.0' will not work,
    # so make sure you convert these values to an appropriate type before
    # calling the function.
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )

    for line in sys.stdin:
        data = line.split(",")
        if len(data) != 22 or data[0] == "":
            continue
        
        key, val = format_key(float(data[14]), float(data[15])), data[6]
        print "{0}\t{1}".format(key, val)


mapper()
