#Define list
DataF = [1,3,5,7,9,11]

#What is the first and the last item
FirstI = DataF[0]
LastI = DataF[-1]
print("First Item is:", FirstI, "The last item is:", LastI)

print(" ")

#Sorting#

#Sorting by length
def my_function(e):
	return len(e)

cars = ['Ford', 'BMW', 'Volvo', 'Mitsubishi']

cars.sort(key=my_function)

print(cars)

#Sorting a dictionary
def my_fc(e):
    return e['year']

cars1 = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars1.sort(key=my_fc)
print(cars1)