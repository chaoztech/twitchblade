def print_home_page():
	print("|----------------------------------------------------|")
	print("|        Welcome to TwitchBlade CLI application      |")
	print("|----------------------------------------------------|")

	print("1. For signup")
	print("2. for signin")


def user_choice(num):
   if num == 1:
      return display_signup_page()
   elif num == 2:
      return display_signin_page()
   else:
      return "Please enter the correct choice"


def display_signup_page():
	print("Singup Page")

def display_signin_page():
	print("SignIn Page")

if __name__ == "__main__":
    print_home_page()
    while True:
      num = int(input("Enter your choice - "))
      print(user_choice(num))
