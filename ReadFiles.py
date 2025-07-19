import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def read_csv_files(paths):
    data_frames = {}
    for path in paths:
        file_name = path.split('/')[-1].replace('.csv', '')  # Get the file name without the ".csv" extension
        data_frames[file_name] = pd.read_csv(path)  # Store the DataFrame in the dictionary
    return data_frames

files_path = [
    './Data/circuits.csv', './Data/constructor_results.csv', './Data/constructor_standings.csv',
    './Data/constructors.csv', './Data/driver_standings.csv', './Data/drivers.csv',
    './Data/lap_times.csv', './Data/pit_stops.csv', './Data/qualifying.csv',
    './Data/races.csv', './Data/results.csv', './Data/seasons.csv', './Data/sprint_results.csv'
]

data_frames = read_csv_files(files_path)
data_frames['drivers'].head(50)
print(data_frames['drivers'].isnull().sum())
df_races = data_frames['races']
df_results = data_frames['results']
