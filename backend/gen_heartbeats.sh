#!/bin/bash
# Until user kills program generate and submit a heartbeat for a random sensor
while [ 1 != 2 ]
do
    sleep 5
    curl -X POST "http://localhost:5000/api/v0/heartbeat?sensor_id=$((1 + $RANDOM % 10))&timestamp=$(date +%s)"
done