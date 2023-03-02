# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid.')
#     finally:
#         n_square = n ** 2
#         return n_square

# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid. Using default value 0')
#         n = 0
#     else:
#         n_square = n ** 2
#         return n_square


# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid. Using default value 0')
#         n = 0
#     else:
#         n_square = n ** 2
#     finally:
#         return n_square


# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid. Using default value 0')
#         return 0
#     finally:
#         n_square = n ** 2
#         return n_square


# # this worked for me but is not the preferred way to do this
# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid. Using default value 0')
#         n = 0
#     finally:
#         n_square = n ** 2
#         return n_square
    

# this is the instructors preferred code
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0.0
    else:
        n_square = n ** 2
        return n_square

print(power_of_two())
print(power_of_two())