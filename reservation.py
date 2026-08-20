from datetime import datetime
class AirlineReservation:
    def __init__(self):
        self.flights = {
            "AI101": {
                "source": "Chennai",
                "destination": "Delhi",
                "travel_date": "2026-09-15",
                "economy": 3,
                "business": 2,
                "first": 1
            },
            "AI202": {
                "source": "Chennai",
                "destination": "Mumbai",
                "travel_date": "2026-09-20",
                "economy": 5,
                "business": 2,
                "first": 1
            }
        }
        self.base_fares = {
            "Economy": 5000,
            "Business": 10000,
            "First": 20000
        }
        self.bookings = {}
        self.next_booking_id = 1
    def search_flights(self, source, destination):
        result = []
        for flight_no, flight in self.flights.items():
            if (flight["source"] == source and
                    flight["destination"] == destination):
                result.append(flight_no)
        return result
    def seat_availability(self, flight_no):
        if flight_no not in self.flights:
            return "Invalid Flight"
        flight = self.flights[flight_no]
        return {
            "Economy": flight["economy"],
            "Business": flight["business"],
            "First": flight["first"]
        }
    def calculate_fare(self, flight_no, passenger_type, seat_class,
                       booking_date):
        if flight_no not in self.flights:
            return "Invalid Flight"
        if seat_class not in self.base_fares:
            return "Invalid Class"
        flight = self.flights[flight_no]
        if seat_class == "Economy":
            seats = flight["economy"]
        elif seat_class == "Business":
            seats = flight["business"]
        else:
            seats = flight["first"]
        if seats <= 0:
            return "Fully Booked"
        fare = self.base_fares[seat_class]
        if seats == 1:
            fare *= 1.50
        elif seats == 2:
            fare *= 1.30
        elif seats <= 3:
            fare *= 1.15
        booking = datetime.strptime(booking_date, "%Y-%m-%d")
        travel = datetime.strptime(
            flight["travel_date"], "%Y-%m-%d"
        )
        days_before = (travel - booking).days
        if days_before <= 3:
            fare *= 1.40
        elif days_before <= 7:
            fare *= 1.20
        elif days_before > 30:
            fare *= 0.90
        if passenger_type == "Child":
            fare *= 0.75
        elif passenger_type == "Senior":
            fare *= 0.80
        elif passenger_type == "Adult":
            pass
        else:
            return "Invalid Passenger"
        return round(fare, 2)
    def book_ticket(self, passenger_name, passenger_type,
                    flight_no, seat_class, booking_date,
                    baggage_kg):
        if not passenger_name:
            return "Invalid Passenger"
        if passenger_type not in ["Adult", "Child", "Senior"]:
            return "Invalid Passenger"
        if flight_no not in self.flights:
            return "Invalid Flight"
        if seat_class not in ["Economy", "Business", "First"]:
            return "Invalid Class"
        flight = self.flights[flight_no]
        if seat_class == "Economy":
            if flight["economy"] <= 0:
                return "Fully Booked"
        elif seat_class == "Business":
            if flight["business"] <= 0:
                return "Fully Booked"
        else:
            if flight["first"] <= 0:
                return "Fully Booked"
        fare = self.calculate_fare(
            flight_no,
            passenger_type,
            seat_class,
            booking_date
        )
        if isinstance(fare, str):
            return fare
        free_baggage = {
            "Economy": 15,
            "Business": 25,
            "First": 40
        }
        allowed = free_baggage[seat_class]
        excess = max(0, baggage_kg - allowed)
        baggage_charge = excess * 500
        total = fare + baggage_charge
        booking_id = "B" + str(self.next_booking_id)
        self.next_booking_id += 1
        self.bookings[booking_id] = {
            "passenger": passenger_name,
            "passenger_type": passenger_type,
            "flight": flight_no,
            "class": seat_class,
            "fare": fare,
            "baggage": baggage_charge,
            "total": total,
            "status": "Confirmed"
        }
        if seat_class == "Economy":
            flight["economy"] -= 1
        elif seat_class == "Business":
            flight["business"] -= 1
        else:
            flight["first"] -= 1
        return {
            "Booking ID": booking_id,
            "Passenger": passenger_name,
            "Flight": flight_no,
            "Class": seat_class,
            "Fare": round(fare, 2),
            "Baggage Charge": baggage_charge,
            "Total": round(total, 2),
            "Status": "Confirmed"
        }
    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            return "Invalid Booking"
        booking = self.bookings[booking_id]
        if booking["status"] == "Cancelled":
            return "Already Cancelled"
        booking["status"] = "Cancelled"
        flight = self.flights[booking["flight"]]
        if booking["class"] == "Economy":
            flight["economy"] += 1
        elif booking["class"] == "Business":
            flight["business"] += 1
        else:
            flight["first"] += 1
        refund = booking["total"] * 0.80
        return round(refund, 2)
if __name__ == "__main__":
    airline = AirlineReservation()
    print("AIRLINE RESERVATION SYSTEM")
    print("==========================")
    print("\nFlight Search:")
    print(
        airline.search_flights(
            "Chennai",
            "Delhi"
        )
    )

    print("\nSeat Availability:")
    print(
        airline.seat_availability("AI101")
    )
    print("\nBooking:")

    result = airline.book_ticket(
        "Rahul",
        "Adult",
        "AI101",
        "Economy",
        "2026-08-20",
        20
    )
    print(result)
