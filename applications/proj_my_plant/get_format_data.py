import datetime
import time
from applications.models import My_plant_data
import pytz
import pandas as pd
import numpy as np


def get_data_models():
    start_time = time.time()
    tz = pytz.timezone('America/Porto_Velho')
    date = datetime.datetime.now(tz)
    day = date.day
    month = date.month
    year = date.year
    dataset = My_plant_data.objects.order_by('-REGISTERED_AT').\
        filter(REGISTERED_AT__gte=datetime.datetime(year, 5, 4, tzinfo=tz)).\
        values('TEMPERATURE', 'REGISTERED_AT', 'HUMIDITY', 'MOISTURE')
    df = pd.DataFrame(list(dataset))
    df.REGISTERED_AT = pd.to_datetime(df.REGISTERED_AT)
    df.REGISTERED_AT = df.REGISTERED_AT.dt.tz_convert('America/Caracas')
    df.TEMPERATURE = df.TEMPERATURE.astype(float)
    df.HUMIDITY = df.HUMIDITY.astype(float)
    df.MOISTURE = df.MOISTURE.astype(float)
    hour = pd.to_timedelta(df.REGISTERED_AT.dt.hour, unit='H')
    hour.name = "REGISTERED_AT"
    df = df.groupby(hour).mean().round(2)
    return format_data(df),(start_time - time.time())


def format_data(df):
    # Function to format the data for google charts data format, also got the max and min temperature
    data_dict: {}
    list_data = []
    NS_IN_ONE_HOUR = 3600000000000
    for index, row in df.iterrows():
        delta_hour = np.timedelta64(index.to_numpy(), 'ns')
        delta_hour = int(delta_hour / NS_IN_ONE_HOUR)
        list_hour = [[delta_hour, 0, 0], row['TEMPERATURE'], row['HUMIDITY'], row['MOISTURE']]
        list_data.append(list_hour)
    return list_data