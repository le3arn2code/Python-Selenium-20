#!/bin/bash
# Lab 18: File Upload Simulation - Commands

# Create lab directory
mkdir lab18-file-upload
cd lab18-file-upload

# Create test file
echo "This is a test file for upload simulation." > sample.txt

# Run the Selenium script
python3 upload_simulation.py
