import kaggle
import pandas as pd

# Authentication of the user credentials
kaggle.api.authenticate()

# dataset identifier for kaggle dataset of world's population and defining required file paths
dataset_name = "iamsouravbanerjee/world-population-dataset"
csv_destination_path = "Data/WorldPopulation"
csv_file_path = "Data/WorldPopulation/world_population.csv"
output_file_path = "Data/WorldPopulation/PopulationWithPercentIncrease.csv"

# Kaggle API call to download the csv file to the csv_destination_path
kaggle.api.dataset_download_files(dataset_name, csv_destination_path, unzip=True)

# Reading the csv file using pandas library
world_population = pd.read_csv(csv_file_path)

# using the actual column names and calculating the percentage increase from year 2000 to 2022
# And adding up a new column and naming it as PercentIncrease_2000_2022
if "2000 Population" in world_population.columns and "2022 Population" in world_population.columns:
    world_population["PercentIncrease_2000_2022"] = (world_population["2022 Population"] - world_population[
        "2000 Population"]) / world_population["2000 Population"]
else:
    print("Column names not found in the csv file, please check the column names in your CSV file.")

# Performing sorting on the PercentIncrease_2000_2022 column in descending order
world_population = world_population.sort_values(by="PercentIncrease_2000_2022", ascending=False)

# Saving the data to a new csv file with name PopulationWithPercentIncrease
world_population.to_csv(output_file_path, index=False)

print("CSV file with percent increase saved successfully, IngestKaggle problem")
