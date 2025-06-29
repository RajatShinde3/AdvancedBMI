import matplotlib.pyplot as plt
import pandas as pd

def show_bmi_graph(user_df, username):
    if user_df.empty:
        return

    user_df["Date"] = pd.to_datetime(user_df["Date"])
    plt.figure(figsize=(8, 4))
    plt.plot(user_df["Date"], user_df["BMI"], marker='o', color="#00BFFF")
    plt.title(f"BMI Trend for {username}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
