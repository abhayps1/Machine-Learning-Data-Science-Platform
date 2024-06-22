def get_description_stats(df, columns):
    df = df[columns]
    return df.describe()