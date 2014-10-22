import pandas as pd
from ggplot import *
from datetime import datetime


def get_day(date_str):
    return datetime.strftime(datetime.strptime(date_str, "%Y-%m-%d").date(), "%a")


def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''
    turnstile_weather["DAYn"] = turnstile_weather["DATEn"].map(get_day)
    entries_by_days = (turnstile_weather[["DAYn", "ENTRIESn_hourly"]].groupby(by="DAYn", as_index=False)).sum()
    #idx = [3, 1, 5, 6, 4, 0, 2]
    #entries_by_days = entries_by_days.iloc[idx]
    plot = ggplot(entries_by_days, aes("DAYn")) + \
      geom_bar(aes(weight='ENTRIESn_hourly'), fill='red') + \
      ggtitle("Total Hourly Entries by Days of Week")

    return plot


if __name__ == "__main__":
    input_filename = "../data/turnstile_data_master_with_weather.csv"
    image = "dv1.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg, format="png")
