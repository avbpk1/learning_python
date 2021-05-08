# Accept Basic Salary and Calculate Gross
basic_salary = int(input("Please Enter Basic Salary:"))
hra = basic_salary * 0.3
da = basic_salary * 0.2
pf = basic_salary * 0.02
net_salary = hra + da - pf
print(f"Basic Salary        : {basic_salary}")
print(f"HRA at 30% of Basic Salary:{hra}")
print(f"DA at 20% of Basic Salary :{da}")
print(f"PF at 2% of Basic Salary  :{pf} ")
print(f"Gross Salary              :{basic_salary + net_salary}")
