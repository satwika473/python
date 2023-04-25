salary=int(input("Enter your salary"))
gender=input("Enter your gender")
if(salary<10000):
              if(gender=="female"):
                  bonus=salary*(12/100)
                  salary=salary+bonus
                  print("Your salary is",salary)
                  print("your bonus is",bonus)
              if(gender=="male"):
                  bonus=salary*(7/100)
                  salary=salary+bonus
                  print("your salary is",salary)
                  print("your bonus is",bonus)
else:
               if(gender=="female"):
                   bonus=salary*(10/100)
                   salary=salary+bonus
                   print("your bonus is",bonus)
                   print("your salary is",salary)
               if(gender=="male"):
                   bonus=salary*(5/100)
                   salary=salary+bonus
                   print("your bonus is",bonus)
                   print("your salary is",salary)
                
