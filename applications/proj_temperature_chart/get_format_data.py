import datetime
from datetime import timedelta
import pytz
import pandas as pd
import numpy as np
from applications.models import Temperature


def get_temp_by_hour():
    tz = pytz.timezone('America/Porto_Velho')
    last_post = Temperature.objects.order_by('REGISTERED_AT').values('REGISTERED_AT').last()
    date_from = last_post['REGISTERED_AT'] - timedelta(days=1)
    day_from = date_from.day
    month_from = date_from.month
    year_from = date_from.year
    date_to = date_from + timedelta(days=1)
    day_to = date_to.day
    month_to = date_to.month
    year_to = date_to.year
    # A complete query that returns just the values from the current day
    dataset = Temperature.objects.order_by('-REGISTERED_AT') \
        .filter(REGISTERED_AT__gte=datetime.datetime(year_from, month_from, day_from, tzinfo=tz), REGISTERED_AT__lte=datetime.datetime(year_to, month_to, day_to, tzinfo=tz))\
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