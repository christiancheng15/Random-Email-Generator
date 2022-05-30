import names
import random

def random_numbers():
       random_numbers = (''.join(str(random.randint(0,9)) for i in range(3)))
       return random_numbers

def random_first_name():
	return names.get_first_name()

def random_last_name():
	return names.get_last_name()

with open('domain.txt', 'r') as f:
    catchall = [line.strip() for line in f]

num_emails = input("Number of emails: ")
num_emails = int(num_emails)
num_catchall = len(catchall)

if num_emails < num_catchall:
       multiplyer = 1
       catchall_list = catchall * multiplyer
       catchall_list = catchall_list[0:num_emails]
else:
       multiplyer = num_emails//num_catchall + 1
       catchall_list = catchall * multiplyer
       catchall_list = catchall_list[0:num_emails]

for email in catchall_list:
       generated_email = f"{random_first_name()}{random_last_name()}{random_numbers()}@{email}"
       with open('firstname.txt', 'a') as f:
              f.write(f"{generated_email}\n")

print(f"Successfully generated {num_emails} emails")
input("Press ENTER to close")