'''
1.Combine strings and numbers with F_STRINGS
To specify a string as an f-string
simply put an f in front of the string literal
and add curly brackets {} as placeholders for variables and other operations.
'''

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)



'''
2.A modifier(修饰符) is included by adding a colon : 
followed by a legal formatting type
like .2f which means fixed point number with 2 decimals
'''
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)            #59.00


#3.math operations

txt = f"The price is {20 * 59} dollars"
print(txt)