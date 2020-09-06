#!/usr/bin/python3

from influxdb import InfluxDBClient

client = InfluxDBClient(host="192.168.1.50", port=8086)
print(client.get_list_database())
client.switch_database('telegraf')

query = '''
            SELECT "value"
            FROM "mqtt_consumer"
            WHERE ("topic" = '6hull/power_price/import/5m_bid_sigma')
            ORDER BY time DESC
            LIMIT 1
        '''
# print(query)
results = client.query(query)
print(results.raw)