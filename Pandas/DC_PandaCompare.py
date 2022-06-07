# Import pandas as pd
import pandas as pd

# Import numpy, you'll need this
import numpy as np

# Import the cars.csv data: cars
cars = pd.read_csv('../DataFiles/cars.csv', index_col=0)

# Print out cars
print(cars)

# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)

# Use dr to subset cars: sel
sel = cars[cars['drives_right']]
# sel = cars[dr]

# Print sel
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc500 = cars['cars_per_cap'] > 500
car_maniac = cars[cpc500]

# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)

