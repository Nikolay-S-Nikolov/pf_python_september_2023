companies_employees_dict = {}
command = input()

while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_employees_dict.keys():
        companies_employees_dict[company_name] = []
    if employee_id not in companies_employees_dict[company_name]:
        companies_employees_dict[company_name].append(employee_id)
    command = input()
for company, employee in companies_employees_dict.items():
    print(company)
    for id in employee:
        print(f"-- {id}")
