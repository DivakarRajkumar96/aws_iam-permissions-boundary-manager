import boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize AWS IAM client
iam_client = boto3.client('iam')

def manage_permissions_boundary(role_name, boundary_policy_arn, action):
    if action == 'add':
        try:
            iam_client.put_role_permissions_boundary(
                RoleName=role_name,
                PermissionsBoundary=boundary_policy_arn
            )
            return f"Permissions boundary '{boundary_policy_arn}' added to role: {role_name}"
        except Exception as e:
            return f"Failed to add permissions boundary: {str(e)}"

    elif action == 'remove':
        try:
            iam_client.delete_role_permissions_boundary(
                RoleName=role_name
            )
            return f"Permissions boundary removed from role: {role_name}"
        except Exception as e:
            return f"Failed to remove permissions boundary: {str(e)}"

    else:
        return "Invalid input. Please enter 'add' or 'remove'."

@app.route('/', methods=['POST'])
def cloud_function_entry_point():
    data = request.get_json()
    
    role_name = data.get('roleName')
    boundary_policy_arn = data.get('boundaryPolicyArn')
    action = data.get('action')
    
    result = manage_permissions_boundary(role_name, boundary_policy_arn, action)
    
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
