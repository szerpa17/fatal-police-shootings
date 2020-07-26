# Fatal Police Shootings Analysis #
**Team members:** [Brynn Hamilton](https://github.com/Brynn-Hamilton),[ Alissa Vokes](https://github.com/alissavokes), and [Saranhais Zerpa](https://github.com/szerpa17)

## Project Description/Outline ##
The goal of our project is to examine fatal police shootings throughout the U.S. from January 2015 to June 2020. We will examine relationships between shootings, time, location (both city and state level), population size, and victim demographics (age, race, and gender).

### Hypothesis ###
**Null Hypothesis:** There is no correlation between population size and fatal police shootings.
**Alternative Hypothesis:** Cities/States with higher populations have more police shootings (for every 100,000 people).


### Additional Research Questions ###
1. Accounting for gender, race, and age, which demographic has had the most victims due to fatal police shootings?
2. Will Florida (State) be one of the top 5 States with the most recorded fatal police shootings? 
3. Which City has the most recorded fatal police shootings? 
4. Which State has the most recorded fatal police shootings?
5. Have police shootings increased in the past five years?
6. Is there a particular time of the year during which police shootings occur more frequently?


## Datasets ##
* [Washington Post Police Shooting Data](https://github.com/washingtonpost/data-police-shootings)
    * The time period focus of our project is from January 2015 to the end of June 2020.
* [Census Population Data by State and Place - Table DP05 ACS 1-Year](https://data.census.gov/cedsci/table?q=population&g=0100000US.04000.001,.160000&hidePreview=false&tid=ACSDP1Y2018.DP05&tp=true&vintage=2018)
    * Four CSVs were obtained from the Census site.
    * The files were used used to identify yearly city and state populations between 2015 and 2018.
    * Due to the lack of availability of 2019 nd 2020, population averages were calculated over the selected timeframe.
    * The 1-year estimates were used for the purpose of [currency](https://www.census.gov/programs-surveys/acs/guidance/estimates.html), though this left out populations under 65,000.

## The Cleaning Process ##
* **Learning the Language of our Data**
    * Each Census file had over 300 columns and 600 rows of information
    * Time was dedicated to studying how information was presented by the Census in order to accurately transform it into insights.
* **Addressing NaN values**
    * The shootings data frame had multiple columns with Nan Values.
    * As our goal was to preserve the ID column to ensure an accurate count, we refrained from dropping NaN values and instead replaced them with the word 'Unknown'.
* **Filtering of Data**
    * Extracted shooting data that was dated after 06/30/2020.
* **Readability**
    * The gender and race columns variables were renamed for readability.  
* **The handling and standardization of multiple files prior to merging**
    * Census Data files had additional terminology associated with city names, which had to be removed with Regex in order to facilitate a future merge with the shootings data frame.
    * Trailing spaces were removed.
    * All Census files were merged into one data frame.
    * Population averages over our chosen four year period were calculated.
    * The shooting data frame was updated to standardize the state column (to facilitate the merging with the census data frames on city and state).

### Insights ###

* The usefullness of creating multiple data frames to address the shrinkage of Data.
    * Cleaned and merged Census data frame - usefull for a high level view of state population.
    * Cleaned shootings data frame - usefull for shooting specific analysis.
    * Merged shootings/Census data frame - useful for the calculation of shooting data per 100,000 people.

### Challenges ###
* Census Place terminology
    * A resource for all 'place' designations was identified within the analysis stage of the project.
    * Therefore, it is possible that cities may have been dropped due to not being matched with the appropriate Census equivalent in the Regex step of the data cleaning. 
    * Resource [link](https://www.census.gov/content/dam/Census/data/developers/understandingplace.pdf)
* **File Inconsistencies**
    * Census Data files were not consistent in their use of column ID's and column description formats in all files
* Size of Data
* Time

## Data Exploration ##
* State and city population information was visualized
    * State
        * Population by State Boxplot
            ![State Population Box Plot- Individual States]()
        * Combined State Average Boxplot
            ![Average State Population Single Box Plot - Combined States]()
    * City
        * Combined City Boxplot
            [Average City Population Single Box Plot - Combined Cities]()
        
### Insights ###
* Census Data
    * This dataset may be limiting in the findings it can provide as it excludes populations under 65,000, which may demonstrate different trends.
    * Outliers
        * Visual exploration on state and city data identified the presence of outliers. 
        * Our hypothesis is focused on population size, therefore, it was determined that outliers would be maintained for our analysis in order to gain additional insights on these populations.

### Challenges ###
* Accounting for "Unknown" values in numeric columns.
    * Though inputting these values in place of NaNs in the cleaning stage, these values made data analysis more complex when dealing with numeric columns. 
* Scope Creep
    * Due to not removing data columns that werent a part of our scope, it was difficult to avoid from scope creep.
    * The mass size of our data also contributed to scope creep as we did not pull samples from our data for analysis.
* Backtracking to validate the results of plotted charts. 
* Application of complicated visualizations.
* Time - which limited analysis and visual details on charts. 


## Data Analysis and Findings ##

## Findings ##
**Hypothesis results**

**State:** 
* No visible correlation
* Low R-squared: 0.09013598548243928
* Null hypothesis was found to be True
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)

        ![State Scatter Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level_State%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

        ![State Regression](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level%20Regression_State%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

        ![State Trends - Subplots](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/State%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)
        
        
**City:**
* Inverse correlation. implying larger cities have less police shootings per capita.
* Low R-squared: 0.09013598548243928
* Neither hypothesis could be accepted.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)

        ![City Scatter Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level_City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

        ![City Regression](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level%20Regression_City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

        ![City Trends - Subplots 1](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities%201.png?raw=true)

        ![City Trends - Subplots 2](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities%202.png?raw=true)

* Questions Answered:
1. Accounting for gender, race, and age, which demographic has had the most victims due to fatal police shootings?
    * The demographic with the most victims due to fatal police shootings are white males between the ages of 31-35.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)

2. Will Florida (State) be one of the top 5 States with the most recorded fatal police shootings? 
    * Florida is among the top 5 States (#3) with the most fatal police shootings.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
    
3. Which City has the most recorded fatal police shootings? 
    * Cities with Highest Count of Fatal Shootings:
        Los Angeles
        Phoenix
        Houston
        Las Vegas
        San Antonio
     * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
            

4. Which State has the most recorded fatal police shootings?
    * States with Highest Count of Fatal Shootings:
        California
        Texas
        Florida
        Arizona
        Colorado 
     * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
     
[Visual Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb "Visual for Questions three and four")
                
   ![Count of Fatal Shootings by State Bar Chart](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/state_bar.png?raw=true)  

5. Have police shootings increased in the past five years?
    * The overall count of police shootings a year has remained consistent.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
       
       ![Shooting Analysis by Year ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Shootings%20per%20Year.png?raw=true) 
    
6. Is there a particular time of the year during which police shootings occur more frequently?
    * Most police shootings take place in the beginning of the year.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)
        
        ![Shooting Analysis by Month ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Shootings%20by%20Month.png?raw=true) 

**Additional Analysis Conducted** 

* Victim Age Distribution
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)
    
        ![Count of Fatal Shootings by Age Group Histogram](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Age%20Distribution%20Histogram.png?raw=true)  

* Fatal Shootings by Race
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)

        ![Race Pie Chart ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/race_pie.png?raw=true) 

* Fatal Shootings by Race and Manner of Death
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)
    
        ![Race and Manner of Death Pie Chart ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/race_manner_of_death_doubledonut.png?raw=true)      

* Fatal Shootings by Race and Gender
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)
    
        ![Fatal Shootings by Race and Gender Bar Chart](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/gender_bar.png?raw=true)
  



## Opportunities ##
There are many opportunities for further exploration of this dataset in the below areas.

* Additional Data Comparisons:
    * Race Specific Population Data
    * Income Inequality
    * Police Funding in relation to fatal police shootings
    * Instances of police brutality, and non lethal shootings
    * Officer Data - shooting instances, length of service 
    * Officer staff count in city/state location
* Visualizations:
    * Maps
* Relationships between other factors in the shootings data set and shooting fatalities:
    * Fleeing designation and shootings
    * Body-cams and shootings
    * Weapons
    * Mental Illness and Risk