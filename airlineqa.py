from Airlinereservation import Airlinereservation
a = AirlineReservation()
passed = 0
def test(n, name, expected, actual):
    global passed
    status = "PASS" if expected == actual else "FAIL"
    if status == "PASS":
        passed += 1
    print("TC", n, "-", name,
          "| Expected:", expected,
          "| Actual:", actual,
          "|", status)
r = a.book("Arun", "Adult", "AI101",
           "Economy", "2026-08-20", 10)
test(1, "Successful Booking", "Confirmed", r["Status"])
a = AirlineReservation()
for name in ["A", "B", "C"]:
    a.book(name, "Adult", "AI101",
           "Economy", "2026-08-20", 10)
r = a.book("D", "Adult", "AI101",
           "Economy", "2026-08-20", 10)
test(2, "Double Booking", "Fully Booked", r)
a = AirlineReservation()
r = a.book("Rahul", "Adult", "AI101",
           "Economy", "2026-08-20", 10)
refund = a.cancel(r["Booking ID"])
test(3, "Cancellation", True, refund > 0)
a = AirlineReservation()
r = a.book("Priya", "Adult", "AI101",
           "Economy", "2026-08-20", 10)
expected = round(r["Total"] * .8, 2)
actual = a.cancel(r["Booking ID"])
test(4, "Refund", expected, actual)
a = AirlineReservation()
a.book("A", "Adult", "AI101",
       "First", "2026-08-20", 10)
r = a.book("B", "Adult", "AI101",
           "First", "2026-08-20", 10)
test(5, "Fully Booked Flight", "Fully Booked", r)
a = AirlineReservation()
r = a.book("", "Adult", "AI101",
           "Economy", "2026-08-20", 10)
test(6, "Invalid Passenger",
     "Invalid Passenger", r)
a = AirlineReservation()
r = a.book("Vijay", "Adult", "AI101",
           "Economy", "2026-08-20", 25)
test(7, "Excess Baggage", 5000,
     r["Baggage Charge"])
a = AirlineReservation()
f1 = a.price("AI202", "Adult",
             "Economy", "2026-07-01")
f2 = a.price("AI202", "Adult",
             "Economy", "2026-09-18")
test(8, "Dynamic Fare", True, f1 != f2)
print("\nTOTAL:", 8)
print("PASSED:", passed)
print("FAILED:", 8 - passed)
