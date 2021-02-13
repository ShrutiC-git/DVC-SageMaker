import pandas as pd
df = pd.read_csv("Iris.data")
print(df.head())
all_features = df.columns

useless = [ "Id","Species"]
df_y = df["Species"]
df = df.drop(['Id', 'Species'], axis=1)
df.to_csv("data_processed.csv", index=False)
df_y.to_csv("labels.csv", index=False)

print(df.shape)