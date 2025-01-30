import datetime
import calendar
from calendar import day_name
def translate_to_polish(day_name):
    english_to_polish_day_name={
        'Monday' : 'Poniedziałek',
        'Tuesday' : 'Wtorek',
        'Wednesday' : 'Środa',
        'Thursday' : 'Czwartek',
        'Friday' : 'Piątek',
        'Saturday' : 'Sobota',
        'Sunday' : 'Niedziela'
    }
    return english_to_polish_day_name[day_name]


date_of_birth = input("Type Your date of birth in format DD-MM-YYYY: ")
day,month,year= date_of_birth.split("-") #dzielimy datę na tuple z trzema zmiennymi. one są STRING

date_of_birth = datetime.datetime(int(year), int(month),int(day)) #KLASA DATETIME oczekuje INT

#print(date_of_birth.weekday()) #pokazuje nam, który to dzień tygodnia
day_name= calendar.day_name[date_of_birth.weekday()]
print(translate_to_polish(day_name)) #podaje dzień tygodnia po angielsku
