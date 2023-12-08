import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("Enter Phone Number: ")
phone=phonenumbers.parse(number)
time_zone=timezone.time_zones_for_number(phone)
carrier_dtl=carrier.name_for_number(phone,"en")
registration=geocoder.description_for_number(phone,"en")
print("-------------------------------------------------")
print("Your Phone Number: ",number)
print("phone: ",phone)
print("time_zone: ",time_zone)
print("carrier_dtl: ",carrier_dtl)
print("registration: ",registration)
print("-------------------------------------------------")
