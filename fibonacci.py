#Exercise 1: Filter out all of the empty strings from the list below

places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

lambda_function = lambda x:x if x.strip() else None
filtered_places = list(filter(lambda_function,places))
print("Unfiltered:", places)
print("Filtered:",filtered_places)

#Exercise 2: Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

def convert(authors):
    li = list(string.split(" "))
    return li

print("="*20)

filtered_authors = sorted(authors, key= lambda n:n.split(" ")[1].lower())
print("Unfiltered:", authors)
print("Filtered:", filtered_authors)

print("="*20)
#Exercise 3: Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

cities = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
filtered_cities = list(map(lambda x:x (x[0],([1]*5//9+32)), cities))

print("Unfiltered:",cities)

print("Filtered:",filtered_cities)

#Exercise 4:


def fib_seq(num):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range (2,num):
        print(n1 + n2)
        nx = n1 + n2
        n1 = n2
        n2 = nx


print(fib_seq(20))