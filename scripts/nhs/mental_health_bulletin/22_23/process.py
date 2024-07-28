import os
import pandas as pd

RAW_DIR = os.path.join('data', 'nhs', 'mental_health_bulletin_22_23', 'manual', 'percentage_secondary_age_gender_year.csv')
OUT_DIR = os.path.join('src', '_data', 'nhs', 'mental_health_bulletin')

if __name__ == '__main__': 

    df = pd.read_csv(RAW_DIR) 

    # Strip any leading or trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Melt the DataFrame to long format
    df = df.melt(id_vars=["Gender", "Age"], var_name="Year", value_name="Value")
    
    df['Year'] = df['Year'].apply(lambda x: '20' + x.split('-')[1])
    df['Value'] = df['Value'].apply(lambda x: round((x * 100),2))

    # Pivot the DataFrame to create a multi-level header
    df_pivot = df.pivot_table(index="Year", columns=["Gender", "Age"], values="Value")

    # Sort the columns to make sure they are in the right order
    df_pivot = df_pivot.sort_index(axis=1)

    # Convert the pivot table back to a DataFrame and reset index
    df_pivot_reset = df_pivot.reset_index()

    # Insert the '---' row at the third position by creating a DataFrame for it
    dash_row = pd.DataFrame([['---'] + [None] * (df_pivot_reset.shape[1] - 1)], columns=df_pivot_reset.columns)

    # Concatenate the dash_row with the rest of the DataFrame
    df_final = pd.concat([df_pivot_reset.iloc[:0], dash_row, df_pivot_reset.iloc[0:]], ignore_index=True)

    df_final.to_csv(os.path.join(OUT_DIR, 'secondary_care_gender_age.csv'), index=False)

