import requests

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes

def make_api_request(api_key:str, lat: str, lon: str, year: str, email: str):
    url = 'https://developer.nrel.gov/api/wind-toolkit/v2/wind/wtk-download.csv?api_key='+api_key+'&wkt=POINT('+lon+'%20'+lat+")&names="+year+'&email='+email
    return url


def make_wind_speed_graph(input_csv: str, save_location: str, title: str, distance: str):
    csv = pd.read_csv(input_csv)
    wind_speed = csv[['Year', 'Month', 'Day', 'Hour', 'Minute', 'wind speed at 10m (m/s)', 'wind speed at 40m (m/s)',
                      'wind speed at 60m (m/s)', 'wind speed at 80m (m/s)', 'wind speed at 100m (m/s)',
                      'wind speed at 120m (m/s)', 'wind speed at 140m (m/s)', 'wind speed at 160m (m/s)',
                      'wind speed at 200m (m/s)']].copy()
    wind_speed.rename(columns={'Year': 'Year', 'Month': 'Month', 'Day': 'Day', 'Hour': 'Hour', 'Minute': 'Minute',
                               'wind speed at 10m (m/s)': 'c10', 'wind speed at 40m (m/s)': 'c40',
                               'wind speed at 60m (m/s)': 'c60', 'wind speed at 80m (m/s)': 'c80',
                               'wind speed at 100m (m/s)': 'c100', 'wind speed at 120m (m/s)': 'c120',
                               'wind speed at 140m (m/s)': 'c140', 'wind speed at 160m (m/s)': 'c160',
                               'wind speed at 200m (m/s)': 'c200'}, inplace=True)
    wind_speed['Date-Time'] = pd.to_datetime(wind_speed[['Year', 'Month', 'Day', 'Hour']])
    grouped_by_hour = wind_speed.groupby(['Month', 'Hour']).mean()
    grouped_by_hour.reset_index(inplace=True)
    jan = grouped_by_hour.loc[grouped_by_hour['Month'] == 1]
    feb = grouped_by_hour.loc[grouped_by_hour['Month'] == 2]
    mar = grouped_by_hour.loc[grouped_by_hour['Month'] == 3]
    apr = grouped_by_hour.loc[grouped_by_hour['Month'] == 4]
    may = grouped_by_hour.loc[grouped_by_hour['Month'] == 5]
    jun = grouped_by_hour.loc[grouped_by_hour['Month'] == 6]
    jul = grouped_by_hour.loc[grouped_by_hour['Month'] == 7]
    aug = grouped_by_hour.loc[grouped_by_hour['Month'] == 8]
    sep = grouped_by_hour.loc[grouped_by_hour['Month'] == 9]
    oct = grouped_by_hour.loc[grouped_by_hour['Month'] == 10]
    nov = grouped_by_hour.loc[grouped_by_hour['Month'] == 11]
    dec = grouped_by_hour.loc[grouped_by_hour['Month'] == 12]
    fig, ax = plt.subplots(1, 1, figsize=(18, 12))

    # plot lines -> change .cXX to required distance
    plt.plot(jan.Hour, jan[distance], label="January")
    plt.plot(feb.Hour, feb[distance], label="February")
    plt.plot(mar.Hour, mar[distance], label="March")
    plt.plot(apr.Hour, apr[distance], label="April")
    plt.plot(may.Hour, may[distance], label="May")
    plt.plot(jun.Hour, jun[distance], label="June")
    plt.plot(jul.Hour, jul[distance], label="July")
    plt.plot(aug.Hour, aug[distance], label="August")
    plt.plot(sep.Hour, sep[distance], label="September")
    plt.plot(oct.Hour, oct[distance], label="October")
    plt.plot(nov.Hour, nov[distance], label="November")
    plt.plot(dec.Hour, dec[distance], label="December")
    plt.legend()
    plt.title(title)
    plt.xlabel("Hour")
    plt.ylabel("Wind Speed (m/s)")
    graph = plt.show()
    plt.savefig(save_location)
    return graph

#makes a wind rose hard coded at 200 m have to hard change values
def build_wind_rose(csv):
    windrose = csv[['Year','Month', 'Day', 'Hour', 'Minute', 'wind speed at 200m (m/s)', 'wind direction at 200m (deg)']]
    windrose = windrose.rename(columns={'Year': 'Year', 'Month': 'Month', 'Day': 'Day', 'Hour': 'Hour', 'Minute': 'Minute',
                                        'wind speed at 200m (m/s)': 'windspeed200', 'wind direction at 200m (deg)': 'winddirection200'})
    windrose.index = pd.to_datetime(windrose[['Year', 'Month', 'Day', 'Hour']])
    windrose.reset_index(inplace=True)
    sns.set_style("white")
    fig = plt.figure(figsize=(7,7))
    ax = WindroseAxes.from_ax(fig=fig)
    wind_rose = ax.bar(windrose.winddirection200, windrose.windspeed200, normed=True, opening=1, edgecolor='white')
    ax.set_legend()
    return wind_rose


def make_wind_speed_graph_by_season(input_csv: str, save_location: str, title: str, distance: str):
    csv = pd.read_csv(input_csv)
    wind_speed = csv[['Year', 'Month', 'Day', 'Hour', 'Minute', 'wind speed at 10m (m/s)', 'wind speed at 40m (m/s)',
                      'wind speed at 60m (m/s)', 'wind speed at 80m (m/s)', 'wind speed at 100m (m/s)',
                      'wind speed at 120m (m/s)', 'wind speed at 140m (m/s)', 'wind speed at 160m (m/s)',
                      'wind speed at 200m (m/s)']].copy()
    wind_speed.rename(columns={'Year': 'Year', 'Month': 'Month', 'Day': 'Day', 'Hour': 'Hour', 'Minute': 'Minute',
                               'wind speed at 10m (m/s)': 'c10', 'wind speed at 40m (m/s)': 'c40',
                               'wind speed at 60m (m/s)': 'c60', 'wind speed at 80m (m/s)': 'c80',
                               'wind speed at 100m (m/s)': 'c100', 'wind speed at 120m (m/s)': 'c120',
                               'wind speed at 140m (m/s)': 'c140', 'wind speed at 160m (m/s)': 'c160',
                               'wind speed at 200m (m/s)': 'c200'}, inplace=True)
    wind_speed['Date-Time'] = pd.to_datetime(wind_speed[['Year', 'Month', 'Day', 'Hour']])
    grouped_by_hour = wind_speed.groupby(['Month', 'Hour']).mean()
    grouped_by_hour.reset_index(inplace=True)

    Spring = grouped_by_hour[grouped_by_hour['Month'].isin([2, 3, 4])]
    groupSpring = Spring.groupby(['Hour']).mean()
    groupSpring.reset_index(inplace=True)

    Summer = grouped_by_hour[grouped_by_hour['Month'].isin([5, 6, 7])]
    groupSummer = Summer.groupby(['Hour']).mean()
    groupSummer.reset_index(inplace=True)

    Fall = grouped_by_hour[grouped_by_hour['Month'].isin([8, 9, 10])]
    groupFall = Fall.groupby(['Hour']).mean()
    groupFall.reset_index(inplace=True)

    Winter = grouped_by_hour[grouped_by_hour['Month'].isin([11, 12, 1])]
    groupWinter = Winter.groupby(['Hour']).mean()
    groupWinter.reset_index(inplace=True)

    fig, ax = plt.subplots(1, 1, figsize=(20, 20))
    # plot lines
    plt.plot(groupSummer.Hour, groupSummer[distance], label="Summer")
    plt.plot(groupFall.Hour, groupFall[distance], label="Fall")
    plt.plot(groupWinter.Hour, groupWinter[distance], label="Winter")
    plt.plot(groupSpring.Hour, groupSpring[distance], label="Spring")

    plt.legend()

    plt.title(title)
    plt.xlabel("Hour")
    plt.ylabel("Wind Speed (m/s)")
    graph = plt.show()
    plt.savefig(save_location)
    return graph


def windspeed_year(csv_location:str, distance:str, title:str):
    csv = pd.read_csv(csv_location)
    wind_speed = csv[['Year','Month', 'Day', 'Hour', 'Minute','wind speed at 10m (m/s)','wind speed at 40m (m/s)','wind speed at 60m (m/s)',
                      'wind speed at 80m (m/s)','wind speed at 100m (m/s)','wind speed at 120m (m/s)', 'wind speed at 140m (m/s)', 'wind speed at 160m (m/s)',
                      'wind speed at 200m (m/s)']].copy()
    wind_speed = wind_speed.rename(columns = {'Year': 'Year','Month': 'Month', 'Day':'Day', 'Hour':'Hour', 'Minute':'Minute',
                                              'wind speed at 10m (m/s)': 'c10','wind speed at 40m (m/s)': 'c40','wind speed at 60m (m/s)':'c60',
                                              'wind speed at 80m (m/s)': 'c80','wind speed at 100m (m/s)': 'c100','wind speed at 120m (m/s)':'c120',
                                              'wind speed at 140m (m/s)':'c140', 'wind speed at 160m (m/s)':'c160', 'wind speed at 200m (m/s)':'c200'})
    wind_speed['Date-Time'] = pd.to_datetime(wind_speed[['Year', 'Month', 'Day', 'Hour']])
    wind = wind_speed[['Date-Time', distance]]
    wind.head()
    wind.set_index('Date-Time', inplace=True)
    month = wind.groupby(wind_speed.Month)[distance].mean()
    day = wind.groupby(wind_speed.Day)[distance].mean()
    hour = wind.groupby(wind_speed.Hour)[distance].mean()
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 6)
    wind[distance].plot(ax=ax,label='Raw', linestyle='None', marker='.', markersize=1, ylabel='wind speed (m/s)', xlabel='Date', title=title)
    wind[distance].resample('D').mean().plot(ax=ax,label='Daily')
    wind[distance].resample('5D').mean().plot(ax=ax,label='5 Day')
    wind[distance].resample('MS').mean().plot(ax=ax,label='Monthly',marker='d') #MS=Month Start
    plt.legend();
    fig1 = fig
    return fig1

