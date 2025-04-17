#!/bin/bash

echo "Running ETL script..."

# Load environment variables from .env
export $(grep -v '^#' .env | xargs)

# Run ETL
python3 scripts/s3_to_redshift_etl.py