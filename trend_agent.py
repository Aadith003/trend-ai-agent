
import pandas as pd
def build(df):
    return pd.crosstab(df['topic'], df['date'])
