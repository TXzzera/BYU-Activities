#A student makes honour roll if their average is >=85
#and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour roll')
else:
    print('You did not got the honour roll, try again next year. ')

gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
if honour_roll:
    print('You made honour roll')

print("For each of these questions, please provide a rating of 1-10: ")
loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))   
down_payment = int(input("How large is your down payment? "))

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
      should_loan = True
    elif credit_history >= 7 and income >= 7:
      if down_payment >= 5:
        should_loan = True
      else:
        should_loan = False
    else:
      should_loan = False
else:
  if credit_history < 4:
    should_loan = False
  else:
    if income >= 7 or down_payment >= 7:
      should_loan = True
    elif income >= 4 and down_payment >= 4:
      should_loan = True
    else:
      should_loan = False

if should_loan:
  print("I can loan to you bro")
else:
  print("I can not loan to you bro, sorry")



         
                           