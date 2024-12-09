
# AWS S3
import boto3

def upload_to_s3(bucket_name, file_path, object_name=None):
    """Upload a file to S3."""
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_name or file_path)

# Azure Blob Storage
from azure.storage.blob import BlobServiceClient

def upload_to_blob(connection_string, container_name, file_path, blob_name):
    """Upload a file to Azure Blob Storage."""
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

# Google Cloud Storage
from google.cloud import storage

def upload_to_gcs(bucket_name, file_path, destination_blob_name):
    """Upload a file to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
            