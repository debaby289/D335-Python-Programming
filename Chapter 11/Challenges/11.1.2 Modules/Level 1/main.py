import airline_kiosk
import airline_luggage

traveler_name = input()
num_luggages = int(input())

airline_kiosk.check_in(traveler_name, num_luggages)
airline_luggage.deposit(num_luggages)