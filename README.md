## Google Cloud Storage Helper Scripts

This README describes two Python scripts for interacting with Google Cloud Storage (GCS).

**1. download_blob.py**

This script downloads a file from a GCS bucket.

* **Requirements:**
    * `google-cloud-storage` library ([https://cloud.google.com/apis/docs/cloud-client-libraries](https://cloud.google.com/apis/docs/cloud-client-libraries))

* **Instructions:**
    1. Update the `credentials_path` variable with the path to your Google Cloud credentials file.
        * You can find your credentials file in the location specified in the code, or you can download a new one from the Google Cloud Console: [https://console.cloud.google.com/](https://console.cloud.google.com/).
    2. Update the following variables with your desired values:
        * `bucket_name`: The name of the GCS bucket you want to download from.
        * `source_blob_name`: The name of the file you want to download within the bucket.
        * `destination_file_name`: The path and filename where you want to save the downloaded file on your local machine.
    3. Run the script. It will download the file and print a confirmation message.

**2. retrieve_buckets.py**

This script lists all the buckets in your GCP project using implicit authentication with Application Default Credentials (ADC).

* **Requirements:**
    * `google-cloud-storage` library ([https://cloud.google.com/apis/docs/cloud-client-libraries](https://cloud.google.com/apis/docs/cloud-client-libraries))

* **Instructions:**
    1. Update the `credentials_path` variable with the path to your Google Cloud credentials file (same as download_blob.py).
    * Ensure the service account associated with the credentials file has the "storage.buckets.list" permission.
    2. Optionally, update the `project_id` variable with your GCP project ID.
    3. Run the script. It will print a list of all buckets in your project.

**Important Notes:**

* Both scripts assume the credentials file is located on your local machine. For production environments, consider using a more secure authentication method.
* Make sure you have the required permissions to access the GCS bucket and its contents.


## BigQuery Script for Client usage

This script utilizes the Google Cloud BigQuery API to analyze customer purchase history data.

* **Functionality:**
    * Calculates the total number of purchases and total amount spent for a specific customer ID.

* **Requirements:**
    * `google-cloud-bigquery` library ([https://cloud.google.com/apis/docs/cloud-client-libraries](https://cloud.google.com/apis/docs/cloud-client-libraries))
    * A Google Cloud project with BigQuery enabled

* **Instructions:**
    1. Update the `credentials_path` variable with the path to your Google Cloud credentials file.
        * You can find your credentials file in the location specified in the code, or you can download a new one from the Google Cloud Console: [https://console.cloud.google.com/](https://console.cloud.google.com/).
    2. Update the following variables with your specific details:
        * Replace `training-gcp-309207` with your GCP project ID.
        * Replace `customer.PurchaseHistory` with the actual dataset and table name containing your customer purchase history data.
        * Update the value of `CustomerID` in the query to analyze data for a different customer.
    3. Run the script. It will print the customer ID, total number of purchases, and total amount spent.

**Important Notes:**

* This script demonstrates a basic query. You can modify the query to perform more complex analysis based on your data schema.
* Ensure you have the necessary permissions to access the BigQuery project and dataset.
