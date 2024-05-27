import pandas as pd
from ucimlrepo import fetch_ucirepo

def load_data():
    # Fetch dataset
    census_income = fetch_ucirepo(id=20)
    # Combine features and target into a single DataFrame
    df = pd.concat([census_income.data.features, census_income.data.targets], axis=1)
    return df

def demographic_data_analyzer():
    df = load_data()

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_rich = advanced_education[advanced_education['salary'] == '>50K'].shape[0]
    percentage_advanced_education_rich = round((advanced_education_rich / advanced_education.shape[0]) * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    non_advanced_education_rich = non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0]
    percentage_non_advanced_education_rich = round((non_advanced_education_rich / non_advanced_education.shape[0]) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K'].shape[0]
    percentage_rich_min_workers = round((rich_min_workers / min_workers.shape[0]) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_population = df['native-country'].value_counts()
    highest_earning_country = (country_earning / country_population * 100).idxmax()
    highest_earning_country_percentage = round((country_earning / country_population * 100).max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = india_occupation.value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_advanced_education_rich': percentage_advanced_education_rich,
        'percentage_non_advanced_education_rich': percentage_non_advanced_education_rich,
        'min_work_hours': min_work_hours,
        'percentage_rich_min_workers': percentage_rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
