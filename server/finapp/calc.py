import pandas as pd
import json

data = pd.read_csv("finance.csv")


data["Částka"] = data["Částka"].str.replace("\s","", regex=True)
data["Částka"] = pd.to_numeric(data["Částka"])

df = data[["Kategorie", "Částka"]]
df_sum = df.groupby(["Kategorie"]).sum()
df_avg = df.groupby(["Kategorie"]).mean()
df_min = df.groupby(["Kategorie"]).min()
df_grouped = pd.concat([df_sum, df_avg, df_min], axis=1)
df_grouped.columns = ["sum", "avg", "min"]

final = df_grouped[:9].to_json(orient="index")
final = json.loads(final)

# print(final)
