#!/usr/bin/python3
# https://www.influxdata.com/blog/getting-started-python-influxdb/

from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import numpy as np

client = InfluxDBClient(host="192.168.1.50", port=8086)
client.switch_database('telegraf')

def solar_data(client, days_ago):
                # SELECT "pv1_power"
                # SELECT "pv2_power"
                # SELECT "total_pv_power"
    query = '''
                SELECT "total_pv_power"
                FROM "mqtt_consumer"
                WHERE ("topic" = '6hull/solar') AND
                    time > now() - {}d AND
                    time < now() - {}d
            '''
    # query = '''
    #             SELECT "total_pv_power"
    #             FROM "mqtt_consumer"
    #             WHERE ("topic" = '6hull/solar') AND
    #                 time > 2020-08-24T05:00 + {}d AND
    #                 time < 2020-08-24T19:00 + {}d
    #         '''
    results = client.query(query.format(days_ago,days_ago-1))
    points = list(results.get_points())

    # times = [x["time"] for x in points]
    values = [x["total_pv_power"] for x in points]
    return values
# print(times)
# print(values)

# print x_val
plt.plot(solar_data(client,1), label='Today', linewidth=1, c="purple")
plt.plot(solar_data(client,2), label='Yesterday', linewidth=1, c="red")
plt.plot(solar_data(client,3), label='Day before yesterday', linewidth=1, c="blue")
# plt.plot(times, values)
# plt.plot_date(times, values, xdate=True, ydate=False)
plt.xlabel("Time")
plt.ylabel("Total solar power (kW)")
plt.legend()
plt.show()

    # print(results.raw)