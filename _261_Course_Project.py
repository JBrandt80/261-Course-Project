# Jeffrey Brandt
# CIS261
# Course Project Phase 1 - Create and Call Functions with Parameters

def main():
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

def get_employee_name():
    name = input('Enter employee name (or "End" to terminate): ')
    return name

def get_hours_worked():
    while True:
        try:
            hours = float(input('Enter hours worked: '))
            if hours >= 0:
                return hours
            else:
                print("Hours worked cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_hourly_rate():
    while True:
        try:
            rate = float(input('Enter hourly rate: '))
            return rate
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_income_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter income taxe rate (e.g., 0.20 for 20%): "))
            return tax_rate
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_pay(hours_worked, hourly_rate, tax_rate):
    gross_pay = hours_worked * hourly_rate
    income_taxes = gross_pay * tax_rate
    net_pay = gross_pay - income_taxes
    return gross_pay, income_taxes, net_pay

def display_employee_details(name, hours_worked, hourly_rate, gross_pay, tax_rate, income_taxes, net_pay):
    print("\n--- Payroll Details ---")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2f}")
    print(f"Income Taxes: ${income_taxes:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")
    print("---------------------------------")

def display_summary(total_employees, total_hours, total_gross_pay, total_income_taxes, total_net_pay):
    print("\n--- Payroll Summary ---")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Income Taxes: ${total_income_taxes:.2f}")
    print(f"Total Net Pay: ${total_net_pay:.2f}")
    print("-----------------------------------")

def main():
    total_employees = 0
    total_hours = 0.0
    total_gross_pay = 0.0
    total_income_taxes = 0.0
    total_net_pay = 0.0

    while True:
        name = get_employee_name()
        if name.strip().lower() == "end":
            break

        hours_worked = get_hours_worked()
        hourly_rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()

        gross_pay, income_taxes, net_pay = calculate_pay(hours_worked, hourly_rate, tax_rate)
        display_employee_details(name, hours_worked, hourly_rate, gross_pay, tax_rate, income_taxes, net_pay)

        total_employees += 1
        total_hours += hours_worked
        total_gross_pay += gross_pay
        total_income_taxes += income_taxes
        total_net_pay += net_pay

    display_summary(total_employees, total_hours, total_gross_pay, total_income_taxes, total_net_pay)

if __name__ == "__main__":
    main()

