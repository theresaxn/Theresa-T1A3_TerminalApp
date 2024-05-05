#!/bin/bash

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment

source .venv/bin/activate

# Install external packages from requirements.txt
pip3 install -r requirements.txt

# Run expense tracker app
python3 main.py

