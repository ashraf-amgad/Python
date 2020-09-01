


# to get date and time 
from datetime import datetime, timedelta

current_date = datetime.now()
print('\n',current_date.day,'-', current_date.month, '-', current_date.year)

print('current_date \t\t\t', current_date)
current_date_mince_one_minute = current_date - timedelta(minutes=1)
print('current_date_mince_one_minute \t',current_date_mince_one_minute)

current_date_mince_one_day = current_date - timedelta(days=1)
print('current_date_mince_one_day \t', current_date_mince_one_day)

current_date_mince_one_week = current_date - timedelta(weeks=1)
print('current_date_mince_one_week \t', current_date_mince_one_week, '\n')



birthday = input("please enter your birthday_date 'dd/mm/yyyy' ")
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('birthday is ', birthday_date)


