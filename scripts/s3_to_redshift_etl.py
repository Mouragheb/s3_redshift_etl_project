import boto3
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")  # you chose to use S3_BUCKET_NAME in .env
S3_KEY = os.getenv("S3_KEY")
REGION = os.getenv("AWS_REGION")

REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT")
REDSHIFT_DB = os.getenv("REDSHIFT_DB")
REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")
REDSHIFT_IAM_ROLE = os.getenv("REDSHIFT_IAM_ROLE")

# Optional: Upload CSV file to S3
def upload_to_s3(local_file, bucket, s3_key):
    s3 = boto3.client('s3',
                      region_name=REGION,
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_key)
        print(f"Uploaded {local_file} to s3://{bucket}/{s3_key}")
    except Exception as e:
        print("Error uploading to S3:", e)

# Load data from S3 into Redshift
def load_to_redshift():
    conn = None  # Avoid UnboundLocalError if connection fails
    try:
        conn = psycopg2.connect(
            host=REDSHIFT_HOST,
            port=REDSHIFT_PORT,
            dbname=REDSHIFT_DB,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD
        )
        cur = conn.cursor()
        print("Connected to Redshift")

        # Create table if not exists
        cur.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        order_id VARCHAR(50),
        customer_name VARCHAR(100),
        region VARCHAR(100),
        product VARCHAR(100),
        quantity INT,
        unit_price FLOAT,
        total_price FLOAT,
        timestamp TIMESTAMP
        );
     """) 
        print("Table is ready")

        # Optional: Clear table first
        cur.execute("DELETE FROM sales_data;")

        # Load data using COPY
        copy_command = f"""
            COPY sales_data
            FROM 's3://{S3_BUCKET}/{S3_KEY}'
            IAM_ROLE '{REDSHIFT_IAM_ROLE}'
            REGION '{REGION}'
            FORMAT AS CSV
            IGNOREHEADER 1;
        """
        cur.execute(copy_command)
        conn.commit()
        print("Data loaded into Redshift successfully")

    except Exception as e:
        print("Error loading to Redshift:", e)

    finally:
        if conn:
            cur.close()
            conn.close()
            print("Redshift connection closed")

# Optional upload (uncomment if needed)
# upload_to_s3('data/sales_data.csv', S3_BUCKET, S3_KEY)

# Load into Redshift
load_to_redshift()