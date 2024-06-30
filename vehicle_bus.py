class Vehicle:
    def __init__(self, seat_cap=0, fare=0, maintain=0) -> None:
        self.seat_cap = seat_cap
        self.fare = self.seat_cap*100
        self.maintain = maintain
        self.total_fare= fare + maintain*fare
class Bus(Vehicle):
    def __init__(self,seat_cap=0, fare=0, maintain=0) -> None:
        super().__init__(seat_cap=0, fare=0, maintain=0)
        self.maintain = 0.1
        self.total_fare= self.fare + self.maintain*self.fare
bus1= Bus()
bus1.fare=5000
print(bus1.total_fare)