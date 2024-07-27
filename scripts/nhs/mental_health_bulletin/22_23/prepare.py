import os
import pandas as pd

RAW_DIR = os.path.join('data', 'nhs', 'mental_health_bulletin_22_23', 'percentage_secondary_age_gender_year.csv')
OUT_DIR = os.path.join('src', '_data', 'nhs', 'mental_health_bulletin', '22_23')

if __name__ == '__main__': 

    df = pd.read_csv(RAW_DIR) 

    df_long = df.melt(id_vars=['Gender', 'Age'], var_name='Year', value_name='Value')

    df_long.set_index('Year', inplace=True)

    df_long['Value'] = (df_long['Value']*100).round(2)

    df_long.to_csv(os.path.join(OUT_DIR, 'percent_sec_gender_age_22_23.csv'))
