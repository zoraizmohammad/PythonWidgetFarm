#Created By: Mohammad Zoraiz
#Seconds Counter
def secondstotal(days, hours, minutes, seconds):
    return ((days*24*60*60)+(hours*60*60)+(minutes*60)+seconds)

days = int(input('Enter the number of days: '))
hours = int(input('Enter the number of hours: '))
minutes = int(input('Enter the number of minutes: '))
seconds = int(input('Enter the number of seconds: '))

print ('The total number of seconds in the given time is: %ds' %secondstotal(days, hours, minutes, seconds))
