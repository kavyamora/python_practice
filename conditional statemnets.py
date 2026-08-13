'''
control statements
     conditional statements
           1-If
           2-else
           3-elif
           4-nested if
'''
'''
if statement
   syntax: if condition
                 statement
        else:
             statement
'''
# age=18
# if age>18:
#  print("you can vote")
# elif age==18:
#     print("you cannot vote")
# else:
#     print("you can vote next time")

'''
nested if 
syntax:
     if condition
        statement
        if condition
         statement
'''

# if True:
#    print("eligible for voting") 
#    if False:
#        print("not eligible for voting") 


'''
conditional statements with logical operator
 syntax: 
    if condition and/or condition
       statemnent
    else:
        statement
        '''
age=20
if age>18 and age==19:
  print("eligible for voting")
else:
    print("not eligible for voting")
