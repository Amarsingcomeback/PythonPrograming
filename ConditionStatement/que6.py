# Python nested if-else statements
# count = 200

# if count < 400:
#     print('The count is below 400')
#     if count < 300:
#         print('The count is below 300')
#     else:
#         print('The count is less than 400 and greater than or equal to 300')

count = 200

if count < 400:
    print("The count is below 400")
    if count < 300:
        print("the count is below 300")
    elif count < 200:
        print("the count is below 200")
    else:
        print("the count is less then 400 and greater than or equal to 300 or 200")