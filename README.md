# Data-Visualization-Strategy-Analytics

This repository contains the python scripts that been used to scrape, merge and clean the datasets used for my Data-Visualization-Strategy-Analytics course work. The main objective
of those scripts were to combine two datasets, one from kaggle (data/nba_2020_per_game.csv) with key performance metrixes for each NBA player for season 2019-2020 and 
another from NBA website with player heigths.

## Steps Taken(in order):
  1. Scrape the tables, containing the players heights from [NBA website](https://www.nba.com/stats/players/bio/?Season=2019-20&SeasonType=Regular%20Season&fbclid=IwAR1HOmAMuXkkiOiB4B1wDi9y5eVsWFmfyTMugrF1yXL7NmaB_oRYBWks8Q0&sort=PLAYER_HEIGHT_INCHES&dir=-1), it was done by script: `scrape_data_from_nba.py`. The tables were stored in `web` folder
  2. Merge all the tables, that was scraped in 1 by using `combine_scraped_data.py`, the merged table was stored in `data/nba_stat_website.csv`
  3. Filter the kaggle dataset since one player had mupltiple occurences when they switched teams mid-season. It was done in script: `filter_kaggle_data.py ` and data was stored at `data/nba_2020_per_game_sorted.csv`
  4. Finally, take a "Height" column from NBA website dataset and add it to kaggle dataset. In the process, I also changed the height from imperial measuring system to metric system. All been done by script `combine_nba_data_with_kaggle_data.py` and data saved in `data/nba_2020_per_game_sorted_with_height.csv`
