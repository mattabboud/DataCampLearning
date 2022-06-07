import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2

# print the bmi index
print(bmi)

# print the bmi indexes results to determine if they are 23
print(bmi>23)

# print the bmi index values that are greater than 23
print(bmi[bmi>23])

# print the bmi index values that are greater than 23
print(np.where(bmi>23))

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5 , my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11 , your_house < 11))