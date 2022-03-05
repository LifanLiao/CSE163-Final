import init_scripts.vaccine_dataset_init as vaccine_dataset_init
import init_scripts.death_counts_init as death_counts_init
import matplotlib.pyplot as plt
import seaborn as sns


def trend_2021_WA(v_df, d_df):
    '''
    Takes in vaccine dataframe and death dataframe,
    creates line plots for percent of covid death and dose1 in Washington
    in 2021
    '''
    v_df = vaccine_dataset_init.vaccine_single(v_df, 'WA', 2021)
    d_df = death_counts_init.death_single(d_df, 'WA', 2021)

    merged = v_df.merge(d_df, left_on='Month', right_on='Month')
    fig, axes = plt.subplots(2, 1)

    sns.lineplot(ax=axes[0], data=merged, x='Month',
                 y='pct_covid_death', color='r')
    axes[0].set_title('Trend of Percent of Covid Death in WA in 2021')
    axes[0].set_ylabel('percent of covid death')
    axes[0].grid()
    axes[0].set_facecolor((0.862, 0.870, 0.956))

    sns.lineplot(ax=axes[1], data=merged, x='Month', y='pct_dose1')
    axes[1].set_title('Trend of Percent of Dose1 in WA in 2021')
    axes[1].set_ylabel('percent of dose1')
    axes[1].grid()
    axes[1].set_facecolor((0.862, 0.870, 0.956))

    plt.tight_layout()
    fig.savefig('trend_2021_WA1.png')


def main():
    vaccine_df = vaccine_dataset_init.vaccine_init()
    death_df = death_counts_init.death_counts_init()
    trend_2021_WA(vaccine_df, death_df)


if __name__ == '__main__':
    main()
