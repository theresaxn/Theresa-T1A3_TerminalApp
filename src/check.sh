#!/bin/bash

# Check if python 3 is installed 
if command -v python3 >/dev/null 2>&1; then
echo Python 3 is installed. Please ensure version below is higher than 3.10.

python3 --version

else
echo Python 3 is not installed. Please install Python 3.10 or above and try again.

fi

# Run run.sh script
chmod +x run.sh
./run.sh