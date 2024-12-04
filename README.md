# IAM Permissions Boundary Manager

A Flask application that allows managing AWS IAM roles' permissions boundaries using `boto3`. The app provides an API endpoint to add or remove permissions boundaries to IAM roles.

## Prerequisites

1. **AWS IAM Role with appropriate permissions**: Your AWS credentials must have `iam:PutRolePermissionsBoundary` and `iam:DeleteRolePermissionsBoundary` permissions to add and remove IAM role permissions boundaries.

2. **AWS Credentials**: Make sure AWS credentials are configured on your machine using the `aws configure` command or via environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).

3. **Python 3.x**: This application is developed with Python 3.x.

## Setup Instructions

1. **Clone the repository:**:

   ```bash
   git clone https://github.com/DivakarRajkumar96/aws_iam-permissions-boundary-manager.git
   cd iam-permissions-boundary-manager
   ```

2. **Set up a virtual environment:**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your AWS credentials:**:

    Ensure that your AWS credentials are configured on your local environment. You can use the AWS CLI to configure your credentials:

    ```bash
    aws configure
    ```

    Alternatively, you can set environment variables for AWS access keys.

5. **Run the Flask app:**

    ```bash
    python app.py
    ```

    The Flask application will run on http://0.0.0.0:8080

    




