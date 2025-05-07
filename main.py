from company_module import Company, Vehicle, Staff

# Create instances
iti_office = Company("ITI Smart Village")
fiat_car = Vehicle("Fiat 128", fuel_rate=100, velocity=60)
samy = Staff("Samy", 1000, "Neutral", 80, emp_id=1, car=fiat_car, email="samy@iti.org", salary=5000, commute_distance=20)

# Hire and simulate work
iti_office.hire(samy)

print("-- Samy starts his day --")
samy.commute(speed=60, distance=20)
iti_office.assess_lateness(emp_id=1, departure_time=7.0)

print(f"Samy's salary: {samy.salary}")
print(f"Remaining fuel: {samy.car.fuel_rate}")
