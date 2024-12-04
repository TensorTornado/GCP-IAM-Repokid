# GCP IAM Permission Optimizer

## **Purpose**
The **GCP IAM Permission Optimizer** is a Python-based tool designed to analyze and reduce unused permissions in Google Cloud Platform (GCP) IAM roles. Inspired by Netflix's Repokid, this tool ensures adherence to least-privilege principles, reduces the security attack surface, and improves compliance with security frameworks like **SOC 2**, **ISO 27001**, and **NIST**.

---

## **Key Benefits**
1. **Reduced Blast Radius**  
   Automatically minimize unused permissions in IAM roles to lower security exposure.
   
2. **Enhanced Compliance**  
   Aligns IAM policies with least-privilege principles, reducing over-permissioned roles.

3. **Automation**  
   Eliminates manual efforts in auditing IAM roles across GCP projects.

---

## **Features**
- **Permission Analysis**  
  Tracks unused permissions using Cloud Audit Logs.

- **Policy Minimization**  
  Automatically generates optimized IAM policies.

- **IAM Role Updates**  
  Programmatically updates IAM roles with minimized permissions.

- **Custom Whitelisting**  
  Supports preservation of critical permissions through custom rules.

- **Audit Reporting**  
  Exports unused permissions as a CSV report for review and compliance.

---

## **Installation**

### **Prerequisites**
1. **Google Cloud SDK**  
   Installed and authenticated.

2. **APIs Enabled**:
   - Cloud Resource Manager API
   - Cloud Logging API
   - IAM API

3. **Service Account**  
   Create a service account with the following roles:
   - `roles/logging.viewer`
   - `roles/iam.securityReviewer`
   - `roles/bigquery.user`

---

### **Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GCP-IAM-Repokid.git
   cd GCP-IAM-Repokid

File Structure:

GCP-IAM-Repokid/
├── README.md               # Documentation
├── LICENSE                 # License
├── requirements.txt        # Dependencies
├── src/                    # Main source code
│   ├── __init__.py         # Makes the directory a Python package
│   ├── main.py             # Entry point for the tool
│   ├── utils/              # Utility modules
│       ├── __init__.py     # Makes utils a Python package
│       ├── iam_manager.py  # Handles IAM operations
│       ├── log_analyzer.py # Analyzes Cloud Audit Logs
│       ├── policy_generator.py # Generates minimized policies
├── tests/                  # Unit tests
│   ├── __init__.py         # Test package initialization
│   ├── test_iam_manager.py # Tests for IAM Manager
│   ├── test_log_analyzer.py# Tests for Log Analyzer
│   ├── test_policy_generator.py # Tests for Policy Generator
├── .gitignore              # Files to exclude from Git tracking


## Step-by-Step Integration

### **1. Prerequisites**
Ensure you have the following prerequisites installed and configured:
- **Google Cloud SDK**: [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
- **Python 3.9 or newer**: Install from [Python.org](https://www.python.org/downloads/).
- **IAM Permissions**:
  - Assign the following roles to the service account or user running the tool:
    - `roles/logging.viewer` (to read Cloud Audit Logs).
    - `roles/iam.securityReviewer` (to analyze IAM roles).
    - `roles/bigquery.user` (if you plan to export data to BigQuery).

---

### **2. Clone the Repository**
Download the project to your local machine:
```bash
git clone https://github.com/your-username/GCP-IAM-Repokid.git
cd GCP-IAM-Repokid

### **3. Install dependencies**
pip install -r requirements.txt


## **4. Configure Authentication
gcloud auth application-default login

If you’re using a service account, set the GOOGLE_APPLICATION_CREDENTIALS environment variable:

export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-service-account-key.json"

5. Analyze Unused Permissions
Run the tool to analyze unused IAM permissions in your GCP project. The tool will output a CSV file with unused permissions.

Command:

python src/main.py --project_id <your-gcp-project-id> --days <number-of-days>
python src/main.py --project_id my-gcp-project --days 90

Output:
A file named unused_permissions_report.csv containing:

#IAM Role Names
Unused Permissions

6. #Update IAM Roles
To minimize unused permissions in IAM roles, use the following command:
python src/main.py --project_id <your-gcp-project-id> --days <number-of-days> --update_roles
EG:python src/main.py --project_id my-gcp-project --days 90 --update_roles

#Result:
IAM roles will be updated with minimized permissions based on the analysis.

10. Automate with Cron or Cloud Scheduler
To run the tool periodically, you can set up automation:

Linux Cron Job:

crontab -e
Add the following line to run daily at midnight:

0 0 * * * python /path/to/src/main.py --project_id <your-gcp-project-id> --days 90
Cloud Scheduler (GCP):
Use Cloud Scheduler to trigger the tool with Cloud Functions or a VM.

Validate Results
Review the updated IAM roles in your GCP console:

Navigate to IAM & Admin > Roles.
Check if the roles reflect the minimized permissions generated by the tool.
python src/main.py --project_id <your-gcp-project-id> --restore_roles


Proprietary License Agreement

Copyright (c) 2024 MOMYFE LLC

This software and associated documentation files (the "Software") are the exclusive property of MOMYFE LLC. Permission is hereby granted to use the Software for evaluation purposes only. Redistribution, modification, or commercial use of this Software is strictly prohibited without a separate written agreement with MOMYFE LLC.

For commercial inquiries, please contact [Your Email/Website].

## Commercial Use

This software is the proprietary property of **MOMYFE LLC**. You may use it for personal or educational purposes. 

If you wish to use this software for commercial purposes or require advanced features, please contact us at **[Your Contact Email/Website]** for licensing options.
