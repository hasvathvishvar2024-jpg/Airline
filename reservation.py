class AirlineReservation:
    def __init__(self):
        self.flights = {
            "AI101": ["Chennai", "Delhi", "2026-09-15", 3, 2, 1],
            "AI202": ["Chennai", "Mumbai", "2026-09-20", 5, 2, 1]
        }
        self.fare = {"Economy": 5000, "Business": 10000, "First": 20000}
        self.bookings = {}
        self.bid = 1
    def search(self, src, dest):
        return [f for f, x in self.flights.items()
                if x[0] == src and x[1] == dest]
    def seats(self, flight):
        if flight not in self.flights:
            return "Invalid Flight"
        x = self.flights[flight]
        return {"Economy": x[3], "Business": x[4], "First": x[5]}
    def price(self, flight, ptype, cls, date):
        if flight not in self.flights:
            return "Invalid Flight"
        if cls not in self.fare:
            return "Invalid Class"
        if ptype not in ["Adult", "Child", "Senior"]:
            return "Invalid Passenger"
        x = self.flights[flight]
        i = {"Economy": 3, "Business": 4, "First": 5}[cls]
        if x[i] <= 0:
            return "Fully Booked"
        f = self.fare[cls]
        if x[i] == 1:
            f *= 1.5
        elif x[i] == 2:
            f *= 1.3
        elif x[i] == 3:
            f *= 1.15
        days = (int(x[2][8:]) - int(date[8:])) + \
               (int(x[2][5:7]) - int(date[5:7])) * 30
        if days <= 3:
            f *= 1.4
        elif days <= 7:
            f *= 1.2
        elif days > 30:
            f *= 0.9
        if ptype == "Child":
            f *= .75
        elif ptype == "Senior":
            f *= .8
        return round(f, 2)
    def book(self, name, ptype, flight, cls, date, baggage):
        if not name:
            return "Invalid Passenger"
        if ptype not in ["Adult", "Child", "Senior"]:
            return "Invalid Passenger"
        if flight not in self.flights:
            return "Invalid Flight"
        if cls not in self.fare:
            return "Invalid Class"
        x = self.flights[flight]
        i = {"Economy": 3, "Business": 4, "First": 5}[cls]
        if x[i] <= 0:
            return "Fully Booked"
        f = self.price(flight, ptype, cls, date)
        if isinstance(f, str):
            return f
        free = {"Economy": 15, "Business": 25, "First": 40}[cls]
        bag = max(0, baggage - free) * 500
        total = f + bag
        bid = "B" + str(self.bid)
        self.bid += 1
        self.bookings[bid] = [flight, cls, total, "Confirmed"]
        x[i] -= 1
        return {"Booking ID": bid, "Status": "Confirmed",
                "Fare": f, "Baggage Charge": bag, "Total": total}
    def cancel(self, bid):
        if bid not in self.bookings:
            return "Invalid Booking"
        b = self.bookings[bid]
        if b[3] == "Cancelled":
            return "Already Cancelled"
        b[3] = "Cancelled"
        x = self.flights[b[0]]
        i = {"Economy": 3, "Business": 4, "First": 5}[b[1]]
        x[i] += 1
        return round(b[2] * .8, 2)
if __name__ == "__main__":
    a = AirlineReservation()
    print("AIRLINE RESERVATION")
    print(a.search("Chennai", "Delhi"))
    print(a.seats("AI101"))
    print(a.book("Rahul", "Adult", "AI101",
                 "Economy", "2026-08-20", 20))
