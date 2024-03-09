import boto3
import os

# AWS credentials
#aws_access_key_id = 'your_access_key'
#aws_secret_access_key = 'your_secret_key'
#aws_session_token = 'your_session_token'  # If using temporary credentials, otherwise set to None

# S3 bucket
bucket_name = 'amirz-bucket'
region = 's3.us-west-1'
aws_server = '.s3.us-west-1.amazonaws.com'

# Create an S3 client
s3 = boto3.client('s3')

#########  List objects in the S3 bucket  ############

objects = s3.list_objects(Bucket=bucket_name)['Contents']

# Print the list of files
print(f"List of files in the bucket: {bucket_name}")
for obj in objects:
    print(obj['Key'])
print("End of list.")

############ Download objects in s3 bucket to local directory /downloads #####################

# Local directory to download files
local_directory = 'downloads'

# Create the local directory if it doesn't exist
if not os.path.exists(local_directory):
    os.makedirs(local_directory)

# Download each file
for obj in objects:
    key = obj['Key']
    local_file_path = os.path.join(local_directory, os.path.basename(key))

    print(f"Downloading {key} to {local_file_path}")
    print(f"Downloading https://{bucket_name}{aws_server}/{key}")
    # Download the file
    s3.download_file(bucket_name, key, local_file_path)

print("Download complete!")

#######################################################

# Local directory containing files to upload
local_upload_directory = 'uploads'

# Check if the local directory 'uploads' exists and contains files
if os.path.exists(local_upload_directory) and os.path.isdir(local_upload_directory):
    files_to_upload = [f for f in os.listdir(local_upload_directory) if os.path.isfile(os.path.join(local_upload_directory, f))]

    if files_to_upload:
        # Upload each file to S3
        for file_name in files_to_upload:
            local_file_path = os.path.join(local_upload_directory, file_name)
            s3_key = file_name  # Use the same file name in S3

            print(f"Uploading {local_file_path} to S3 key: {s3_key}")
            s3.upload_file(local_file_path, bucket_name, s3_key)

        print("Upload complete!")
    else:
        print("No files found in the 'uploads' folder.")
else:
    print("The 'uploads' folder does not exist or is not a directory.")