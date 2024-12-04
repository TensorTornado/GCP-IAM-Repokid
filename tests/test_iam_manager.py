import google.auth
from googleapiclient.discovery import build
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class IAMManager:
    def __init__(self):
        # Initialize the IAM API client
        logging.info("Initializing IAM API client...")
        self.credentials, self.project = google.auth.default()
        self.iam_service = build('iam', 'v1', credentials=self.credentials)
        logging.info(f"Using project: {self.project}")

    def get_roles(self):
        # Get roles from the project
        roles = {}
        try:
            logging.info("Fetching roles from IAM...")
            request = self.iam_service.projects().roles().list(parent=f"projects/{self.project}")
            response = request.execute()

            # Log the full response to understand its structure
            logging.info(f"Response: {response}")

            for role in response.get('roles', []):
                # Check if the 'includedPermissions' key exists
                if 'includedPermissions' in role:
                    roles[role['name']] = role['includedPermissions']
                else:
                    logging.warning(f"Role {role['name']} does not have 'includedPermissions'.")
                    roles[role['name']] = []  # Add empty list or handle accordingly

            return roles
        except Exception as e:
            logging.error(f"Failed to fetch roles: {e}")
            raise ValueError(f"Failed to fetch roles: {e}")

    def update_role(self, role_path, permissions):
        # Update the role with new permissions using 'patch'
        try:
            logging.info(f"Fetching details for role: {role_path}")
            role = self.iam_service.projects().roles().get(name=role_path).execute()

            # Update the role's permissions
            role['includedPermissions'] = permissions

            # Use 'patch' instead of 'update' to modify the role
            logging.info(f"Updating role: {role_path} with permissions: {permissions}")
            updated_role = self.iam_service.projects().roles().patch(name=role_path, body=role).execute()

            return updated_role
        except Exception as e:
            logging.error(f"Failed to update role: {e}")
            raise ValueError(f"Failed to update role: {e}")


def main():
    logging.info("Script execution started.")

    try:
        # Initialize IAMManager
        manager = IAMManager()
        
        # Fetch roles
        logging.info("Fetching roles from IAM...")
        roles = manager.get_roles()
        logging.info(f"Roles fetched: {roles}")
        
        # Display the roles fetched from the project
        if roles:
            logging.info("Roles in the project:")
            for role_name, permissions in roles.items():
                logging.info(f"- {role_name}: {permissions}")
        else:
            logging.warning("No roles found.")
        
        # Prompt for the custom role name and permissions
        custom_role_name = input("Enter the custom role name (e.g., 'audit_team_custom_role'): ")
        custom_role_path = f"projects/{manager.project}/roles/{custom_role_name}"
        logging.info(f"Custom role path: {custom_role_path}")
        
        new_permissions_input = input("Enter the new permissions for the role, separated by commas: ")
        new_permissions = [perm.strip() for perm in new_permissions_input.split(',') if perm.strip()]
        
        if not new_permissions:
            logging.warning("No permissions entered. Skipping role update.")
        else:
            logging.info(f"Updating role {custom_role_path} with permissions: {new_permissions}")
            updated_role = manager.update_role(custom_role_path, new_permissions)
            logging.info(f"Updated Role: {updated_role}")
            print(f"Updated Role: {updated_role}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
