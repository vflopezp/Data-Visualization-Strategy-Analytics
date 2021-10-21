import pandas as pd
# combine the data from all web pages datasets
# array to store our dataframes
dfs = []
# loop to iterate over them
for i in range(11):
    # read data from csv
    df = pd.read_csv(f"./data{i}.csv")
    # add the data to our array
    dfs.append(df)

# pd.concat will merge the list of our dataframes in one single dataframe
df_all_rows = pd.concat(dfs)
# we save this single dataframe to one file
df_all_rows.to_csv('nba_stat_website.csv')
