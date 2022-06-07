# Import cars data
import pandas as pd
cars = pd.read_csv('../DataFiles/cars.csv', index_col = 0)
print(cars)
# Iterate over rows of cars
for key, data in cars.iterrows():
    print(key + ": " + str(data["cars_per_cap"]))

# Code for loop that adds COUNTRY column
# for key, data in cars.iterrows():
#     cars.loc[key, "COUNTRY"] = data["country"].upper()

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)