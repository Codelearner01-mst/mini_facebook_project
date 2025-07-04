# ------------------------------
# Account Creation (Sign Up)
# ------------------------------
# Fields required to create a new user:
# - Name
# - Date of Birth
# - Gender
# - Phone Number
# - Password
# These details will be stored in the database (or a file for now).

# ------------------------------
# Sign In
# ------------------------------
# User provides:
# - Phone Number
# - Password
# We check if these match stored data.

# ------------------------------
# Forgot Password
# ------------------------------
# If user forgets password:
# - System sends a reset code
# - User enters new password
# - We update their stored password
from datetime import datetime
import hashlib
import json
#import os

DEFAULT_DB="main_db.json"

def reset_database():
    with open("main_db.json", "w") as f:
        json.dump({}, f)
    print("✅ Database reset successfully!")

#reset_database()
#Creating JSON to load file
def load_users(file_name=DEFAULT_DB):
    #print(f"Using load_users from: {os.path.abspath(file_name)}")
    try:
        with open(file_name , "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return {}
            
#Creating JSON to save file
def save_users(database , file_name=DEFAULT_DB):
        with open(file_name , "w") as f:
            json.dump(database, f , indent=4)        
        

#Creating function to check validation when collecting user info
def validation_input(prompt , validation_func , error_message):
    while True:
        user_input=input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)
            
            
#function to check date of birth
def validate_dob(dob_str):
   try:
       dob=datetime.strptime(dob_str , "%Y-%m-%d")
       return dob
   except ValueError:
       return None

    
#Using password hashing for security
def password_hashing(password):
      return hashlib.sha256(password.encode()).hexdigest()
 

#Collecting user phone number
def input_phone():
   return validation_input("\nEnter phone number:" , lambda x: x.isdigit() and len(x)==10 , "Phone number should be exactly 10 digits and only contain numbers.")

  
#Collecting user name
def input_name():   
   return validation_input("Enter your name:" , lambda x: len(x)>0, "Name cannot be empty")


#Collecting user date of birth     
def input_dob():
   return validation_input("Enter your date of birth (YYYY-MM-DD): ", validate_dob , "Invalid date format. Please use YYYY-MM-DD (like 2004-06-25).")


#Collecting user gender type
def input_gender():    
   return validation_input("Choose your gender(1.Male 2.Female):" , lambda x: x=="1"or x=="2" , "Please choose from options(1.Male 2.Female).")


#Collecting user password
def input_password():   
   return validation_input("Enter your password (at least 8 characters): ", lambda x: len(x) >= 8  , "Password should be at least 8 characters")


#Check if phone alredy exist
def user_exist(database , phone):
       return phone in database
  
#Make sure all variables are defined before using them
#content = "My first post!"
#timestamp = "2025-06-04 15:00"
#user = "0535750228"
#text = "Great post!"
#time = "2025-06-04 15:05"

#Storing user info in database            
def user_database(database ,phone , name , dob , gender , password_hash):
   database[phone] = {
    "name": name,
    "dob": dob,
    "gender": gender,
    "hash_password": password_hash,
    "friends": [],
    "friend_requests": [] ,
    "sent_requests": [],
    "posts": []
                        }
                    
    # return database[phone]
  
   save_users(database , DEFAULT_DB)
   print(json.dumps(database, indent=4))
   
             
#Checking user authentification   
def  authenticate_user(database , phone , password):
        if phone not in database:
            return False , "Phone number not registered" 
        if database[phone]["hash_password"] != password_hashing(password):
            return False , "Incorrect password"
   
        return True , f"Welcome back, {database[phone]['name']}! "        

#Creating sign up flow
def sign_up_flow():
   while True:
     print("-------Sign up-------")
     database=load_users(DEFAULT_DB)             
     phone=input_phone()
     if user_exist(database , phone):
             print("Phone number already exist")
             continue 
     
     name=input_name()
     dob=input_dob()
     gender=input_gender()
     password=input_password()
     password_hash=password_hashing(password)
     
     user_database(database ,phone , name , dob , gender , password_hash)
     print("Account created successfully!") 

     return phone , database 
   

   

#Creating sign in flow
def sign_in():
    print("\n-----Sign in-----")
    database=load_users(DEFAULT_DB)      
    print("Forgot password")
    while True:
        phone=input_phone()
        password=input("Enter password:")
    
        success , message=authenticate_user(database , phone , password)
        if success==False:
            print(message)
            continue     
        print(message)
        print(database)
        return phone , database
 
                       
#This function is to create user profile  
def display_user_profile(database , phone ):
    print(database[phone])
    user=database[phone]
    print("\n-----User profile------")
    print(f"Phone: {phone}")
    print(f"Name: {user['name']}")
    print(f"Date of birth: {user['dob']}")
    print(f"Gender: {'Male' if user['gender']=='1' else 'Female'}")    


def change_name(phone):
    database=load_users(DEFAULT_DB)
    new_name=input_name()
    database[phone]["name"]=new_name
    save_users(database)
    print("Name updated successfully")

         

    
        
        

  

  
              

      