## 1. Programming And Data Science ##

england = 135
china = 123
india = 124
united_states = 134

## 2. Display Values Using The Print Function ##

china = 123
india = 124
united_states = 134
china = 123
india = 124
united_states = 134
print(china)
print(india)
print(united_states)

## 3. Data Types ##


china_name = "China"
china_rounded = 123
china_exact = 122.5

print(china_name)
print(china_rounded)
print(china_exact)

## 4. The Type Function ##

china_name = "China"
china_exact = 122.5
print(type(china_exact))

## 5. Converting Types ##

china_rounded = 123
china_exact = 122.5
int_to_str = str(china_rounded)
str_to_int = int(int_to_str)

## 6. Comments ##

china = 123
india = 124
united_states = 134
# Number one in population.
china = 123
# Number two in population.
india = 124
# Number three in population.
united_states = 134

## 7. Arithmetic Operators ##


china_plus_10 = china + 10
us_times_100 = united_states * 100
print(china_plus_10)
print(us_times_100)

## 8. Order Of Operations ##

china = 123
india = 124
united_states = 134
china_celsius = (china - 32) * 0.56
india_celsius = (india - 32) * 0.56
us_celsius = (united_states - 32) * 0.56

## 9. Console ##




## 10. Using A List To Store Multiple Values ##


# Create empty lists.
countries = []
temperatures = []

# Add values to each list.
countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)

print(countries)
print(temperatures)

## 11. Creating Lists With Values ##


temps = ["China", 122.5, "India", 124.0, "United States", 134.1]

## 12. Accessing Elements In A List ##

countries = []
temperatures = []

countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)

# Add your code here.
countries = []
temperatures = []

countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)

# Add your code here.
china = countries[0]
china_temperature = temperatures[0]

## 13. Retrieving The Length Of A List ##

countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
two_sum = len(countries) + len(temperatures)

## 14. Slicing Lists ##

countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
countries_slice = countries[1:4]
temp_length = len(temperatures)
temperatures_slice = temperatures[len(temperatures)-3: len(temperatures)]

## 15. Next steps ##

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
index = len(months) - 2
second_last = months[index]
print(second_last)