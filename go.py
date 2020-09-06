#!/usr/bin/python3
# https://www.influxdata.com/blog/getting-started-python-influxdb/

from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import numpy as np

client = InfluxDBClient(host="192.168.1.50", port=8086)
client.switch_database('telegraf')

query = '''
            SELECT "pv1_power"
            FROM "mqtt_consumer"
            WHERE ("topic" = '6hull/solar')
            ORDER BY time DESC
            LIMIT 100
        '''
# print(query)
results = client.query(query)
points = list(results.get_points())

times = [x["time"] for x in points]
values = [x["pv1_power"] for x in points]
print(times)
print(values)

# print x_val
plt.plot(times, values)
plt.show()

    # print(results.raw)