class Hotel:

    def __init__(self, name, rooms, booked, location):
        self.name = name
        self.rooms = rooms
        self.booked = booked
        self.location = location

    @property
    def check_availability(self):
        return self.rooms - self.booked
    
    def book_room(self):
        if self.check_availability > 0:
            self.booked += 1
            print('Room Booked')
        else:
            print('No Rooms Available')