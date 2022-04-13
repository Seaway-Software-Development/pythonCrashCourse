# David Wels
# userSignup.py
# 04/13/2022

print("\n\nUser Signup Application:")
print("------------------------")

fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")
email = input("Please enter your email address: ")

file = "user_signup.txt"

with open(file, 'a') as file_object:
	file_object.write('\nFirst Name: \t')
	file_object.write(fname.title())
	file_object.write('\nLast Name: \t')
	file_object.write(lname.title())
	file_object.write('\nEmail: \t\t')
	file_object.write(email.lower())
	file_object.write('\n_____________________________________________________\n')

print('#######################################')
print('Thank you for Signing Up', fname.title(), '!')
print('\nHave a great day!!')
