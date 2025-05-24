def year_to_day(year):
  '''this function converts our year integer to an integer which is the amount of days that have passed from year 0 to December 31 of the previous year (including December 31 of the previous year)'''
  four_years = year // 4
  days_in_four_years = (3* 365 +366)
  remaining_years = (year % 4)
  days_of_year = four_years * days_in_four_years + remaining_years * 365 - 1*(year//100) + 1*(year//400)
  return days_of_year

def month_to_day(month, year):
  '''this function converts our 3-letter month string to an integer which is the amount of days that have passed from January till the month before the "month" parameter'''
  month_letters = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  month_number = month_letters.index(month) + 1
  lom = [31, 28, 31, 30, 31, 30,31,31,30,31,30,31]
  days_of_month = sum(lom[:(month_number-1)])
  return days_of_month 

def calculateDaysBetween(date1, date2):
  '''this function takes the two date strings and does the following:
  - It splits the string into a month string, a day integer, and year integer
  - We then use month_to_day() and year_to_day() to figure out the amount of time of the years and months in days
  - After this, we add the days of the months, years, and the original days to get the total amount of time in days
  - Finally, we subtract the times in days from each other
  '''
  date1 = date1.split()
  date2 = date2.split()
  year_1 = int(date1[2])
  year_2 = int(date2[2])
  month_1 = date1[0] 
  month_2 = date2[0]
  day_1 = int(date1[1][:-1])
  day_2 = int(date2[1][:-1])
  days_of_year_1 = year_to_day(year_1)+month_to_day(month_1, year_1)+day_1
  days_of_year_2 = year_to_day(year_2)+month_to_day(month_2, year_2)+day_2
  difference = abs(days_of_year_1 - days_of_year_2)
  return difference