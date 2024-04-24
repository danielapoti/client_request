import logging
import os
import sys
from google.cloud import storage


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting script execution")


"""
When interacting with Google Cloud Client libraries, the library can auto-detect the
credentials to use.

**Important:**
- Ensure you have the correct path to your service account credentials file.
- Verify that the service account has "storage.buckets.list" permission.

Args:
    project_id: The project id of your Google Cloud project.
"""


# Update with the correct path to your credentials file
credentials_path = "C:\\Users\\EPOTENDIG\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


def retrieve_buckets(project_id):

    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    logging.info("Buckets retrieved successfully!")


# Run the function with your project ID
retrieve_buckets(project_id="training-gcp-309207")
