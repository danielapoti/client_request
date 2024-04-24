from google.cloud import storage
import os
import logging


#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting script execution")


def download_blob(bucket_name, source_blob_name, destination_file_name):
    # Update with the correct path to your credentials file
    credentials_path = "C:\\Users\\EPOTENDIG\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    """Downloads a blob from the bucket."""
    # The ID of your GCS project
    project_id = "training-gcp-309207"

    storage_client = storage.Client(project=project_id)

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    try:
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        logging.info("Table downloaded!")
        print(
            "Downloaded storage object {} from bucket {} to local file {}.".format(
                source_blob_name, bucket_name, destination_file_name
            )
        )
    except Exception as e:
        #print(f"Error downloading file: {e}")
        logging.error(f"Error downloading file: {e}")


# Run the function with your project ID
download_blob("bucket_prova_2", "company.csv", "C:\\Users\\EPOTENDIG\\Downloads\\company.csv")
