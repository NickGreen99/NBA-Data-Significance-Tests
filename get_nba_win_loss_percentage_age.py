import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Seasons to scrape (1980-81 through 2024-25)
seasons = list(range(1981, 2025))  # 1981 corresponds to the 1980-1981 season

# Initialize a list to store all teams
all_teams = []

# Loop over each season
for season in seasons:
    # Format the season string for the URL
    season_str = f"{season-1}-{str(season)[-2:]}"
        
    # Build the URL for the season's playoffs page
    url = f"https://www.basketball-reference.com/playoffs/NBA_{season}.html"
    print(f"Scraping playoff data for the {season_str} playoffs")

    # Request the page
    page = requests.get(url)
    time.sleep(random.randint(4,5))
    # If the request fails, go to the next
    if page.status_code != 200:
        print(f"Failed to retrieve data for the {season_str} season")
        continue
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Find the advanced team data table
    table = soup.find('table', {'id': 'advanced-team'})
    rows = table.find_all('tr')
    
    # Extract team data from the rows
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        if len(cols) > 0:
            if cols[0].text == 'League Average':
                continue
            if cols[1].text == '':
                continue
            if cols[4].text == '':
                continue
            team_name = cols[0].text
            #BASKETBALL REFERENCE WEIGHS AGE BY MINS
            age = cols[1].text
            win_loss_percentage = cols[4].text
            pace = cols[10].text
            # Append the player's data, along with the team and season info
            all_teams.append([season_str, team_name, age,win_loss_percentage, pace])
    

# Create a DataFrame from the scraped data
columns = ['Season', 'Team', 'Age', 'Win_loss_percentage', 'Pace']
df = pd.DataFrame(all_teams, columns=columns)

#Φτιάξε ένα df με το nba api, το οποίο θα έχει για στήλες [σεζόν, ομάδα, νίκες πλειόφ]
#Λογικά merge στο τέλος για να έχω [σεζόν, ομάδα, μέσος όρο ηλικίας, νίκες πλειοφ]
# Save the data to a CSV file
df.to_csv('playoff_win_loss_percentage_age_pace_1980_2024.csv', index=False)

#print("Scraping complete. Data saved to 'nba_rosters_2000_2010.csv'.")



