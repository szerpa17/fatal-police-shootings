# Dependancies
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from scipy.stats import sem
import numpy as np
import os

# File load
file1 = os.path.join('csv_exports', 'Shootings.csv' )
file2 = os.path.join('csv_exports', 'Census.csv' )
file3 = os.path.join('csv_exports', 'Combined.csv' )

# File read
shootings_df = pd.read_csv(file1)
census_df = pd.read_csv(file2)
combined_df = pd.read_csv(file3)


# Victim age analysis, excluding 'unknown' output in the age column
age_df = shootings_df[shootings_df['age'].str.match('^Unknown') == False]

# Age is an object due to the way unknown values are listed
# Updated age column
age_df[['age']] = age_df [['age']].astype('float')
age_df


# Identified min and max age
min_age = age_df['age'].min()
max_age = age_df['age'].max()
print(f'Minimum age: {min_age} \nMaximum age: {max_age}')


# Age Visualization
bins = [0, 9, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 89, 100]

plt.hist(age_df['age'], bins=bins)
plt.title('Fatal Shootings by Victim Age')
plt.xlabel('Age Group')
plt.ylabel('Victim Count')

# Export plot image
plt.savefig('images/Age Distribution Histogram.png')
plt.show()


shootings_df


# Split year information from date column into two new columns
yearly_shootings = shootings_df
yearly_shootings[['year', 'month', 'day']] = yearly_shootings['date'].str.split('-', 2, expand=True)
yearly_shootings


shootings_per_year_df  = pd.DataFrame(yearly_shootings.groupby('year')['id'].count())
shootings_per_year_df = shootings_per_year_df.reset_index()
shootings_per_year_df


# Plot
plt.plot(shootings_per_year_df['year'], shootings_per_year_df['id'] )
plt.title('Fatal Police Shootings Per Year')
plt.xlabel('Year')
plt.ylabel('Count of Shootings')
plt.ylim(0,1200)

# Export plot image
plt.savefig('images/Shootings per Year.png')
plt.show()


monthly_shootings_df = pd.DataFrame(yearly_shootings.groupby('month')['id'].count())
monthly_shootings_df
monthly_shootings_df = monthly_shootings_df.reset_index()
monthly_shootings_df


# Plot
plt.plot(monthly_shootings_df['month'], monthly_shootings_df['id'])
plt.title('Fatal Police Shootings by Month \n(4 Year Period)')
plt.xlabel('Month')
plt.ylabel('Count of Shootings')

# Export plot image
plt.savefig('images/Shootings by Month.png')
plt.show()


# Shootings by State over the span of 4 years
# Census data manipulation 
# to estimate the average state population by summing 4 year city population averages within each state
state_info_df = census_df[['state','Average']]
state_avg_pop_df = state_info_df.groupby('state')['Average'].sum()
state_avg_pop_df = state_avg_pop_df.reset_index()
state_avg_pop_df = state_avg_pop_df.rename(columns={'Average': 'average population'})

# Shooting Totals by State
shooting_state_info = shootings_df[['state', 'id']]
shooting_state_df = shooting_state_info.groupby('state')[['id']].count()
shooting_state_df = shooting_state_df.reset_index()
shooting_state_df = shooting_state_df.rename(columns={'id': 'shooting occurences'})

#Table Merge
state_pop_shooting_comparison = pd.merge(state_avg_pop_df, 
                                         shooting_state_df,
                                         how='left',
                                         on='state')

four_year_state_pop_shooting_comparison = state_pop_shooting_comparison.dropna()
four_year_state_pop_shooting_comparison['shootings per 100,000'] = (
                                four_year_state_pop_shooting_comparison['shooting occurences']/
                                four_year_state_pop_shooting_comparison['average population']) * 100000

four_year_state_pop_shooting_comparison


# Data Shape
four_year_state_df = four_year_state_pop_shooting_comparison.agg(['mean', 'median', 'var', 'std', 'sem'])

four_year_state_df = four_year_state_df.rename(columns={'mean': 'Mean',
                                                        'median': 'Median',
                                                        'var': 'Variance',
                                                        'std': 'Standard Deviation',
                                                        'sem': 'SEM'})
four_year_state_df


# Max and Min States - Per Capita shootings per 100,000
four_year_state_pop_shooting_comparison.loc[((four_year_state_pop_shooting_comparison['average population'] 
                                             == 
                                             four_year_state_pop_shooting_comparison['average population'].max())
                                             |
                                            (four_year_state_pop_shooting_comparison['average population'] 
                                             == 
                                            four_year_state_pop_shooting_comparison['average population'].min()))]


four_year_state_pop_shooting_comparison.loc[((four_year_state_pop_shooting_comparison['shootings per 100,000'] 
                                             == 
                                             four_year_state_pop_shooting_comparison['shootings per 100,000'].max())
                                             |
                                            (four_year_state_pop_shooting_comparison['shootings per 100,000'] 
                                             == 
                                            four_year_state_pop_shooting_comparison['shootings per 100,000'].min()))]


# Plot
plt.figure(figsize=(10,5))
plt.scatter(four_year_state_pop_shooting_comparison['shootings per 100,000'],
            four_year_state_pop_shooting_comparison['average population'])

plt.title('Fatal Shootings per 100,000 in a Four Year Period vs State Population \n(2017-2018)')
plt.xlabel('Shootings Per 100,000')
plt.ylabel('Average State Population')
# Export plot image
plt.savefig('images/High Level_State Population Vs. Per Capita Shooting Fatalities.png')
plt.tight_layout()
plt.show()


x = four_year_state_pop_shooting_comparison['shootings per 100,000']
y = four_year_state_pop_shooting_comparison['average population']

# Regression
x_values = x
y_values = y

# Regression Calculation
(slope, intercept, rvalue, pvalue, stderr) = st.linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

plt.figure(figsize=(10,5))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
annotation = plt.annotate(line_eq,(1,20000000),fontsize=15,color="red")
plt.title('Regression Analysis of Fatal Shootings per 100,000 in a Four Year Period vs State Population \n(2017-2018)')
plt.xlabel('Shootings Per 100,000')
plt.ylabel('Average State Population')
print(f"The r-squared is: {rvalue**2}")
plt.tight_layout()
# Export plot image
plt.savefig('images/High Level Regression_State Population Vs. Per Capita Shooting Fatalities.png')
plt.show()


# Multiplot for a more detailed view of the data
#Sets plot into a 2x2 grid
fig, axs = plt.subplots(2,2, figsize=(10,10))

# Plot 1
axs[0, 0].scatter(x, y)
axs[0, 0].set_title('Fatal Shootings per 100,000 vs \nAverage State Population \nPopulation Range 400000-500000')
axs[0, 0].plot(x_values,regress_values,"r-")
axs[0, 0].set_ylim(2000000, 26000000)

# Plot 2
axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Fatal Shootings per 100,000 vs \nAverage State Population \nPopulation Range 200000-300000')
axs[0, 1].plot(x_values,regress_values,"r-")
axs[0, 1].set_ylim(1000000, 2000000)

# Plot 3 
axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Fatal Shootings per 100,000 vs \nAverage State Population \nPopulation Range 100000-200000')
axs[1, 0].plot(x_values,regress_values,"r-")
axs[1, 0].set_ylim(500000, 1000000)

# Plot 4 
axs[1, 1].scatter(x, y)
axs[1, 1].plot(x_values,regress_values,"r-")
axs[1, 1].set_title('Fatal Shootings per 100,000 vs \nAverage State Population \nPopulation Range 60000-100000')
axs[1, 1].set_ylim(0,500000)

# Assign Labels
for ax in axs.flat:
    ax.set(xlabel='Shootings Per 100,000', ylabel='Average State Population')


# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.tight_layout()
plt.savefig('images/State Population Vs. Per Capita Shooting Fatalities.png')
plt.show()


# DF View
combined_df.head()


# Identify the count of lethal shootings in each unique city and state
# combination through the use of groupby
cities_state_grp = combined_df.groupby(['state', 'city'])
counts = cities_state_grp['id'].count()

# Convert to DF
counts_by_city_df = pd.DataFrame({'shooting occurences' : counts})

# Reset index
counts_by_city_df = counts_by_city_df.reset_index()

# Merge DF with average population information
per_capita_df = pd.merge(counts_by_city_df, 
                         combined_df[['city', 'state', 'Average']], 
                         on=('city', 'state'), 
                         how='left')

# Calculate per capita shootings
per_capita_df['shootings per 100,000'] = (per_capita_df['shooting occurences']/
                                     per_capita_df['Average'])*100000

# Restructuring of columns
per_capita_df = per_capita_df[['state', 'city', 'shooting occurences', 'Average', 'shootings per 100,000']]

# Column title format
per_capita_df = per_capita_df.rename(columns={'Average': 'average population'})

# Drop duplicates
per_capita_df = per_capita_df.drop_duplicates()

per_capita_df


# Data Shape
pop_distrb = per_capita_df.agg(['mean', 'median', 'var', 'std', 'sem'])
pop_distrb
pop_distrb_df = pop_distrb.rename(columns={'mean': 'Mean',
                                          'median': 'Median',
                                          'var': 'Variance',
                                          'std': 'Standard Deviation',
                                          'sem': 'SEM'})
pop_distrb_df


plt.figure(figsize=(10,5))
plt.scatter(per_capita_df['shootings per 100,000'], 
            per_capita_df['average population'])

plt.title('Fatal Shootings per 100,000 vs \nAverage City Population')
plt.xlabel('Shootings Per 100,000')
plt.ylabel('Average City Population')
plt.tight_layout()
plt.title('Analysis of Fatal Shootings per 100,000 in a Four Year Period vs City Population \n(2017-2018)')
# Export
plt.savefig('images/High Level_City Population Vs. Per Capita Shooting Fatalities.png')
plt.show()


x = per_capita_df['shootings per 100,000']
y = per_capita_df['average population']


x_values = x
y_values = y

# Regression Calculation
(slope, intercept, rvalue, pvalue, stderr) = st.linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

plt.figure(figsize=(10,5))
plt.scatter(x_values,y_values)
plt.plot(x_values,regress_values,"r-")
annotation = plt.annotate(line_eq,(2,10000000),fontsize=15,color="red")
plt.xlabel('Shootings Per 100,000')
plt.ylabel('Average City Population')
plt.title('Regressiong Analysis of Fatal Shootings per 100,000 in a Four Year Period vs City Population \n(2017-2018)')
plt.tight_layout()
print(f"The r-squared is: {rvalue**2}")

# Export
plt.savefig('images/High Level Regression_City Population Vs. Per Capita Shooting Fatalities.png')
plt.show()


# Multiplot for a more detailed view of the data
#Sets plot into a 2x2 grid
fig, axs = plt.subplots(2,2, figsize=(10,10))

# Plot 1
axs[0, 0].scatter(x, y)
axs[0, 0].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 400000-500000')
axs[0, 0].plot(x_values,regress_values,"r-")
axs[0, 0].set_ylim(400000, 500000)

# Plot 2
axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 200000-300000')
axs[0, 1].plot(x_values,regress_values,"r-")
axs[0, 1].set_ylim(200000, 300000)

# Plot 3 
axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 100000-200000')
axs[1, 0].plot(x_values,regress_values,"r-")
axs[1, 0].set_ylim(100000, 200000)

# Plot 4 
axs[1, 1].scatter(x, y)
axs[1, 1].plot(x_values,regress_values,"r-")
axs[1, 1].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 60000-100000')
axs[1, 1].set_ylim(60000,100000)

# Assign Labels
for ax in axs.flat:
    ax.set(xlabel='Fatal Shootinig Count', ylabel='Average City Population')


# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.tight_layout()
# Export
plt.savefig('images/City Population Vs. Per Capita Shooting Fatalities 1.png')
plt.show()


# Multiplot
x_values = x
y_values = y

# Regression Calculation
(slope, intercept, rvalue, pvalue, stderr) = st.linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

#Sets plot into a 2x2 grid
fig, axs = plt.subplots(2,2, figsize=(10,10))

# Plot 1
axs[0, 0].scatter(x, y)
axs[0, 0].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 1000000-5000000')
axs[0, 0].plot(x_values,regress_values,"r-")
# axs[1, 1].set_ylim(12,16)
axs[0, 0].set_ylim(1000000, 5000000)

# Plot 2
axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 3000000-5000000')
axs[0, 1].plot(x_values,regress_values,"r-")
# axs[0, 1].set_ylim(8,12)
axs[0, 1].set_ylim(3000000,5000000)

# Plot 3 
axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 2000000-3000000')
axs[1, 0].plot(x_values,regress_values,"r-")
# axs[0, 1].set_ylim(4,8)
axs[1, 0].set_ylim(2000000, 3000000)

# Plot 4 
axs[1, 1].scatter(x, y)
axs[1, 1].plot(x_values,regress_values,"r-")
#axs[1, 1].annotate(line_eq,(2,20),fontsize=15,color="red")
axs[1, 1].set_title('Fatal Shootings per 100,000 vs \nAverage City Population \nPopulation Range 1000000-2000000')
#axs[1, 1].set_ylim(50000,100000)
#axs[1, 1].set_markersize=5000
# Print out the r-squared value along with the plot.
axs[1, 1].set_ylim(1000000,2000000)

for ax in axs.flat:
    ax.set(xlabel='Fatal Shootinig Count', ylabel='Average City Population')
    #ax.plot(**marker_style)

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.tight_layout()
# Export
plt.savefig('images/City Population Vs. Per Capita Shooting Fatalities 2.png')
plt.show()



