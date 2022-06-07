# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe/keys in Europe
print(europe)
print(europe.keys())

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)
print(europe['italy'])

# Add poland to europe
europe['poland'] = 'warsaw'

# Update capital of germany
europe['germany'] = 'berlin1'

# Add australia
europe['australia'] = 'vienna'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)