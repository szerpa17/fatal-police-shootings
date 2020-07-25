# Fatal Police Shootings Analysis Project #
**Team members:** Brynn Hamilton, Alissa Vokes, and Saranhais Zerpa

## Project Description/Outline ##
Our project is to examine fatal police shootings throughout the U.S.A. from 2015 to June 2020. We'll examine relationships between shootings, time, location (City, State), population size, and victim age, race, and gender.

### Hypothesis ###
trends in shootings over the years; and relationships between gender, race, age.

### Research Questions to Answer ###
Are there more instances of fatal shootings in certain areas (metropolitan vs rural)?
Are there more instances of males being fatally shot than other genders?
Is there a higher rate of fatal shootings for certain races/ethnicities?
Is there a link between police shootings and city population sizes?
Hypothesis
State Population and Shootings (for every 100,000 people)
Null: There is no correlation between population size in a city or state and lethal police shootings.
Alternative:  Cities/States with higher populations have more police shootings (for every 100,000 in the state or ever 10,000 in the city). 
Age
Null: 18+
Alternative: 20-25 years olds make up a majority of the shooting data
Shootings over time
Null: Shootings have not increased over our timeframe
Alternative: Shootings have increased
??? Metropolitan Areas and Shootings (for every 10,000 people)
Null: Metropolitan areas (areas with more than 50,000 people) do not have higher rates of police shootings.
Alternative: Metropolitan areas have higher rates of police shootings for every 10,000 people.
Victims (among police shootings)
Null: There is no common victim demographic????
Alternative: The most common victim demographic is predicted to be black males, within the range of 20-25 years old.
States
It is hypothesized that Florida will be among the top five states with the most fatal shooting deaths.

## Datasets to Be Used ##
* [Washington Post Police Shooting Data][https://github.com/washingtonpost/data-police-shootings]
    * Time period our project focused on is from 2015 to the end of June 2020.
* [Census Population Data by State and Place - Table DP05 ACS 1-Year][https://data.census.gov/cedsci/table?q=population&g=0100000US.04000.001,.160000&hidePreview=false&tid=ACSDP1Y2018.DP05&tp=true&vintage=2018]
    * To identify average city populations between 2015 and 2018

## Cleaning Process ##
### Insights ###

### Challenges###


## Analysis ##

## Results ##

Potential issue: City names in the Washington Post Data may not always consistently match the Census data given, this may be challenging to work with.
Rough Breakdown of Tasks
Done in a group setting
Clean census data - find average population by city/place
Merge into fatal shooting data (by City and State)
Set conditional to assign “rural” and “metro” categories to each place, this will be a new column in the dataframe. 
Create dataframe
Breakout into individual branches
Brynn Branch
City & State Demographics
Percentage and count of shootings by City
Percentage and count of shootings by State
Gender Demographics
Percentage and count of male shootings “M”
Percentage and count of female shootings “W”
Percentage and count of Other / Non-Disclosed (if any)
Alissa Branch
Racial Demographics - pie chart
Percentage and count of Black fatal shootings “B”
Percentage and count of White fatal shootings “W”
Percentage and count of Hispanic fatal shootings “H”
Percentage and count of Other / Non-Disclosed fatal shootings “O”
Bar chart of total shootings for race/genders
(x-axis = gender/race, y-axis=shooting instances)
Bar chart for states
Other relevant charting
Sara Branch
Shooting comparison by state population
Age Demographics
Create age bins - 5 years apart
Fatal shootings by age group
Scatter for all shooting data (shooting events)
Including regression line for full span of shootings
If Time Allows:
Exploration/presentation of ‘overall manner of death’ data.
Top Cities
Percentage and count of shootings by City
Top 5 “most dangerous” Cities based on police shootings. 
Top States
Percentage and count of shootings by State
Top 5? “most dangerous” States?
Top demographic
Most likely to be shot demographic (age, gender, and race factors)
