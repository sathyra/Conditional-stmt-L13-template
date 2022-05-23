
#if statement
marks_1 = 40
marks_2 = 45
if(marks_1 + marks_2 < 100):
  print("Total marks is less than 100. Condition is true.")

#else statement
  marks_1 = 95
marks_2 = 45
if(marks_1 + marks_2 < 100):
  print("Total marks is less than 100. Condition is true.")
else: 
  print("Total marks is not less than 100. Else Condition is true.")


# Elif
  theory_points = 30
practical_points = 20

if(theory_points > 50):
    print("input points for 'Theory' is correct.") 
elif(practical_points > 50):
    print("input points for 'Practical' is correct.")  
else:
    print("Points validated. Your total is: ",practical_points + theory_points)