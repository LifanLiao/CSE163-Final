import pandas as pd


def death_counts_init():
    '''
    initializes COVID-19_Death_Counts_by_Week_Ending_Date_and_State dataset
    for covid-19 analysis project.
    returns a concentrated dataframe that is easier to use
    for later analysis.
    '''
    path = 'datasets\\COVID-19_Death_Counts_by_Week_Ending_Date_and_State.csv'
    state_name_path = 'datasets\\StateNames.csv'
    columns = ['Group', 'Year', 'Month', 'State',
               'COVID-19 Deaths', 'Total Deaths']

    death_df = pd.read_csv(path)
    state_name_df = pd.read_csv(state_name_path)

    death_df = death_df[columns]
    death_df = death_df[death_df['Group'] == 'By Month']
    # death_df = death_df.dropna()

    # remove punctuation
    cov_death = 'COVID-19 Deaths'
    total_death = 'Total Deaths'
    death_df[cov_death] = death_df[cov_death].str.replace(r'[^\w\s]+', '')
    death_df[total_death] = death_df[total_death].str.replace(r'[^\w\s]+', '')

    # turn data into numeric
    death_df[cov_death] = pd.to_numeric(death_df[cov_death])
    death_df[total_death] = pd.to_numeric(death_df[total_death])
    death_df['Year'] = pd.to_numeric(death_df['Year'])

    death_df = death_df.merge(state_name_df, left_on='State',
                              right_on='State', how='left')

    return death_df


def death_single(df, state, year):
    '''
    Takes in the initialized death count dataframe,
    a state name as string, and
    year as int,
    returns a dataframe that indicates the number and percent
    of covid death for each month of a given year in a given state.
    '''
    # select state
    df = df[df['Code'] == state]

    # select year
    df = df[df['Year'] == year]

    # calculate death pct of covid death
    df['pct_covid_death'] = (df['COVID-19 Deaths'] / df['Total Deaths']) * 100

    return df


# for checking df structure
'''
df = death_counts_init()
print(df)
df = death_counts(df, 'WA', 2021)
print(df)
'''
