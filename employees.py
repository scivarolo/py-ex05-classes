class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_job_title(self):
        return self.job_title

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_start_date(self):
        return self.start_date

class Company(object):
    """Represents a company in which people work."""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def get_company_name(self):
        """Returns the name of the company."""
        return self.company_name

    def set_company_name(self, company_name):
        self.company_name = company_name

    def get_date_founded(self):
        return self.date_founded

    def print_employees_list(self):

        for employee in self.employees:
            print(f"{employee.name}, {employee.job_title}")

    def hire_employee(self, employee):
        self.employees.append(employee)

    def fire_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)


awesome_place = Company("Awesome Place", "January 9, 2019")

kelly = Employee("Kelly", "Senior Organizer", "January 9, 2019")
sebastian = Employee("Sebastian", "Founder", "January 9, 2019")
nolan = Employee("Nolan", "Respeaker", "January 9, 2019")

awesome_place.hire_employee(kelly)
awesome_place.hire_employee(sebastian)
awesome_place.hire_employee(nolan)

print("All Employees")
awesome_place.print_employees_list()

awesome_place.fire_employee("Kelly")
print("\nAfter Firing Kelly")
awesome_place.print_employees_list()