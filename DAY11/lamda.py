# # LAMBDA FUNCTION IN PYTHON

# 1. Lambda kya hota hai?
# Lambda ek small anonymous function hota hai.
# Iska naam nahi hota aur ye single expression mein likha jata hai.

# 2. Normal function:
# def add(a, b):
#     return a + b

# 3. Same function using Lambda:
# add = lambda a, b: a + b
# print(add(10, 20))   Output: 30

# 4. Lambda syntax:
#
# # LAMBDA FUNCTION IN PYTHON
#
# # 1. Lambda kya hota hai?
# # Lambda ek small anonymous function hota hai.
# # Iska naam nahi hota aur ye single expression mein likha jata hai.
#
# # 2. Normal function:
# def add(a, b):
#     return a + b
#
# # 3. Same function using Lambda:
# add = lambda a, b: a + b
# print(add(10, 20))  # Output: 30
#
# # 4. Lambda syntax:
# # lambda arguments: expression
#
# # 5. Playwright mein Lambda ka use:
#
# page.on("dialog", lambda dialog: dialog.accept())
# # Dialog event aane par automatically OK click karega.
#
# # 6. Important:
# # lambda = Chhota function
# # dialog = Function ka parameter
# # dialog.accept() = Dialog par OK click karta hai

# 5. Playwright mein Lambda ka use:

# page.on("dialog", lambda dialog: dialog.accept())
# Dialog event aane par automatically OK click karega.

# 6. Important:
# lambda = Chhota function
# dialog = Function ka parameter
# dialog.accept() = Dialog par OK click karta hai

####################################################################################################################################################
# syntax   lambda arguments: expression

# normal

def sum(a):
    print(a+10)
sum(100)            # 110



# through lambda key

x = lambda a:a+10     # here-   lamda = key,   a = parameter,   a+10 = expression
print(x(100))

# Another example

x = lambda a,b,c: a+b+c
print(x(100,100,100))       # 300

