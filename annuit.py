k = float(input("Enter summ of credit "))
p = float(input("Enter interest rate "))
m = float(input("Enter month count "))

print(int(k*0.01*p*(1 + 0.01*p)**m/((1 +0.01*p)**m-1)))