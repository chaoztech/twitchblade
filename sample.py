
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
	user
	print("|----------------------------------------------------|")
	print("|                   Signup Page                      |")
	print("|----------------------------------------------------|")

	
	username = input("Enter Username- ")
	password = input("Enter Password- ")
	print("Successfully Signed Up!", username)
	
	a=[]
	user_info_up=[username,password]
	a=append(user_info_up)
	count+=1
	print("DB till now",a)
	
	
	

def display_signin_page():
	
	print("|----------------------------------------------------|")
	print("|                   Signin Page                      |")
	print("|----------------------------------------------------|")

	username = input("Enter Username- ")
	password = input("Enter Password- ")

	b=[]
	user_info_in=[username,password]
	for i in range(count)
		for j in range(count)
			if(user_info_in[i][j]==user_info_up[i][j])
				print("Successfully Signed In with ", username)
			else
				print("Either Username or password is incorrect  OR The username doesn't exist")
	
	#print("Successfully Signed In with ", username)

if __name__ == "__main__":
    print_home_page()
    while True:
      num = int(input("Enter your choice - "))
      print(user_choice(num))