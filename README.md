# Fatal Police Shootings Analysis #
**Team members:** [Brynn Hamilton](https://github.com/Brynn-Hamilton),[ Alissa Vokes](https://github.com/alissavokes), and [Saranhais Zerpa](https://github.com/szerpa17)

## Project Description ##
The goal of our project is to examine fatal police shootings throughout the U.S. from January 2015 to June 2020. We will examine relationships between shootings, time, location (both city and state level), population size, and victim demographics (age, race, and gender).

Our interest in this topic is due to the social movement taking place, Black Lives Matter, for which we want to explore existing data.

### Hypothesis ###
**Null Hypothesis:** There is no correlation between population size and fatal police shootings.

**Alternative Hypothesis:** Cities/States with higher populations have more police shootings (for every 100,000 people).


### Additional Research Questions ###
1. Accounting for gender, race, and age, which demographic has had the most victims due to fatal police shootings?
2. Will Florida (State) be one of the top 5 states with the most recorded fatal police shootings? 
3. Which City has the most recorded fatal police shootings? 
4. Which State has the most recorded fatal police shootings?
5. Have police shootings increased in the past five years?
6. Is there a particular time of the year during which police shootings occur more frequently?


## Datasets ##
* [Washington Post Police Shooting Data](https://github.com/washingtonpost/data-police-shootings)
* [Census Population Data by State and Place - Table DP05 ACS 1-Year](https://data.census.gov/cedsci/table?q=population&g=0100000US.04000.001,.160000&hidePreview=false&tid=ACSDP1Y2018.DP05&tp=true&vintage=2018)
    * Four CSVs were obtained from the Census site.
    * The files were used to identify yearly city and state populations between 2015 and 2018.
    * Due to the lack of availability of 2019 and 2020 population data, population averages were calculated over the selected timeframe.
    * The 1-year estimates were used for data [currency](https://www.census.gov/programs-surveys/acs/guidance/estimates.html), though this left out populations under 65,000.

## The Cleaning Process ##
* **Learning the Language of our Data**
    * Each Census file had over 300 columns and 600 rows of information
    * Time was dedicated to studying how information was presented by the Census to accurately transform it into insights.
        ![c2015 Data Frame Visual](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Data%20Frames%20and%20Code%20Snippets/c_2015%20Data%20Frame%20Snippet.png?raw=true)

* **Addressing NaN values**
    * The shooting's data frame had multiple columns with NaN Values.
    * As our goal was to preserve the ID column to ensure an accurate count, we refrained from dropping NaN values and instead replaced them with the word 'Unknown'.
* **Filtering of Data**
    * Extracted shooting data that was dated after 06/30/2020.
* **Readability**
    * The gender and race columns variables in the shooting's data frame were renamed for readability.  
* **The handling and standardization of multiple files prior to merging**
    * Census Data files had additional terminology associated with city names, which had to be removed with Regex to facilitate a future merge with the shootings data frame.
        ![Regex Code](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Data%20Frames%20and%20Code%20Snippets/Regex.png?raw=true)
        
    * Trailing spaces were removed.
    * All Census files were merged into one data frame.
    * Population averages over our chosen four year period were calculated.
        ![Merged Census Data Frame with Average Population Calculation](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Data%20Frames%20and%20Code%20Snippets/Merged%20Census%20Data%20Frame.png?raw=true)
    * The shooting data frame was updated to standardize the state column (to facilitate the merging with the census data frames on city and state).
        
        

### Insights ###

* The usefulness of creating multiple data frames to address the shrinkage of Data.
    * Cleaned and merged Census data frame, used for a high-level view of state populations.
    * Cleaned shooting's data frame, used for shooting specific analysis.
    * Merged shooting's/Census data frame, used for the calculation of shooting data per 100,000 people.

### Challenges ###
* Census 'Place' terminology
    * A resource for all 'place' designations was identified within the analysis stage of the project.
    * Therefore, cities may have been dropped due to not being matched with the appropriate Census equivalent in the Regex step of the data cleaning. 
    * [Resource link](https://www.census.gov/content/dam/Census/data/developers/understandingplace.pdf)
* **File Inconsistencies**
    * Census Data files were not consistent in their use of column ID's and column description formats in all files
* Identifying cleaning opportunities in the analysis stage.
* Size of Data
* Time

## Data Exploration ##
* State and city population information was visualized
    * State
        * Population by State Boxplot (Zoomed, not including all outliers)
            
            ![State Population Box Plot- Individual States](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/State%20Box%20Plot%20Exploration.png?raw=true)
        
        * Combined State Average Boxplot
            
            ![Average State Population Single Box Plot - Combined States](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Combined%20Average%20State%20Population%20Exploration.png?raw=true)
    * City
        * Combined City Boxplot
            
            ![Average City Population Single Box Plot - Combined Cities](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Combined%20Average%20City%20Population%20Exploration.png?raw=true)
        
### Insights ###
* Census Data
    * This dataset may be limiting in the findings it can provide as it excludes populations under 65,000, which may demonstrate different trends.
    * Outliers
        * Visual exploration of state and city data identified the presence of outliers. 
        * Our hypothesis is focused on population size, therefore, it was determined that outliers would be maintained for our analysis to gain additional insights into these populations.

### Challenges ###
* Accounting for "Unknown" values in numeric columns.
    * Though inputting these values in place of NaNs in the cleaning stage, these values made data analysis more complex when dealing with numeric columns. 
* Scope Creep
    * Due to not removing data columns that were not a part of our scope, it was difficult to avoid scope creep.
    * The mass size of our data also contributed to scope creep as we did not pull samples from our data for analysis.
* Identifying the opportunity for additional data frames to be made as a foundation for data analysis in the exploration phase (such as a Census data frame that pulls city shooting data for state per capita calculations).
* The process of backtracking to validate the results of plotted charts. 
* Plot and visualization formatting difficulties.
    * Though white males within the 31-35 age group were found to be the largest race/age victim group, visualizations did not always match this.
    * Further development could be made to refine the plots.
    ![Race, Gender, and Age Table](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Data%20Frames%20and%20Code%20Snippets/Race_Age_Gender_Table.png?raw=true)![Male Fatal Shooting Deaths by Race and Age Group](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Combined_Demographics_Male.png?raw=true)
* Time - which limited analysis and visual details on charts. 


## Data Analysis and Findings ##

**Hypothesis results**

A note on R-squared values - data based on human behavior can often have a low r-squared as it is difficult to predict and show statistical significance. ([Source](https://statisticsbyjim.com/glossary/regression-analysis/))

**State:** 
* No visible correlation
* Low R-squared: 0.09013598548243928
* The null hypothesis was found to be true.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)

    
    * Scatterplot and Regression Line 
    
        ![State Scatter Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level_State%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

        ![State Regression](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level%20Regression_State%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

    * Zoomed Scatter Plot (by Population Size)
    
        ![State Trends - Subplots](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/State%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)
     
        
**City:**
* Smaller R-squared value, but a more visible grouping of cities, visually implying larger cities have fewer police shootings per capita.
* Low R-squared: 0.0026383280666281714
* Neither hypothesis could be accepted.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)

    * Scatterplot and Regression Line 
        
        ![City Scatter Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level_City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)
    
        ![City Regression](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/High%20Level%20Regression_City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities.png?raw=true)

    * Zoomed Scatter Plot (by Population Size)
        
        ![City Trends - Subplots 1](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities%202.png?raw=true)
        
        ![City Trends - Subplots 2](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/City%20Population%20Vs.%20Per%20Capita%20Shooting%20Fatalities%201.png?raw=true)

* Questions Answered:
1. Accounting for gender, race, and age, which demographic has had the most victims due to fatal police shootings?
    * The demographic with the most victims due to fatal police shootings are white males between the ages of 31-35.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
        
        ![Race vs Age Group Bar Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Race_Age_Bar.png?raw=true)

2. Will Florida (State) be one of the top 5 states with the most recorded fatal police shootings? 
    * Florida is among the top 5 states (#3) with the most fatal police shootings.
    * Note: See chart in # 4.
    
3. Which City has the most recorded fatal police shootings? 
    * Cities with Highest Count of Fatal Shootings:
        - Los Angeles
        - Phoenix
        - Houston
        - Las Vegas
        - San Antonio
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
            

4. Which State has the most recorded fatal police shootings?
    * States with Highest Count of Fatal Shootings:
        - California
        - Texas
        - Florida
        - Arizona
        - Colorado 
    * [Analysis Location 1](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)
    * [Analysis Location 2](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
       
       ![Count of Fatal Shootings by State Bar Chart](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/state_bar.png?raw=true)  

5. Have police shootings increased in the past five years?
    * The overall count of police shootings a year has remained consistent.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
       
       ![Shooting Analysis by Year ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Shootings%20per%20Year.png?raw=true) 
    
6. Is there a particular time of the year during which police shootings occur more frequently?
    * Most police shootings take place at the beginning of the year, specifically in February.
    * Further research can be conducted to specify why this is.
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)
        
        ![Shooting Analysis by Month ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Shootings%20by%20Month.png?raw=true) 

**Additional Analysis Conducted** 

* Victim Age Distribution
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_SZ.ipynb)
    
        ![Count of Fatal Shootings by Age Group Histogram](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Age%20Distribution%20Histogram.png?raw=true) 
        
* Victim Gender
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
    
        ![Victim Gender Bar Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Gender_Race_Bar.png?raw=true)

* Gender and Age Group
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
    
        ![Victim Gender vs Age Group Bar Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Gender_Age_Bar.png?raw=true)

* Female Fatal Shooting Deaths by Race and Age Group
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis_BH.ipynb)
    
        ![Female Data - Race and Age Group Bar Plot](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Combined_Demographics_Female.png?raw=true)

* Fatal Shootings by Race
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)

        ![Race Pie Chart ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/race_pie.png?raw=true) 

* Fatal Shootings by Race and Manner of Death
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)
    
        ![Race and Manner of Death Pie Chart ](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/race_manner_of_death_doubledonut.png?raw=true)      

* Fatal Shootings by Race and Gender
    * [Analysis Location](https://github.com/szerpa17/fatal-police-shootings/blob/master/Analysis.ipynb)
    
        ![Fatal Shootings by Race and Gender Bar Chart](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/gender_bar.png?raw=true)


## Commentary and Opportunities ##

It is worth further investigating these populations with the removal of outliers to confirm the visual trend due to the extremely low r-squared values obtained. This project could also become narrower in scope to focus on one state or a sample of states/cities for further insights.

*In regards to the demographic results - though white males make up the majority of the victims, according to the [Census Quickfacts](https://www.census.gov/quickfacts/fact/table/US/PST045219) 2019 estimates - the white population accounts for 76.3 percent of the U.S. population. Therefore the number of black victims is not proportional to the black population (listed as 13.4 percent of the U.S. population). This data analysis is still not complete without the factoring of the population makeup within each state/city area or the identification of per capita deaths by race population, which is integral to the topic of police violence.*

![Census Quickfacts Snippet](https://github.com/szerpa17/fatal-police-shootings/blob/master/images/Data%20Frames%20and%20Code%20Snippets/Census%20Quickfacts%20Table.PNG?raw=true)

There are also many additional opportunities for further exploration of this dataset in the below areas (though data may not be currently captured and released to the public on all of the below).

* Additional Data Comparisons:
    * Income inequality
    * Police funding vs fatal police shootings
    * Instances of police brutality, and non-lethal shootings
    * Officer data - shooting instances, length of service 
    * Officer staff count in city/state location
    * Political affiliation within each state/city in comparison to shootings.
* Visualizations:
    * Maps
* Relationships between other factors in the shootings data set and shooting fatalities:
    * Fleeing designation and shootings
    * Body-cams and shootings
    * Weapons
    * Mental illness