# Define the employee data as a list of dictionaries
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

# Function to print the employee data
def print_employee_data(data):
    print("Employee ID\tName\tAge\tSalary (PM)")
    for employee in data:
        print(f"{employee['Employee ID']}\t{employee['Name']}\t{employee['Age']}\t{employee['Salary (PM)']}")

# Function to sort the employee data based on user's choice
def sort_employee_data(data, key):
    return sorted(data, key=lambda x: x[key])

# Main program
print("Choose sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    sorted_data = sort_employee_data(employee_data, "Age")
elif choice == 2:
    sorted_data = sort_employee_data(employee_data, "Name")
elif choice == 3:
    sorted_data = sort_employee_data(employee_data, "Salary (PM)")
else:
    print("Invalid choice")
    exit()

print("\nSorted Employee Data:")
print_employee_data(sorted_data)