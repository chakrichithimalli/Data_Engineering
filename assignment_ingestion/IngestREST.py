import requests
import configparser as config
import csv

# Method to read the data from EIA dataset
def download_data_to_csv(params, state_ids, csv_destination_path):
    base_url = "https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/"

    # Constructing the final URL
    url = f"{base_url}?{'&'.join([f'facets[stateId][]={state}' for state in state_ids])}"

    # Making the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        with open(csv_destination_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Header
            header = [
                "Period",
                "Sector ID",
                "Sector Name",
                "Fuel ID",
                "Fuel Name",
                "State ID",
                "State Name",
                "Value",
                "Value Units"
            ]
            csv_writer.writerow(header)

            # Iterating over the response and write each entry as a single record
            for entry in data['response']['data']:
                row = [
                    entry['period'],
                    entry['sectorId'],
                    entry['sector-name'],
                    entry['fuelId'],
                    entry['fuel-name'],
                    entry['stateId'],
                    entry['state-name'],
                    entry['value'],
                    entry['value-units']
                ]
                csv_writer.writerow(row)

        print(f'Data saved to {csv_destination_path}')
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')

# Using configparser to read the apie key from .config file
configParser = config.ConfigParser()
configParser.read('API_Key.config')

# Defining the Api key
api_key = configParser['API']['api_key']
# API Parameters for 1st problem
paramsTotalEmissionByState2019 = {
    'api_key': api_key,
    'frequency': 'annual',
    'data[0]': 'value',
    'facets[sectorId][]': 'TT',
    'facets[fuelId][]': 'TO',
    'start': '2019',
    'end': '2019',
    'offset': '0',
    'length': '5000'
}

# API Parameters for 2nd problem
paramsCo2EmissionByCoal = {
    'api_key': api_key,
    'frequency': 'annual',
    'data[0]': 'value',
    'facets[sectorId][]': 'TT',
    'facets[fuelId][]': 'CO',
    'start': '2019',
    'end': '2019',
    'offset': '0',
    'length': '5000'
}

# State codes for which the data will be extracted
state_ids = [
    'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
    'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
    'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE',
    'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
    'SC', 'SD', 'TN', 'TX', 'US', 'UT', 'VA', 'VT', 'WA', 'WI',
    'WV', 'WY'
]

api_key_FilePath = "API_Key.config"

# Destination paths to store the csv files
csv_destination_path_TotalEmissionsByState2019ByAllFuels = "Data/CO2/TotalEmissionsByState2019.csv"
csv_destination_path_TotalEmissionsByState2019ByCoal = "Data/CO2/CoalEmissionsByState2019.csv"

# Method calls to perform the data extraction
download_data_to_csv(paramsTotalEmissionByState2019, state_ids, csv_destination_path_TotalEmissionsByState2019ByAllFuels)
download_data_to_csv(paramsCo2EmissionByCoal, state_ids, csv_destination_path_TotalEmissionsByState2019ByCoal)
