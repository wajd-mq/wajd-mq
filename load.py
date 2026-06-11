import pandas as pd
import os

def load_to_csv(record):

    os.makedirs("data", exist_ok=True)

    filepath = "data/weather.csv"

    df = pd.DataFrame([record])

    if os.path.exists(filepath):
        df.to_csv(
            filepath,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            filepath,
            index=False
        )

