import death_counts_init
import vaccine_dataset_init
import pandas as pd


def vacc_death_aggregate():
    '''
    Uses initialized vaccine and death datasets
    output csv file with columns:
    'Code', 'COVID_Death_Rate', 'Vaccine_Rate'
    by December 2021
    '''
    vac_df = vaccine_dataset_init.vaccine_init()
    death_df = death_counts_init.death_counts_init()

    # concentrate vaccine dataframe
    vac_df = vac_df[vac_df['Year'] == 2021]
    vac_df = vac_df[vac_df['Month'] == 12]

    columns = ['Recip_State', 'Administered_Dose1_Recip', 'Census2019']
    vac_df = vac_df[columns]

    col = ['Administered_Dose1_Recip', 'Census2019']
    vac_df = pd.DataFrame(vac_df.groupby('Recip_State')[col].sum())
    vac_df = vac_df.reset_index()

    vac_df['Vaccine_Rate'] = (vac_df['Administered_Dose1_Recip'] /
                              vac_df['Census2019']) * 100
    vac_df = vac_df[['Recip_State', 'Vaccine_Rate']]

    # concentrate death dataframe
    columns = ['Year', 'State', 'COVID-19 Deaths', 'Total Deaths', 'Code']
    death_df = death_df[columns]
    death_df = death_df[death_df['Year'] == 2021]
    death_df = death_df[death_df['State'] != 'United States']

    col = ['COVID-19 Deaths', 'Total Deaths']
    death_df = pd.DataFrame(death_df.groupby('Code')[col].sum()).reset_index()
    death_df['COVID_Death_Rate'] = (death_df['COVID-19 Deaths'] /
                                    death_df['Total Deaths']) * 100
    death_df = death_df[['Code', 'COVID_Death_Rate']]

    # combine
    aggregated = death_df.merge(vac_df, left_on='Code', right_on='Recip_State')
    aggregated = aggregated[['Code', 'COVID_Death_Rate', 'Vaccine_Rate']]

    # write csv file
    path = 'datasets\\aggregated_table_v_d_rate_by_state.csv'
    aggregated.to_csv(path)
    return aggregated


def main():
    vacc_death_aggregate()


if __name__ == '__main__':
    main()
