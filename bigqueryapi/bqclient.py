from google.cloud import bigquery
import os


# Update with the correct path to your credentials file
credentials_path = "C:\\Users\\EPOTENDIG\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


def query_result(query):
    # Construct a BigQuery client object.
    client = bigquery.Client()
    rows = client.query_and_wait(query)  # Make an API request.

    print("The query data:")
    for row in rows:
        print("name={}, count={}, total Amount={}".format(row[2], row[0], row[1]))


query = """
        SELECT count(*),sum(TotalAmount) as total, CustomerID
        FROM `training-gcp-309207.customer.PurchaseHistory`
        WHERE CustomerID = 298
        GROUP BY CustomerID
    """
query_result(query)
