salary = float(input("Enter basic salary: "))

hra = 0.10 * salary
da = 0.05 * salary
gross = salary + hra + da

print("Gross Salary:", gross)
