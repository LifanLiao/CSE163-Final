import pandas as pd


def vaccine_init():
    '''
    initializes COVID-19_Vaccinations_in_the_United_States_County dataset
    for covid-19 analysis project.
    returns a concentrated dataframe that is easier to use
    for later analysis.
    '''
    path = 'datasets\\COVID-19_Vaccinations_in_the_United_States_County.csv'
    columns = ['Date', 'Recip_State', 'Administered_Dose1_Recip', 'Census2019']

    vacc_df = pd.read_csv(path)
    vacc_df = vacc_df[columns]
    # vacc_df = vacc_df.dropna()

    # determine day, year, and month
    vacc_df['Year'] = pd.DatetimeIndex(vacc_df['Date']).year
    vacc_df['Month'] = pd.DatetimeIndex(vacc_df['Date']).month
    vacc_df['Day'] = pd.DatetimeIndex(vacc_df['Date']).day

    # only include day 1 for each month
    vacc_df = vacc_df[vacc_df['Day'] == 1]

    # remove punctuation
    recip = 'Administered_Dose1_Recip'
    census = 'Census2019'
    vacc_df[recip] = vacc_df[recip].str.replace(r'[^\w\s]+', '')
    vacc_df[census] = vacc_df[census].str.replace(r'[^\w\s]+', '')

    # turn into numeric data
    vacc_df[recip] = pd.to_numeric(vacc_df[recip])
    vacc_df[census] = pd.to_numeric(vacc_df[census])

    return vacc_df


def vaccine_single(vacc_df, state, year):
    '''
    Takes in the initialized vaccine dataframe,
    a state name as string, and
    year as int,
    returns a dataframe indicates the number of dose1
    by the first day of months of a given year
    in a given state
    '''
    # select state
    df = vacc_df[vacc_df['Recip_State'] == state].copy()

    # select year
    df = df[df['Year'] == year]

    # group by month and sum up
    columns = ['Administered_Dose1_Recip', 'Census2019']
    total_vacc = pd.DataFrame(df.groupby('Month')[columns].sum())

    # calculate pct of dose1
    total_vacc['pct_dose1'] = (total_vacc[columns[0]] /
                               total_vacc[columns[1]]) * 100

    # state indicator
    total_vacc['State'] = state

    return total_vacc


# for checking df structure

# df = vaccine_init()
# print(df)
# df = vaccine(df, 'WA', 2021)
# print(df)
