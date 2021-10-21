import pandas as pd
# add the height from website data to kaggle dataset
df = pd.read_csv("nba_2020_per_game_sorted.csv")
df2 = pd.read_csv("nba_stat_website.csv")

arr_of_height = []
for i in df2['Height']:
    num = i.replace('-', ".")
    converted_num = float(num)
    arr_of_height.append(converted_num)

df['Height'] = arr_of_height

df.to_csv("nba_2020_per_game_sorted_with_heighth.csv")
