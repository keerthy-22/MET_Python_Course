class HotelRoom:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.booking_status = False

    def book_room(self):
        if not self.booking_status:
            self.booking_status = True
            print("\nRoom booked successfully.")
        else:
            print("\nRoom is already booked.")

    def cancel_booking(self):
        if self.booking_status:
            self.booking_status = False
            print("\nBooking cancelled successfully.")
        else:
            print("\nRoom is not booked.")

    def display_details(self):
        print("\n------ Room Details ------")
        print("Room Number    :", self.room_number)
        print("Room Type      :", self.room_type)
        print("Price per Night: ₹", self.price_per_night)

        if self.booking_status:
            print("Booking Status : Booked")
        else:
            print("Booking Status : Available")


# User Input
room_number = int(input("Enter Room Number: "))
room_type = input("Enter Room Type (Single/Double/Deluxe): ")
price = float(input("Enter Price per Night: "))

# Create Object
room1 = HotelRoom(room_number, room_type, price)

# Display Initial Details
room1.display_details()

# Book the Room
room1.book_room()

# Display Updated Details
room1.display_details()

# Cancel the Booking
room1.cancel_booking()

# Display Final Details
room1.display_details()
