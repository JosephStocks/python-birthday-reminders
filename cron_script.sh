#!/bin/bash

export PATH="$PATH:$HOME/.local/bin"

# Get the path to the current script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Set log file paths
STDOUT_LOG="$SCRIPT_DIR/output.log"
STDERR_LOG="$SCRIPT_DIR/error.log"

# Run the Python script and redirect output and errors to log files
cd $SCRIPT_DIR && poetry run python main.py > "$STDOUT_LOG" 2> "$STDERR_LOG"


