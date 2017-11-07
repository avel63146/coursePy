import datetime
import os
import multiprocessing
import random
from time import sleep

now = datetime.date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    output.write(now_str)

with open ('today.txt', 'rt') as input:
    today_string = input.read()
print(today_string)

new_today = today_string.rsplit('-')
print(new_today)

print(os.listdir('.'))
print(os.listdir('..'))

def now(seconds):
     sleep(seconds)
     print('wait', seconds, 'seconds, time is', datetime.datetime.utcnow())
if __name__ == '__main__':
     for n in range(5):
         seconds = random.randrange(1,2)
         proc = multiprocessing.Process(target=now, args=(seconds,))
         proc.start()

my_day = datetime.date(1998, 9, 22)
print(my_day)
print(my_day.weekday())
print(my_day.isoweekday())

party_day = my_day + datetime.timedelta(days=1000)
print(party_day)