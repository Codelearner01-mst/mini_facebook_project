import json
import os
from datetime import datetime
from user_auth import  save_users,load_users


# Dictionary to store each user's friends list
# Example: friends["12345"] = ["67890", "54321"]

# Dictionary to store friend requests each user has received
# Example: friend_requests["12345"] = ["67890"]

# Dictionary to store confirmed friends for each user
# (This can be the same as friends or handled separately if needed)

# Dictionary to store friend requests each user has sent
# Example: sent_requests["12345"] = ["67890"]


def numbering_func(user_list):
    #This fuction creates numbering lists e.g.{1:"Paul" , 2:"John Doe"}
    return {str(i+1): user for i , user in enumerate(user_list)}
    
def user_choice(numbered_results , pick):
    #Get 
    return numbered_results.get(pick)

def friend_exist(database , phone ,friend):
    #Checking if friend in user friends list or sent_request and confirmed it later in "get_suggested_friends function"
    
    return friend in database[phone]["friends"]  
    
def has_sent_request(database , phone , friend):
    #-Checking if friend in user sent request list and confirmed it later in "get_suggested_friends function"
    
    return friend in database[phone]["sent_requests"]
    
def get_suggested_friends(database, user_id):
     #Filter out suggested friends(excluding already friends , sent request )
     all_users=[str(user).strip() for user in database if user !=user_id]
     suggested=[user for user in all_users if not friend_exist(database , user_id ,user) and not has_sent_request(database , user_id , user)]
     
     return suggested
     
def display_user_list(database , user_ids):
    #This function display user list by numbers e.g. 1. Paul  2.John Doe
    #we pass any list to display, as an argument in user_ids parameter
    numbered=numbering_func(user_ids)
    for num , user in numbered.items():
           print(f"{num}. {database[user]['name']}")
    return numbered    
   


def select_friend_to_send_request(numbered_list):
     choice=input("Choose friend to send request:")
     return user_choice(numbered_list , choice )


def update_friend_requests(database , sender , receiver):
    #Updates database after user sent friend request
    if receiver not in database[sender]["sent_requests"]:
        database[sender]["sent_requests"].append(receiver)
        
    if sender not in database[receiver]["friend_requests"]:
        database[receiver]["friend_requests"].append(sender)
        
        
def send_friend_request(phone ,file_name):
    database=load_users(file_name)
    suggestions=get_suggested_friends(database , phone)
    if not suggestions:
        print("No new friend to suggest")
        return
    print("Suggested friends:")
    numbered=display_user_list(database , suggestions)     
    selected=select_friend_to_send_request(numbered)
    
    if not selected:
        print("invalid choice")
        return
          
    update_friend_requests(database ,phone , selected)
             
    save_users(database , file_name)
    print(f"Friend request sent to {database[selected]['name']}")


def select_friend_from_requests(numbered_requests,choice,decision):
    select_friend=input(f"Choose friend {decision[choice]} request:")
    return user_choice(numbered_requests , select_friend)
    


#This function get request list    
def get_friend_requests(database ,phone):
    #Get received friend requests from the database
    get_all_requests=database[phone]["friend_requests"]
    return get_all_requests

 
#function to accept request
def update_accepted_request(database , phone , request_id):
    if request_id not in database[phone]["friends"]:
        database[phone]["friends"].append(request_id)

    if request_id in database[phone]["friend_requests"]:
        database[phone]["friend_requests"].remove(request_id)

    if phone not in database[request_id]["friends"]:
        database[request_id]["friends"].append(phone)
              

#function to decline request   
def update_declined_request(database , phone , request_id):
    if request_id in database[phone]["friend_requests"]:
        database[phone]["friend_requests"].remove(request_id)

    if phone in database[request_id].get("sent_requests" ,[] ):
        database[request_id]["sent_requests"].remove(phone)
              
              

    
      
def update_requests(database, phone , request_id , action):
      if action=="accept":
          update_accepted_request(database , phone , request_id)

          print(f"✅ Accepted request from {request_id}")
              
              
      elif action=="decline":
              update_declined_request(database , phone , request_id)
                      
              print(f"❌ Declined request from {request_id}")
             
              
                   
def accept_or_decline_request(phone,database, file_name ):
      database=load_users(file_name)
      friend_requests=get_friend_requests(database ,phone)
      if not friend_requests:
          print("You have no friend requests")
          return
          
      print("Friend requests:")
      numbered_requests=display_user_list(database , friend_requests)
      decision={"1":"accept" , "2":"Decline"}    
      
      while True:
         print("\n1.Accept request\n2.Decline request\n3.Back")
         choice=input("Enter choice:")
  
         if choice=="3":
            return
            
         if choice not in decision:
            print("Invalid choice.Please try again")
            continue
         selected=select_friend_from_requests(numbered_requests,choice,decision)

         if not selected:
              print("Invalid request number")
              continue 
              
         action=decision[choice]
        
         update_requests(database, phone , selected , action) 
         break        
            
      save_users(database , file_name)
    

 def display_friends(database,phone):
    get_friends=database[phone].get("friends",[])
    if not get_friends:
        print("You have no friends")
        return
    for num,friend in enumerate(get_friends,start=1):
        print(f"{num} - {friend}")
