import pandas as pd
import os

# directory where your csv files are stored
dir_path = '/users/khayreali/documents/github/Severe-servers/aviation research' 

# get a list of all csv files in the directory
all_files = [file for file in os.listdir(dir_path) if file.endswith('.csv')]

# create an empty list to store dataframes
dfs = []

# loop through all files and read each into a dataframe, then append the dataframe to the list
for file in all_files:
    df = pd.read_csv(os.path.join(dir_path, file))
    dfs.append(df)

# concatenate all dataframes in the list
combined_df = pd.concat(dfs, ignore_index=True)

# write the combined dataframe to a new csv file
combined_df.to_csv('output.csv', index=False)
