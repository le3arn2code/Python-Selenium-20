#!/bin/bash
# Commands for Lab 10: Taking Screenshots

# Verify setup
python3 --version
pip3 --version
python3 -m pip show selenium | grep Version
google-chrome --version
chromedriver --version

# Run the script
python3 take_screenshot.py

# List screenshot files
ls -lh *.png
