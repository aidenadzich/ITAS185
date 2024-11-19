import Employee as e

employee_one = e.Employee()
employee_one.emp_name = "Kay Oss"
employee_one.id_number = 47899
employee_one.department = "Accounting"
employee_one.position = "Vice President"

employee_two = e.Employee()
employee_two.emp_name = "Ben Dover"
employee_two.id_number = 39119
employee_two.department = "IT"
employee_two.position = "Programmer"

employee_three = e.Employee()
employee_three.emp_name = "Al E. Gator"
employee_three.id_number = 81774
employee_three.department = "Manufacturing"
employee_three.position = "Engineer"

print(employee_one.get_info())
print(employee_two.get_info())
print(employee_three.get_info())