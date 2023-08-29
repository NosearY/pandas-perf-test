# %%
import pandas as pd
from icecream import ic
import time

# Read the CSV file
data = pd.read_csv("data.csv")
dfs = list(map(lambda x: data.copy(), list(range(1, 5))))

# Print the contents of the DataFrame


start_time = time.time()
for df in dfs:
    for cost in list(range(1, 10001)):
        temp = df.loc[df["Cost"] == cost] if "Cost" in df else pd.DataFrame({})
end_time = time.time()
ic("method1", end_time - start_time)


start_time = time.time()
for df in dfs:
    for cost in list(range(1, 10001)):
        df.loc[df["Cost"].values == cost]
end_time = time.time()
ic("method2", end_time - start_time)

