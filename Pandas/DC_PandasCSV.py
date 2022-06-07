# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('../DataFiles/cars.csv', index_col=0)

# Print out cars
print(cars)

# File path parent level:  '../file.csv'
# File path same level: '.file.csv'
# File path child level: '/childpath/file.csv'

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observation for Japan
print(cars.loc[['AUS', 'EG']])

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])
print(cars.iloc[5, 2])
print(cars.index)

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(type(cars.loc[:, 'drives_right']))
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(type(cars.loc[:, ['drives_right']]))
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])