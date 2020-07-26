# Dependancies
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# File load
file1 = os.path.join('data', 'fatal-police-shootings-data.csv' )
file2 = os.path.join('data', 'ACSDP1Y2015.csv' )
file3 = os.path.join('data', 'ACSDP1Y2016.csv' )
file4 = os.path.join('data', 'ACSDP1Y2017.csv' )
file5 = os.path.join('data', 'ACSDP1Y2018.csv' )

# File read
shootings_df = pd.read_csv(file1)
c_2015 = pd.read_csv(file2)
c_2016 = pd.read_csv(file3)
c_2017 = pd.read_csv(file4)
c_2018 = pd.read_csv(file5)


c_2015


# Idetified that all columns are objects
c_2015.dtypes.value_counts()


# Census Data Cleaning

# Function Setup
# Column pull and format function
def col_pf(df, year):
    # Pulled geo ID, name, and population columns
    df = df.loc[:, ['GEO_ID', 'NAME', 'DP05_0001E']]
    # Renamed columns
    df = df.rename(columns={'NAME': 'Place/State', 'DP05_0001E': f'{year} Population'}) 
    # Split the Place/State column into two new columns
    df[['city', 'state']] = df['Place/State'].str.rsplit(',', expand=True)
    # Removed rows that only have states (no 'place')
    df = df[53:]
    # Reorganized DF for Population to be at the end
    df = df[['GEO_ID', 'Place/State', 'city', 'state', f'{year} Population']]
    # Reset index and remove the prior index
    df = df.reset_index(drop=True)
    # Pulled only necessary columns
    df = df.iloc[:, [0, 2, 3, 4]]
    # Cast population column as int
    df[[f'{year} Population']] = df[[f'{year} Population']].astype('int64')
    # Used regex on the Place column to leave the place name without an 
    # additional description
    df[['city']] = df[['city']].replace(regex=[r'city$'], value='')
    df[['city']] = df[['city']].replace(regex=[r'town$'], value='')
    df[['city']] = df[['city']].replace(regex=[r'village$'], value='')
    df[['city']] = df[['city']].replace(regex=[r'CDP$'], value='')
    df[['city']] = df[['city']].replace(regex=[r'municipality$'], value='')
    df[['city']] = df[['city']].replace(regex=[r'zona urbana$'], value='')
    return df

# DF merge function
def col_merge(df, df2, df3, df4):
    merged_df = pd.merge(df, df2, on=('GEO_ID', 'city', 'state'), how='outer')
    merged_df = pd.merge(merged_df, df3, on=('GEO_ID', 'city', 'state'), how='outer')
    merged_df = pd.merge(merged_df, df4, on=('GEO_ID', 'city', 'state'), how='outer')
    return merged_df


# Applied col_pf function on Census DFs
df_2015 = col_pf(c_2015, 2015)
df_2016 = col_pf(c_2016, 2016)
df_2017 = col_pf(c_2017, 2017)
df_2018 = col_pf(c_2018, 2018)

df_2015.head(100)


# Merged the DFs
merged_df = col_merge(df_2015, df_2016, df_2017, df_2018)
merged_df


# Identified that there were trailing spaces in Census data
merged_df[['city']] = merged_df['city'].str.strip(' ')
merged_df[['state']] = merged_df['state'].str.strip(' ')
merged_df


# Count non-NA items in each column
merged_df.count()


# Drop NA cells
clean_df = merged_df
clean_df.dropna(inplace = True) 
clean_df.count()


# Type check on merged DF
clean_df.dtypes


# Identify the average population over the four year period
clean_df['Average'] = clean_df.iloc[:, [3, 4, 5, 6]].mean(axis=1)
clean_df


# Collection of individual state population averages
state_list = clean_df['state'].unique().tolist()
state_pop_data = []

for state in state_list:
    state_series = clean_df.loc[clean_df["state"] == state, 'Average']
    state_pop_data.append(state_series)


# Zoomed Multiplot View - Partially Removing Outliers
fig, axs = plt.subplots(2,2, figsize=(15,15))

# Plot 1
axs[0, 0].boxplot(state_pop_data, labels=state_list)
axs[0, 0].set_title('State Population')
axs[0, 0].set_xlim(0, 13.5)
axs[0, 0].set_ylim(0, 1000000)

# Plot 2
axs[0, 1].boxplot(state_pop_data, labels=state_list)
axs[0, 1].set_title('State Population')
axs[0, 1].set_xlim(13.5, 26.5)
axs[0, 1].set_ylim(0, 1000000)

# Plot 3 
axs[1, 0].boxplot(state_pop_data, labels=state_list)
axs[1, 0].set_title('State Population')
axs[1, 0].set_xlim(26.5, 39.5)
axs[1, 0].set_ylim(0, 1000000)

# Plot 4 
axs[1, 1].boxplot(state_pop_data, labels=state_list)
axs[1, 1].set_title('State Population')
axs[1, 1].set_xlim(39.5,50)
axs[1, 1].set_ylim(0, 1000000)


# Assign Labels
for ax in axs.flat:
    ax.set(ylabel='Average State Population')
    
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=90)
    
# Export plot image
plt.savefig('images/State Box Plot Exploration.png')
plt.show()


# Exported Census data with population averages by city
file_path = os.path.join('csv_exports', 'Census.csv')
clean_df.to_csv(file_path, index=False, header=True)


shootings_df


# U.S. State Dictionary
# Link: http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

abbrv_df= pd.DataFrame({'State Name' : states})
abbrv_df = abbrv_df.reset_index()
abbrv_df
abbrv_df = abbrv_df.rename(columns=({'index': 'state'}))
abbrv_df


# Merged state name data into shootings DF
shootings_merge = pd.merge(shootings_df, abbrv_df, on='state', how='left')
shootings_merge = shootings_merge.rename(columns={'state':'abbreviation',
                                                  'State Name': 'state'})

#Reorganized shootings DF columns
shootings_merge = shootings_merge[['id',
                                  'name',
                                  'date',
                                  'manner_of_death',
                                  'armed',
                                  'age',
                                  'gender',
                                  'race',
                                  'city',
                                  'state',
                                  'abbreviation',
                                  'signs_of_mental_illness',
                                  'threat_level',
                                  'flee',
                                  'body_camera']]
shootings_merge


shootings_merge["gender"].replace({"M": "Male", "F": "Female"}, inplace=True)
shootings_merge["race"].replace({"A": "Asian", "W": "White", "B": "Black", "O": "Other", 
                                  "H": "Hispanic", "N": "Native American"}, inplace=True)
shootings_merge


shootings_merge.count()


# Filled NA rows with 'Unknown' in shooting DF originating columns
values = {'armed':'Unknown', 'age':'Unknown', 'gender':'Unknown', 'race':'Unknown', 'flee':'Unknown'}
shootings_merge = shootings_merge.fillna(value=values)
shootings_merge.count()


# Checked shooting DF type
# Identified data is an object
shootings_merge.dtypes


# Checked dtypes
shootings_merge['date'] = pd.to_datetime(shootings_merge['date'],format='get_ipython().run_line_magic("Y-%m-%d')", " ")
shootings_merge.dtypes


shootings_merge


# Filtered out shooting data after June 30, 2020
shootings_merge = shootings_merge[shootings_merge['date'] <= '2020-06-30']


# Exported Census data with population averages by city
file_path = os.path.join('csv_exports', 'Shootings.csv')
shootings_merge.to_csv(file_path, index=False, header=True)


# Checked Census DF to ensure there are no duplicated city/state combinations
clean_df.loc[clean_df.duplicated(['city', 'state'])].count()


## Census and Shooting Data Merge


#Merge Average city population into the shootings DF
final_merge_df = pd.merge(shootings_merge,clean_df, on=('city','state'), how='left')
final_merge_df


# Identified further cleaning is needed
final_merge_df.count()


# Dropped duplicates
cleaned_shooting_census_df = final_merge_df.dropna()
cleaned_shooting_census_df.count()


cleaned_shooting_census_df


# City Average Population - Visual Outliers
average_city_populaton = cleaned_shooting_census_df
plt.boxplot(average_city_populaton['Average'])
plt.title('Combined City Population')
plt.xlabel('Cities')
plt.ylabel('Average City Population')
plt.tight_layout()
plt.savefig('images/Combined Average City Population Exploration.png')
plt.show()


# State Population - Visual Outliers
average_state_populaton = cleaned_shooting_census_df.groupby('state')[['Average']].sum()
plt.boxplot(average_state_populaton['Average'])
plt.title('Combined State Population')
plt.tight_layout()
plt.xlabel('States')
plt.ylabel('Average State Population')
plt.savefig('images/Combined Average State Population Exploration.png')
plt.show()


# Exported Census data with population averages by city
file_path = os.path.join('csv_exports', 'Combined.csv')
cleaned_shooting_census_df.to_csv(file_path, index=False, header=True)
