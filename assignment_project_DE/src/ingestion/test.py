import requests
import json
import csv
import os

# Define the API endpoint and parameters
base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_1"
params = {
    'filter': 'record_date:gte:2000-01-01',
    'page[number]': 1,
    'page[size]': 10000
}

# Making the GET request
try:
    response = requests.get(base_url, params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        list_of_records = data['data']

        # Define the local folder path to save the CSV file
        local_folder = 'data'  # Change this to your desired folder path

        # Create the local folder if it doesn't exist
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)

        # Define the local file path for the CSV
        csv_file_path = os.path.join(local_folder, 'data.csv')

        # Convert the JSON data to a CSV file and save it locally
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write the header row
            csv_writer.writerow(list_of_records[0].keys())
            # Write the data rows
            for record in list_of_records:
                csv_writer.writerow(record.values())

        print(f'Data downloaded and saved as {csv_file_path}')

    else:
        print(f'Request failed with status code: {response.status_code}')

except Exception as e:
    print(f'An error occurred: {str(e)}')
