def book_stay(guests_db, room_catalog, guest_id, room_type, nights):
    
    if guest_id not in guests_db:
        raise KeyError("Guest ID not found")
    if room_type not in room_catalog:
        raise KeyError("Invalid room type") 
    if type(nights) != int or nights < 1:
        raise ValueError("Nights must be positive integer")
    room_price = room_catalog[room_type]["price"]
    cleaning_fee = room_catalog[room_type]["cleaning_fee"]
    total_cost=(nights * room_price) + cleaning_fee
    balance=guests_db[guest_id]["balance"]
    if balance < total_cost:
        raise ValueError("Insufficient funds")
    guests_db[guest_id]["balance"]-= total_cost
    return float(total_cost)
    
def process_bookings(guests_db, room_catalog, booking_list):
    total_revenue=0.0
    failed_bookings=0
    result = {}
    for guest_id,room_type,nights in booking_list:
        try:
            cost = book_stay(guests_db, room_catalog, guest_id, room_type, nights)
            total_revenue += cost
        except (KeyError,ValueError) as e:
            print(f'Booking Error for {guest_id}: {e}')
            failed_bookings=failed_bookings+1
    return {"total_revenue": total_revenue,
            "failed_bookings":failed_bookings}

        
rooms = {
    "Standard": {"price": 100.0, "cleaning_fee": 20.0},
    "Suite":    {"price": 200.0, "cleaning_fee": 50.0}
}

# Format: {GuestID: {"balance": float}}
guests = {
    "G1": {"balance": 300.0},
    "G2": {"balance": 50.0}
}

bookings = [
    ("G1", "Standard", 2),    # Valid. Cost: 200+20=220. Rem: 80.
    ("G2", "Suite", 1),       # Error: Cost 250 > Bal 50.
    ("G3", "Standard", 1),    # Error: Guest ID not found.
    ("G1", "Penthouse", 1),   # Error: Invalid room type.
    ("G1", "Standard", 0)     # Error: Nights must be positive.
]

result = process_bookings(guests, rooms, bookings)
print(result)