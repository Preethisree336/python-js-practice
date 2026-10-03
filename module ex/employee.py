def calculate_salary(basic,bonus):
    return basic + bonus
def display_employee(name,basic,bonus):
    total = calculate_salary(basic,bonus)
    print("Employee:",name)
    
    print("Total salary:",total)
