from azure.storage.blob import BlobServiceClient

# Defining Azure Storage Account connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=chakristorageaccount;AccountKey=X5YzPzX7yB//yYNRHiG6uu+bgGAQ4IQB1J50gFoUgXw6Rd1FaKgq5XJ9hIei31aBh+E+pajO3qX3+AStegKaaw==;EndpointSuffix=core.windows.net"

# Defining the container,file and directory names
container_name = "assign-2"
directory_name = "upload-sample"
source_file = "Data/WorldPopulation/PopulationWithPercentIncrease.csv"
upload_file = "PopulationWithPercentIncrease.csv"

#Method to upload data to ADLS, with args connection_string, container_name, directory_name, source_file and upload_file
def upload_data_toADLS(connection_string, container_name, directory_name, source_file, upload_file):
    # Creating a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Creating a new container
    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client.create_container()

    # Creating a BlobClient for uploading the file
    blob_client = container_client.get_blob_client(f"{directory_name}/{upload_file}")

    # Uploading the file to Azure Blob Storage
    with open(source_file, "rb") as data:
        blob_client.upload_blob(data, overwrite =True)

    print(f' "Successfully uploaded the file {upload_file} to Azure Blob Storage in container {container_name}"')
    print("UploadDataToADLS problem")

# Method call to perform uploading the file to the specified path
upload_data_toADLS(connection_string,container_name,directory_name, source_file, upload_file)