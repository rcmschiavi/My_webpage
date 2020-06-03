import datetime

import pytz
import pandas as pd
import numpy as np
from applications.models import Temperature


def get_temp_by_hour():
    tz = pytz.timezone('America/Porto_Velho')
    date = datetime.datetime.now(tz)
    day = date.day
    month = date.month
    year = date.year
    # A complete query that returns just the values from the current day
    dataset = Temperature.objects.order_by('-REGISTERED_AT') \
        .filter(REGISTERED_AT__gte=datetime.datetime(year, 5, 4, tzinfo=tz)) \
        .exclude(TEMPERATURE__lte=-120).values('TEMPERATURE', 'REGISTERED_AT')
    df, df_group_hour = df_manipulation(dataset)
    listData = format_data(df, df_group_hour)
    return listData

def df_manipulation(dataset):
    df = pd.DataFrame(list(dataset))
    df.REGISTERED_AT = pd.to_datetime(df.REGISTERED_AT)
    df.REGISTERED_AT = df.REGISTERED_AT.dt.tz_convert('America/Caracas')
    df.TEMPERATURE = df.TEMPERATURE.astype(float)
    hour = pd.to_timedelta(df.REGISTERED_AT.dt.hour, unit='H')
    hour.name = "REGISTERED_AT"
    df_group_hour = df.groupby(hour).mean()
    return df, df_group_hour


def format_data(df, df_group_hour):
    # Function to format the data for google charts data format, also got the max and min temperature
    data_dict: {}
    list_data = []
    NS_IN_ONE_HOUR = 3600000000000
    for hour in df_group_hour.index:
        delta_hour = np.timedelta64(hour.to_numpy(), 'ns')
        delta_hour = int(delta_hour / NS_IN_ONE_HOUR)
        df_hour = df[df.REGISTERED_AT.dt.hour == delta_hour]
        data_dict = {"v": [delta_hour, 0, 0], "f": "Time: " + str(delta_hour) + ":00"}
        list_hour = [data_dict, df_hour.max().TEMPERATURE, df_hour.mean().round(2).TEMPERATURE, df_hour.min().TEMPERATURE]
        list_data.append(list_hour)
    return list_data