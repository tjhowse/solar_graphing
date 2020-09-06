#!/usr/bin/python3
# https://www.influxdata.com/blog/getting-started-python-influxdb/

from influxdb import InfluxDBClient
from cycler import cycler
import matplotlib.pyplot as plt
import numpy as np

client = InfluxDBClient(host="192.168.1.50", port=8086)
client.switch_database('telegraf')

def solar_data(client, series, days_ago):
                # SELECT "pv1_power"
                # SELECT "pv2_power"
                # SELECT "total_pv_power"
    # query = '''
    #             SELECT "total_pv_power"
    #             FROM "mqtt_consumer"
    #             WHERE ("topic" = '6hull/solar') AND
    #                 time > now() - {}d AND
    #                 time < now() - {}d
    #         '''
    query = '''
                SELECT "{}"
                FROM "mqtt_consumer"
                WHERE ("topic" = '6hull/solar') AND
                    time > '{}T06:00:00Z' - 10h AND
                    time < '{}T18:00:00Z' - 10h
            '''
    results = client.query(query.format(series, days_ago, days_ago))
    points = list(results.get_points())

    # times = [x["time"] for x in points]
    values = [x[series] for x in points]
    return values
# print(times)
# print(values)

# print x_val
plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'm']) +
                           cycler('linestyle', ['-', '-', '-', '-', '-'])))
# for i in range(5):
#     plt.plot(solar_data(client, "pv1_power", i), label=i, linewidth=1)
def plot_day(date):
    plt.plot(solar_data(client, "pv1_power", date), label=date, linewidth=1)
plot_day('2020-08-25')
plot_day('2020-08-28')
plt.xlabel("Time")
plt.ylabel("Total solar power (W)")
plt.legend()
plt.show()

    # print(results.raw)