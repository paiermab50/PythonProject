import datetime

class Human:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        self.mood = 'Happy' if hours == 7 else 'Tired' if hours < 7 else 'Lazy'

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items * 10


class Vehicle:
    def __init__(self, model, fuel_rate, velocity):
        self.model = model
        self.fuel_rate = min(max(fuel_rate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def drive(self, speed, distance):
        self.velocity = min(max(speed, 0), 200)
        fuel_needed = distance * 0.1
        if self.fuel_rate >= fuel_needed:
            self.fuel_rate -= fuel_needed
            self.stop("Arrived at destination")
        else:
            actual_distance = self.fuel_rate / 0.1
            self.fuel_rate = 0
            self.stop(f"Stopped after {actual_distance:.1f} km due to low fuel")

    def stop(self, message):
        self.velocity = 60
        print(f"[{self.model}] stopped: {message}")


class Staff(Human):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, commute_distance):
        super().__init__(name, money, mood, health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.commute_distance = commute_distance

    def work(self, hours):
        self.mood = 'Happy' if hours == 8 else 'Tired' if hours > 8 else 'Lazy'

    def commute(self, speed, distance):
        self.car.drive(speed, distance)

    def refuel_car(self, amount=100):
        self.car.fuel_rate = min(self.car.fuel_rate + amount, 100)

    def send_email(self, to, subject, body, receiver_name):
        print(f"""
        To: {to}
        Subject: {subject}
        Hi {receiver_name},
        {body}
        """)


class Company:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def list_employees(self):
        return self.employees

    def get_employee_by_id(self, emp_id):
        return next((e for e in self.employees if e.emp_id == emp_id), None)

    def hire(self, employee):
        self.employees.append(employee)
        Company.employee_count += 1

    def fire(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        Company.employee_count -= 1

    def apply_deduction(self, emp_id, amount):
        emp = self.get_employee_by_id(emp_id)
        if emp:
            emp.salary -= amount

    def apply_reward(self, emp_id, amount):
        emp = self.get_employee_by_id(emp_id)
        if emp:
            emp.salary += amount

    def assess_lateness(self, emp_id, departure_time):
        emp = self.get_employee_by_id(emp_id)
        if emp:
            lateness = Company.calculate_lateness(9, departure_time, emp.commute_distance, emp.car.velocity)
            if lateness is None:
                print("Cannot assess lateness: car velocity is zero.")
                return

            if lateness > 10:
                self.apply_reward(emp_id, 10)
            elif lateness < -10:
                self.apply_deduction(emp_id, 10)
            else:
                print(f"{emp.name} arrived on time.")

    @staticmethod
    def calculate_lateness(target_hour, departure_hour, distance, speed):
        if speed == 0:
            return None
        travel_time = distance / speed
        arrival = departure_hour + travel_time
        return arrival - target_hour

    @classmethod
    def set_employee_count(cls, number):
        cls.employee_count = number
