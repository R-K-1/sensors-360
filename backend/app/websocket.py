#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import datetime
import time
import random
import websockets
from .. import common


async def time(websocket, path):
    """
    Description:
        sends the latest heartbeat of every sensors
        and the list of sensors that have not sent a
        heartbeat in the last ten minutes
    
    Parameters:
        websocket (Websocket) : websocket
        path (String) :
    
    Returns:
        no data returned, sends messages instead
    """
    cursor = db_conn()
    no_heartbeat_wait_ = 0
    while True:
        time.sleep(5)
        cursor.execute("""
            SELECT DISTINC s.name, h.timestamp
            FROM
            Sensor s
            INNER JOIN
            Heartbeat h
            ON s.id = h.sensor_id
            ORDER BY h.timestamp DESC
            """)
        heartbeats = cursor.fetchall()
        late_sensors = []
        if x % 6 == 0:
            cursor.execute("""
                SELECT DISTINCT ON (s.name), h.timestamp
                FROM
                Sensor s
                INNER JOIN
                Heartbeat h
                ON s.id = h.sensor_id
                WHERE h.timestamp < (now()::time - INTERVAL '10 min')
                ORDER BY h.timestamp DESC
            """)

            late_sensors = cursor.fetchall()

        #now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(heartbeats)
        x += 1

start_server = websockets.serve(time, "127.0.0.1", 6000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()