from random import randint
import time
import os
class Profile:
    def __init__(self, **kwargs) -> None:
        self.first_name = kwargs.get('first_n')
        self.last_name = kwargs.get("last_n")
        self.email = kwargs.get("email_add")
        self.phone_num = kwargs.get("phone_n")
        self.address = kwargs.get("address")

    def display_profile(self):
        if "@gmail.com" in self.email and len(str(self.phone_num)) == 10:
            return f"""
            Name: {self.first_name + " " + self.last_name}
            Email: {self.email}
            Phone Number: {self.phone_num}
            Address: {self.address}
            """
        else:
            return"Must include @gmail.com or your phone number is incomplete"

if __name__=="__main__":
    print("Welcome to my class Banking System")
    print("press 1 to create a new account/ 2 to login for existing users")
    
    os.system("cls")
    time.sleep(2)
   
    try:
        user_response = int(input("Enter your choice: "))
        if user_response == 1:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            phone_num = int(input("Enter your phone number: "))
            my_address = input("Enter your address: ")
        elif user_response == 2:
            print("Proceed to login")
        else:
            print(" You have entered the wrong options. You can either select 1 or 2")
    except ValueError:
        print("Read the options again. This is not a valid Number")
    person1 = Profile(first_n = first_name, last_n =last_name, email_add = email, phone_n = phone_num, address = my_address)
    print(person1.display_profile())

        