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

#database={}

DB_FILE="user_db.json"

#Creating JSON to load file
def load_users():
    try:
        with open(DB_FILE , "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return {}
            
#Creating JSON to save file
def save_users(database):
        with open(DB_FILE , "w") as f:
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
  

#Storing user info in database            
def user_database(database ,phone , name , dob , gender , password_hash):
   database[phone]={"name":name ,
  "dob":dob , 
  "gender":gender,
  "hash_password":password_hash ,}
  
   save_users(database)
   
             
#Checking user authentification   
def  authenticate_user(database , phone , password):
        if phone not in database:
            return False , "Phone number not registered" 
        if database[phone]["hash_password"] != password_hashing(password):
            return False , "Incorrect password"
   
        return True , f"Welcome back, {database[phone]['name']}! "        

#Creating sign up flow
def sign_up_flow():
     print("-------Sign up-------")
     database=load_users()             
     phone=input_phone()
     if user_exist(database , phone):
          print("Phone number alredy exist")
          return
         
     
     name=input_name()
     dob=input_dob()
     gender=input_gender()
     password=input_password()
     password_hash=password_hashing(password)
     
     user_database(database ,phone , name , dob , gender , password_hash)
     print("Account created successfully!") 

sign_up_flow()     

#Creating sign in flow
def sign_in():
    print("\n-----Sign in-----")
    database=load_users()
    print("Forgot password")
    while True:
        phone=input_phone()
        password=input("Enter password:")
    
        success , message=authenticate_user(database , phone , password)
        print(message)
        if success:
            display_user_profile(database , phone )
            break
    change_name(database , phone)    
            
            
#This function is to create user profile  
def display_user_profile(database , phone ):
    user=database[phone]
    print("\n-----User profile------")
    print(f"Phone: {phone}")
    print(f"Name: {user['name']}")
    print(f"Date of birth: {user['dob']}")
    print(f"Gender: {'Male' if user['gender']=='1' else 'Female'}")    


def change_name(database , phone):
    database=load_users()
    new_name=input_name()
    database[phone]["name"]=new_name
    save_users(database)
    print("Name updated successfully")

         
sign_in() 
    

    
    
    
    
        
        

  

  
              

      