import pandas as pd

df = pd.read_csv("covid_data.csv")

print("Data Snapshot:")
print(df)

print("\nTotal confirmed cases by country:")
print(df.groupby("Country")["Confirmed"].sum())

print("\nTotal deaths:")
print(df["Deaths"].sum())

df["Death Rate (%)"] = (df["Deaths"] / df["Confirmed"]) * 100
print("\nDeath rate by country:")
print(df[["Country", "Death Rate (%)"]])
