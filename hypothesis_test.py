import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Get data
data = pd.read_csv('playoff_win_loss_percentage_age_pace_1980_2024.csv')

# Set as age threshold the average age of playoff teams over the years
age_threshold = np.mean(data['Age'])

# Split data into young teams and old teams
young_teams = data.loc[data['Age'] < age_threshold]
old_teams = data.loc[data['Age'] >= age_threshold]

# Split years into two periods [start_season-till_season) and [till_season - now]
start_season = '1980-81'
till_season = '2004-05'

# Young Teams
young_teams_then = young_teams.loc[(young_teams['Season'] >= f'{start_season}')
                                   &
                                   (young_teams['Season'] <  f'{till_season}')]

young_teams_now = young_teams.loc[young_teams['Season'] >=  f'{till_season}']

# Get young teams pace stats and win-loss percentage stats
young_teams_now_pace = young_teams_now['Pace'].values
young_teams_then_pace = young_teams_then['Pace'].values

young_teams_now_success = young_teams_now['Win_loss_percentage'].values
young_teams_then_success = young_teams_then['Win_loss_percentage'].values

# Old Teams
old_teams_then = old_teams.loc[(old_teams['Season'] >= f'{start_season}')
                                   &
                                   (old_teams['Season'] <  f'{till_season}')]

old_teams_now = old_teams.loc[old_teams['Season'] >=  f'{till_season}']

# Get old teams pace stats and win-loss percentage stats
old_teams_now_pace = old_teams_now['Pace'].values
old_teams_then_pace = old_teams_then['Pace'].values

old_teams_now_success = old_teams_now['Win_loss_percentage'].values
old_teams_then_success = old_teams_then['Win_loss_percentage'].values

# Function that determines whether we reject the null hypothesis or not!
def reject_null_or_not(ind_t_test):
    pvalue = ind_t_test[1]
    if pvalue < 0.05:
        print(f'We reject the null hypothesis (p-value={pvalue})')
    else:
        print('There is not enough evidence to reject the null hypothesis')
        
# First test: Playoff success of young teams between the two periods

# Plot the stats as histograms
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first histogram
ax1.hist(young_teams_then_success, bins=30, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title('Young Teams Success 1980-2004')
ax1.set_xlabel('Win-Loss Percentage')
ax1.set_ylabel('Frequency')

# Plot the second histogram
ax2.hist(young_teams_now_success, bins=30, alpha=0.7, color='green', edgecolor='black')
ax2.set_title('Young Teams Success 2004-2024')
ax2.set_xlabel('Win-Loss Percentage')
ax2.set_ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()

t_test_1 = stats.ttest_ind(young_teams_now_success, young_teams_then_success, alternative='greater')
print('\nFirst test:\n')
print('Null Hypothesis: The playoff success of young teams now is less than or equal to the playoff success of young teams in the past.\n')
reject_null_or_not(t_test_1)

# Second test: Playoff success of young teams and old teams now

# Plot the stats as histograms
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first histogram
ax1.hist(young_teams_now_success, bins=30, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title('Young Teams Success 2004-2024')
ax1.set_xlabel('Win-Loss Percentage')
ax1.set_ylabel('Frequency')

# Plot the second histogram
ax2.hist(old_teams_now_success, bins=30, alpha=0.7, color='green', edgecolor='black')
ax2.set_title('Old Teams Success 2004-2024')
ax2.set_xlabel('Win-Loss Percentage')
ax2.set_ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()

t_test_2 = stats.ttest_ind(young_teams_now_success, old_teams_now_success, alternative='less')
print('\nSecond test:\n')
print('Null Hypothesis: The playoff success of young teams now is greater than or equal to the playoff success of old teams now.\n')
reject_null_or_not(t_test_2)

# Third test: Pace of young teams between the two periods

# Plot the stats as histograms
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first histogram
ax1.hist(young_teams_then_pace, bins=30, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title('Young Teams Pace 1980-2004')
ax1.set_xlabel('Pace')
ax1.set_ylabel('Frequency')

# Plot the second histogram
ax2.hist(young_teams_now_pace, bins=30, alpha=0.7, color='green', edgecolor='black')
ax2.set_title('Young Teams Pace 2004-2024')
ax2.set_xlabel('Pace')
ax2.set_ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()

t_test_3 = stats.ttest_ind(young_teams_now_pace, young_teams_then_pace, alternative='less')
print('\nThird test:\n')
print('Null Hypothesis: The playoff pace of young teams now is greater than or equal to the playoff pace of young teams in the past.\n')
reject_null_or_not(t_test_3)






    

