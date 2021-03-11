from webbrowser import get
import pandas as pd

data = [{"name": "Icaro Carmona", "title": "Software Engineer"},
        {"name": "Icaro Carmona", "title": "Data Engineer"},
        {"name": "Icaro Almeida", "title": "Data Architect"}]


def get_data():
    df = pd.DataFrame(data=data)
    print('@'*66)
    print(df.head())
    print('@'*66)
    return df
