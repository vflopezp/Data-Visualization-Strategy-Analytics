import pandas as pd
# delete the duplicate player and find the mean for each of them instead

df = pd.read_csv("nba_2020_per_game.csv")

#
df = df.groupby(['Player'], as_index=False).agg(
    {'Age': 'mean', 'Tm': 'first', 'Pos': 'first', 'G': 'mean', 'GS': 'mean', "MP": "mean", "FG": "mean", "FGA": "mean", "FG%": "mean", "3P": "mean", "3PA": "mean", "3P%": "mean", "2P": "mean", "2PA": "mean",	"2P%": "mean",	"eFG%": "mean", 	"FT": "mean",	"FTA": "mean",	"FT%": "mean",	"ORB": "mean",	"DRB": "mean",	"TRB": "mean",	"AST": "mean",	"STL": "mean",	"BLK": "mean",	"TOV": "mean",	"PF": "mean",	"PTS": "mean"})

df.to_csv("nba_2020_per_game_sorted.csv")
print(df['Player'].nunique())
