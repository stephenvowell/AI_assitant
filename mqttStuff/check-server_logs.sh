#!/bin/bash

# Variables
LOG_FILE="/var/log/apache2/access.log"  # Replace with your actual log file path
SEARCH_TERM="temperature data"

# Check if the log file exists
if [ ! -f "$LOG_FILE" ]; then
  echo "Log file not found: $LOG_FILE"
  exit 1
fi

# Tail the log file and search for the term
tail -f "$LOG_FILE" | grep --line-buffered "$SEARCH_TERM"