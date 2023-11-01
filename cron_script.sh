#!/bin/bash

export PATH="$PATH:$HOME/.local/bin"

# Get the path to the current script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Set log file paths
COMBINED_STDOUT_ERROR_LOG="$SCRIPT_DIR/cron.log"

# Run the Python script and redirect output and errors to log files
cd $SCRIPT_DIR && poetry run python main.py > "$COMBINED_STDOUT_ERROR_LOG" 2>&1
