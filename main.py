# Opening CSV file for reading
myfile = open('WeatherDataWindows.csv', 'r')
line = myfile.readline()
weather_list = []
row = 0
for line in myfile:
    weather_list.append(line.strip().split(',')) # Remove newline and separate by comma to make list of lists
    for col in range(1,len(weather_list[row])):
        weather_list[row][col] = float(weather_list[row][col])
    row += 1
# Compute max temp, min temp, average daily precip to 2 dec places
max_temp = weather_list[0][1]
min_temp = weather_list[0][3]
avg_precip = weather_list[0][-1]
for i in range(1,len(weather_list)):
    if weather_list[i][1] > max_temp:
        max_temp = weather_list[i][1]
    if weather_list[i][3] < min_temp:
        min_temp = weather_list[i][3]
    avg_precip += weather_list[i][-1]
avg_precip /= len(weather_list)
# Printing output
print('3-year maximum temperature: %d'%max_temp)
print('3-year minimum temperature: %d'%min_temp)
print('3-year average precipitation: %.2f'%avg_precip)
########## Part B ###########
# Gather user input
month = input('Please enter a month: ')
year = int(input('Please enter a year: '))
# Conver month to a digit
month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
for i in range(len(month_list)):
    if month == month_list[i]:
        month_value = i + 1
# Creating a list for data from the month the user asked for
user_month = []
for row in range(len(weather_list)):
    first_col = weather_list[row][0].split('/')
    if int(first_col[0]) == month_value and int(first_col[2]) == year:
        user_month.append(weather_list[row])
# Average of low temps, std deviation and humidity < 75
avg_low = 0
mean = 0
count = 0
for i in range(len(user_month)):
    avg_low += user_month[i][3]
    mean += user_month[i][-1]
    if user_month[i][8] < 75:
        count +=1
avg_low /= len(user_month)
count /= len(user_month)
count *= 100
mean /= len(user_month)
from math import sqrt
std_dev = 0
for i in range(len(user_month)):
    std_dev += abs(user_month[i][-1] - mean) ** 2
std_dev /=len(user_month)
std_dev = sqrt(std_dev)
# Printing output
print('For',month,year,':')
print('Average low temperature: %.1f'%avg_low,'F')
print('Percentage of days with average humidity below 75%%: %.1f%%'%count)
print('Standard deviation of daily precipitation: %.4f'%std_dev)
myfile.close()