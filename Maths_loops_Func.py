import math
from datetime import datetime, timedelta
# Define your start and end dates

def Adjust_Rate(rate,pct) :
    New_Rate = round(Base_Rate*(1+Multiplier),-2)
    return New_Rate

start_str = "2025-06-01"
Base_Rate = 9000
Multiplier = 0.15


# Convert to datetime objects
start = datetime.strptime(start_str, "%Y-%m-%d")
end = start + timedelta(days=10)
# Build the list<br>
dates = []
current = start

while current <= end:
     dates.append(current.strftime("%Y-%m-%d"))
     current += timedelta(days=1)

for d in dates :
    Multiplier = Multiplier + .01
    New_Rate = Adjust_Rate(Base_Rate,Multiplier)
    print(f"Date : {d} : {New_Rate}")





