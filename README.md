# Fatal Police Shootings Analysis Project #
**Team members:** Brynn Hamilton, Alissa Vokes, and Saranhais Zerpa

## Project Description/Outline ##
The goal of our project is to examine fatal police shootings throughout the U.S. from 2015 to June 2020. We'll examine relationships between shootings, time, location (both City and State level), population size, and victim demographics (age, race, and gender).

### Hypothesis ###
**Null Hypothesis:** There is no correlation between population size and fatal police shootings.
**Alternative Hypothesis:** Cities/States with higher populations have more police shootings (for every 100,000)


### Additional Research Questions ###
1. Accounting for gender, race, and age, which demographic has had the most victims due to fatal police shootings?
2. Will Florida (State) be one of the top 5 States with the most recorded fatal police shootings? 
3. Which City has the most recorded fatal police shootings? 
4. Which State has the most recorded fatal police shootings?
5. Have police shootings increased in the past five years?
6. Is there a particular time of the year during which police shootings occur more frequently?


## Datasets to Be Used ##
* [Washington Post Police Shooting Data][https://github.com/washingtonpost/data-police-shootings]
    * Time period our project focused on is from 2015 to the end of June 2020.
* [Census Population Data by State and Place - Table DP05 ACS 1-Year][https://data.census.gov/cedsci/table?q=population&g=0100000US.04000.001,.160000&hidePreview=false&tid=ACSDP1Y2018.DP05&tp=true&vintage=2018]
    * To identify average city populations between 2015 and 2018

## The Exploration and Cleaning Process ##

### Insights ###

### Challenges###


## The Data Analysis Process ##

## Findings ##

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
