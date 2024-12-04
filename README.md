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

   # Setup

   ## Step 1: Set Up AWS Credentials
   Ensure that your AWS credentials are configured. You can set up your credentials using the AWS CLI or by directly    
   configuring the ~/.aws/credentials file. You can also use environment variables to set the AWS credentials.

   Run the following command to configure the AWS CLI:

   ```bash
   aws configure
   ```

   Alternatively, you can set your AWS credentials using environment variables:

   ```bash
   export AWS_ACCESS_KEY_ID="your-access-key-id"
   export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
   export AWS_DEFAULT_REGION="your-region"
   ```

   ## Step 2: Modify the Flask Application (Optional)
   The default Flask application listens on 0.0.0.0 (all interfaces) and port 8080. You can change these settings if needed     by modifying the app.run() parameters in the script.

   ```python
   app.run(host='0.0.0.0', port=8080)
   ```

   ## Step 3: Run the Application
   Once the dependencies are installed, you can run the Flask application using the following command:

   ```bash
   python app.py
   ```

   This will start a local Flask web server, and the API will be available at http://localhost:8080.

   # API Usage
   ## Endpoint: POST /

   This endpoint accepts a JSON payload with the following parameters:

   1. roleName: The name of the IAM role (string).
   2. boundaryPolicyArn: The ARN of the IAM policy to be used as the permissions boundary (string). 
   3. action: The action to perform (add to add the permissions boundary or remove to remove it).
   
   Example Payload for Adding a Permissions Boundary

   ```json
   {
   "roleName": "ExampleRole",
   "boundaryPolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess",
   "action": "add"
   }
   ```

   


    




