import pandas as pd;


def calculate_demographic_data(print_data=True):
    # Read data from file
    df=pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male=df[df['sex']=='Male']
    average_age_men = average_age_men=male['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelors =len(df[df['education']=='Bachelors'])
    percentage_bachelors=(bachelors/ len(df))*100
   

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters','Doctorate'])]

    # percentage with salary >50K
    higher_educ_rich=higher_education[higher_education['salary']=='>50K']
    higher_education_rich= len(higher_educ_rich)/len(higher_education)*100  
                           


    lower_educ_rich=lower_education[lower_education['salary']=='>50K']
    lower_education_rich=len(lower_educ_rich)/len(lower_education)*100
   

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    num_rich_min_hours = len(min_hours_workers[min_hours_workers['salary'] == '>50K'])
    rich_percentage=(num_rich_min_hours / len(min_hours_workers)) * 100
# ---------------------------------------------------------------------------
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country =df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()
    ###################


    highest_earning_country_percentage=(US_rich/populationUS)*100

    # Identify the most popular occupation for those who earn >50K in India.
    rich_in_India=df[(df['native-country']=='India') & (df['salary']=='>50K')]
    top_IN_occupation = rich_in_India['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
