



k = float(input("Укажите свой обхват по бюсту "))
m = float(input("Укажите обхват по бедрам "))
n = float(input("Укажите обхват по талии "))
t = float(input("Укажите свой рост "))
p = float(input("Укажите вес в кг "))

l = (k*m*t)/(n**2*p)
if l >= 5:
    print(f"Your point by Landau {l} Вы ничешка!")
elif l <= 3.5 and l > 2:
    print(f"Your point by Landau {l} You are normal!")
elif l <= 2:
    print(f"Your point by Landau {l} Fat!") 
else:
    print(f"Your point by Landau {l} Who are you?!!!")

