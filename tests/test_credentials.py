from google.cloud.iam_credentials_v1 import IAMCredentialsClient

def test_credentials_client():
    try:
        client = IAMCredentialsClient()
        print("IAMCredentialsClient initialized successfully!")
    except Exception as e:
        print(f"Error initializing IAMCredentialsClient: {e}")

test_credentials_client()
