# calendarTools import

from calendarTools import *
from itertools import *

date1 = "Jun 12, 2015"
date2 = "Aug 05, 2017"
date3 = "Aug 25, 2016"
date4 = "Dec 10, 2017"
date5 = "Jan 03, 2018"
date6 = "Mar 03, 2020"
date7 = "Mar 03, 2120"

list_of_dates = ["Jun 12, 2015", "Aug 05, 2017", "Aug 25, 2016", "Dec 10, 2017", "Jan 03, 2018", "Mar 03, 2020", "Mar 03, 2120"]

sample_inputs = list(combinations(list_of_dates, 2))
print(sample_inputs)

for sample_input in sample_inputs:
  date1 = sample_input[0]
  date2 = sample_input[1]
  difference = calculateDaysBetween(date1, date2)
  print(difference)