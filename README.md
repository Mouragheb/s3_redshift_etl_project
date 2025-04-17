# S3 to Redshift ETL Project

This project is a real-world cloud-based ETL pipeline that extracts CSV sales data from AWS S3, loads it into a Redshift Serverless data warehouse, and prepares it for analytics.

## Project Summary

- **Source:** AWS S3 (CSV files)
- **Destination:** Amazon Redshift Serverless
- **Tools Used:** Python, Boto3, Psycopg2, AWS IAM, EC2, GitHub
- **Data:** Restaurant sales data including order ID, product, quantity, revenue, and timestamps

---

## Project Structure
S3_redshift_etl_project/
│
├── data/                  # Sample CSV files (optional, excluded from GitHub)
├── scripts/               # Main ETL script
│   └── s3_to_redshift_etl.py
├── .env                   # Environment variables (excluded from GitHub)
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignore config
└── README.md              # Project documentation

---

## Setup Instructions

### 1. Environment Variables

Create a `.env` file in the root directory with the following keys:

```env
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY="your_secret_key"
AWS_REGION=us-east-2
S3_BUCKET_NAME=your-bucket-name
S3_KEY=raw/your_file.csv

REDSHIFT_DB=dev
REDSHIFT_USER=your_username
REDSHIFT_PASSWORD=your_password
REDSHIFT_HOST=your-redshift-endpoint.amazonaws.com
REDSHIFT_PORT=5439
REDSHIFT_IAM_ROLE=arn:aws:iam::your_account_id:role/RedshiftS3AccessRole

Note: Never upload this file to GitHub — it is excluded by .gitignore.

2. Run the Script
python3 scripts/s3_to_redshift_etl.py

  •	Creates the Redshift table (if it doesn’t exist)
	•	Loads the CSV file from S3 into the table using COPY
	•	Confirms success in the terminal

## Skills Demonstrated

	•	AWS IAM Role and Policy Management
	•	Redshift Schema Design
	•	Secure Credential Management using .env
	•	Python SDK Integration with Boto3 and Psycopg2
	•	Realistic Production-style Deployment Pipeline

⸻

Redshift Schema Structure

This project uses a dedicated Redshift schema:
restaurant_etl.sales_data

Schema and table are created automatically by the ETL script if they don’t already exist.
EC2 Deployment Instructions

To simulate production-like cloud execution, you can run this project on an AWS EC2 instance:
	1.	Launch a new EC2 instance (Amazon Linux 2 or Ubuntu)
	2.	SSH into your instance:
  ssh -i your-key.pem ec2-user@your-public-ip
  3.	Clone the GitHub repo:
  git clone git@github.com:Your_username/project_name.git
  cd project name
  4.	Create a virtual environment:
  python3 -m venv venv
  source venv/bin/activate
  5.	Install dependencies:
  pip install -r requirements.txt
  6.	Create your .env file (copied from local machine or manually created)
  7.	Run the ETL:
  python3 scripts/project_name.py

  Automated EC2 Deployment (CI/CD)

This project also includes automated deployment from GitHub to EC2 using:
	•	deploy.sh – Bash script that sets up environment and runs the ETL
	•	.github/workflows/deploy.yaml – GitHub Actions workflow that triggers deployment when code is pushed to main

To use this:
	1.	Add your EC2 IP and SSH credentials to GitHub secrets:
	•	EC2_HOST
	•	EC2_USER
	•	EC2_KEY (your private key or use SSH Agent forwarding)
	2.	Push to main branch
	3.	GitHub Actions will connect to EC2 and run the ETL via deploy.sh

⸻

Author

Moustafa Ragheb
Houston, Texas
GitHub: @Mouragheb


