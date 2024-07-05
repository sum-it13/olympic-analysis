import pandas as pd
def preprocess(df,region_df):

    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    #merging with region_df
    df = df.merge(region_df, on='NOC', how='left')
    #dropping duplicate values
    df.drop_duplicates(inplace=True)
    #medal tally
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df