import pandas as pd
import os
from datetime import datetime

DATA_PATH = os.path.join("data", "bmi_history.csv")

def save_bmi_record(name, weight, height, bmi, category):
    data = {
        "Name": name,
        "Weight": weight,
        "Height": height,
        "BMI": round(bmi, 2),
        "Category": category,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([data])
    os.makedirs("data", exist_ok=True)
    if os.path.exists(DATA_PATH):
        df.to_csv(DATA_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_PATH, index=False)

def get_user_history(name):
    if not os.path.exists(DATA_PATH):
        return None
    df = pd.read_csv(DATA_PATH)
    return df[df["Name"].str.lower() == name.lower()]
