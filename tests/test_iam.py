import sys
import os
import logging

# Add the src/utils directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Now import IAMManager from utils.iam_manager
from utils.iam_manager import IAMManager

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Ensure GCP_PROJECT_ID is set in the environment
    project_id = os.getenv("GCP_PROJECT_ID")
    if not project_id:
        raise ValueError("Environment variable GCP_PROJECT_ID is not set.")

    print("Initializing IAMManager...")
    logging.info("Initializing IAMManager...")
    # Initialize the IAMManager
    manager = IAMManager()

    # Test the get_roles method
    try:
        print("Fetching roles...")
        logging.info("Fetching roles...")
        roles = manager.get_roles()
        logging.info(f"Roles fetched: {roles}")
        print(f"Roles fetched: {roles}")

        print("Roles in the project:")
        for role_name, permissions in roles.items():
            print(f"- {role_name}: {permissions}")

        # Prompt user for custom role name and permissions to update
        custom_role_name = input("Enter the full custom role name (e.g., 'projects/<project-id>/roles/<role-name>'): ")
        new_permissions_input = input(
            "Enter the new permissions for the role, separated by commas (e.g., 'storage.buckets.list,storage.objects.get'): "
        )

        # Split the input into a list, ensuring it's not empty
        new_permissions = [perm.strip() for perm in new_permissions_input.split(',') if perm.strip()]

        # Check if permissions are provided
        if not new_permissions:
            print("No permissions entered. Skipping role update.")
        else:
            logging.info(f"Updating role: {custom_role_name} with permissions: {new_permissions}")
            updated_role = manager.update_role(custom_role_name, new_permissions)
            logging.info(f"Updated Role: {updated_role}")
            print(f"Updated Role: {updated_role}")

    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")
