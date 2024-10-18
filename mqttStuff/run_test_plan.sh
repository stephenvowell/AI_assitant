#!/bin/bash

# Run server log check
./check_server_logs.sh &

# Run MQTT check
node mqtt_check.js