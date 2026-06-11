import pandas as pd
import os

def load_to_csv(data, filename="output.csv"):

    os.makedirs("data", exist_ok=True)

    filepath = os.path.join("data", filename)

    df = pd.DataFrame([data])
    df.to_csv(filepath, index=False)

    print(f"Saved to {filepath}")