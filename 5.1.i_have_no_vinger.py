import datetime
import random

fDate = datetime.datetime.strptime(input("write a date (YYYY-MM-DD):"), '%Y-%m-%d')
sDate = datetime.datetime.strptime(input("write a date (YYYY-MM-DD):"), '%Y-%m-%d')

randDate = datetime.datetime.fromtimestamp(random.uniform(fDate.timestamp(), sDate.timestamp()))

if (randDate.weekday() == 0):
    print("I have no vinaigrette!")
