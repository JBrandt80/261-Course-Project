# Jeffrey Brandt
# CIS261
# Course Project Phase 2 - Usin Lists and Dictionaries to Store and Retrieve Data
 
hourly_rate = 21.00

# Define employee data: (name, hours worked, tax rate)
employee_data = [
    ("Jeff", 40, 0.20),
    ("Brian", 38, 0.18),
    ("Kevin", 42, 0.22),
    ("Mike", 36.5, 0.19),
    ("Mark", 44, 0.21),
    ("Sara", 40, 0.20),
    ("Heather", 39, 0.17),
    ("Michele", 41, 0.23),
    ("Lindsey", 37, 0.20),
    ("Izzy", 40, 0.19)
]

from datetime import datetime

# Function to input and validate dates
def input_dates():
    while True:
        try:
            from_date = input("Enter FROM date (mm/dd/yyyy): ")
            to_date = input("Enter TO date (mm/dd/yyyy): ")
            from_date_obj = datetime.strptime(from_date, "%m/%d/%Y")
            to_date_obj = datetime.strptime(to_date, "%m/%d/%Y")
            if to_date_obj < from_date_obj:
                print("Error: 'To date' cannot be earlier than 'From date'. Try again.")
                continue
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def input_employee_data():
    from_date, to_date = input_dates()
    name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    tax_rate = float(input("Enter income tax rate (e.g., 0.20 for 20%): "))
    return {
        "from_date": from_date,
        "to_date": to_date,
        "name": name,
        "hours_worked": hours_worked,
        "hourly_rate": hourly_rate,
        "tax_rate": tax_rate
    }

def calculate_payroll(employee):
    gross_pay = employee["hours_worked"] * employee["hourly_rate"]
    income_taxes = gross_pay * employee["tax_rate"]
    net_pay = gross_pay - income_taxes
    employee["gross_pay"] = gross_pay
    employee["income_taxes"] = income_taxes
    employee["net_pay"] = net_pay

def process_employee_data(employee_records):
    summary_data = {
        "total_employees": 0,
        "total_hours": 0.0,
        "total_income_taxes": 0.0,
        "total_net_pay": 0.0,
        "total_gross_pay": 0.0
    }

    for emp in employee_records:
        calculate_payroll(emp)
        print("\n--- Employee Payroll ---")
        print(f"From Date: {emp['from_date']}")
        print(f"To Date: {emp['to_date']}")
        print(f"Name: {emp['name']}")
        print(f"Hours Worked: {emp['hours_worked']}")
        print(f"Hourly Rate: ${emp['hourly_rate']:.2f}")
        print(f"Gross Pay: ${emp['gross_pay']:.2f}")
        print(f"Income Tax Rate: {emp['tax_rate']:.2f}")
        print(f"Income Taxes: ${emp['income_taxes']:.2f}")
        print(f"Net Pay: ${emp['net_pay']:.2f}")
        print("---------------------------------")

        summary_data["total_employees"] += 1
        summary_data["total_hours"] += emp["hours_worked"]
        summary_data["total_income_taxes"] += emp["income_taxes"]
        summary_data["total_net_pay"] += emp["net_pay"]
        summary_data["total_gross_pay"] += emp["gross_pay"]

    return summary_data

def display_summary_from_dict(summary_data):
    print("\n--- Payroll Summary ---")
    print(f"Total Employees: {summary_data['total_employees']}")
    print(f"Total Hours Worked: {summary_data['total_hours']}")
    print(f"Total Gross Pay: ${summary_data['total_gross_pay']:.2f}")
    print(f"Total Income Taxes: ${summary_data['total_income_taxes']:.2f}")
    print(f"Total Net Pay: ${summary_data['total_net_pay']:.2f}")
    print("-----------------------------------")

def main():
    employee_records = []
    while True:
        emp_data = input_employee_data()
        if emp_data:
            employee_records.append(emp_data)
        cont = input("Add another employee? (yes/no): ").strip().lower()
        if cont != "yes":
            break

    summary = process_employee_data(employee_records)
    display_summary_from_dict(summary)

if __name__ == "__main__":
    main()

