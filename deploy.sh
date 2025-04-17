#!/bin/bash

echo "Running ETL script..."

# Load environment variables safely from .env
set -o allexport
source .env
set +o allexport

# Run the ETL script
python3 scripts/s3_to_redshift_etl.py