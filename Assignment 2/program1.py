hours=int(input('Enter the hours: '))
minutes=int(input('Enter the minutes: '))
seconds=int(input('Enter the seconds: '))
hh=hours*3600  ## because 1 hour = 3600 seconds
mm=minutes*60  ## because 1 minute = 60 seconds
total_seconds= hh + mm + seconds
print(f'total seconds in {hours} hours,{minutes} minutes and {seconds} seconds is {total_seconds}.')