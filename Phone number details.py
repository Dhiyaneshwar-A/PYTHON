import phonenumbers
from phonenumbers import timezone,geocoder,carrier
num=input("Enter number(+91) : ")
phone=phonenumbers.parse(num)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,'en')
desc=geocoder.description_for_number(phone,'en')
print(phone,'\n',time,'\n',car,'\n',desc)