import Hotel as h

hotel1 = h.Hotel('Best Western', 200, 150, 'West Vancouver')
hotel2 = h.Hotel('Marriott', 200, 120, 'Victoria')

print(f'Hotel 1 is {hotel1.name}')
print(f'{hotel1.name} has {hotel1.check_availability} rooms available')
hotel1.book_room()
print(f'{hotel1.name} has {hotel1.check_availability} rooms available')

hotel_name = input('Enter name: ')
rooms = int(input('Enter # of rooms: '))
booked = int(input('Enter # of booked rooms: '))
location = input('Enter location: ')

hotel3 = h.Hotel(hotel_name, rooms, booked, location)
print(hotel3.check_availability)