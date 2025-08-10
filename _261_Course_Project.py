# Jeffrey Brandt
# CIS261
# Course Project Phase 3 - Using Files to Store and Retrieve Data
 
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

def clear_file(filename):
    open(filename, "w").close()

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

def write_to_file(filename, from_date, to_date, name, hours, rate, tax):
    with open(filename, "a") as file:
        record = f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax}\n"
        file.write(record)

def read_and_process_file(filename="employee_data.txt"):
    from_date_filter = input("Enter FROM date to filter (mm/dd/yyyy) or 'All':").strip()
    if from_date_filter.lower() != "all":
        try:
            datetime.strptime(from_date_filter, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format.")
            return

    summary = {
        "total_employees": 0,
        "total_hours": 0.0,
        "total_income_taxes": 0.0,
        "total_net_pay": 0.0,
        "total_gross_pay": 0.0
    }

    try:
        with open(filename, "r") as file:
            for line in file:
                fields = line.strip().split("|")
                if len(fields) != 6:
                    continue
                
                from_date, to_date, name, hours, rate, tax = fields
                if from_date_filter.lower() != "all" and from_date != from_date_filter:
                    continue
                   
                hours = float(hours)
                rate = float(rate)
                tax = float(tax)
                gross = hours * rate
                income_tax = gross * tax
                net = gross - income_tax

                print("\n--- Employee Payroll ---")
                print(f"From Date: {from_date}")
                print(f"To Date: {to_date}")
                print(f"Name: {name}")
                print(f"Hours Worked: {hours}")
                print(f"Hourly Rate: ${rate:.2f}")
                print(f"Gross Pay: ${gross:.2f}")
                print(f"Income Tax Rate: {tax:.2f}")
                print(f"Income Taxes: ${income_tax:.2f}")
                print(f"Net Pay: ${net:.2f}")
                print("---------------------------------")

                summary["total_employees"] += 1
                summary["total_hours"] += hours
                summary["total_income_taxes"] += income_tax
                summary["total_net_pay"] += net
                summary["total_gross_pay"] += gross
    except FileNotFoundError:
        print("No data file found.")

    display_summary(summary)

def display_summary(summary):
    print("\n--- Payroll Summary ---")
    print(f"Total Employees: {summary['total_employees']}")
    print(f"Total Hours Worked: {summary['total_hours']}")
    print(f"Total Gross Pay: ${summary['total_gross_pay']:.2f}")
    print(f"Total Income Taxes: ${summary['total_income_taxes']:.2f}")
    print(f"Total Net Pay: ${summary['total_net_pay']:.2f}")
    print("-----------------------------------")

def main():
    filename = "employee_data.txt"
    mode = input("Start fresh or append to existing data? (fresh/append): ").strip().lower()
    if mode == "fresh":
        clear_file(filename)

    while True:
        from_date = input("Enter From Date (mm/dd/yyyy): ")
        to_date = input("Enter To Date (mm/dd/yyyy): ")
        name = input("Enter employee Name: ")
        hours = float(input("Enter Hours Worked: "))
        rate = float(input("Enter Hourly Rate: "))
        tax = float(input("Enter Income Tax Rate (e.g., 0.20 for 20%): "))

        write_to_file(filename, from_date, to_date, name, hours, rate, tax)

        cont = input("Add another employee? (yes/no): ").strip().lower()
        if cont != "yes":
            break
   
    read_and_process_file(filename)

if __name__ == "__main__":
    main()

