from user_auth import sign_up_flow, sign_in, display_user_profile,change_name , DEFAULT_DB
from helpers import select_post_from_lists, verifying
from options import main_options,home_options, friends_options, settings_options
from Likes import Likes
from posts import Post , Postmanager
from comments import Comments, CommentsManager 
from friends import accept_or_decline_request,send_friend_request, display_friends
file_name=DEFAULT_DB

def verify_user_selection(selected_from):
     while True:
         selected=select_post_from_lists()  
         if verifying(selected, selected_from):
             print("\nInvalid post number")
             continue 
         return selected


content="Hello world"
timestamp="2:00"

def show_home(phone , database):
       manager=Postmanager(content , phone , database, timestamp,file_name)
       numbered_posts=manager.show_all_posts()
       

       posts_interaction(phone , database, numbered_posts)
                                           
def add_content(phone , database):
       manager=Postmanager(content , phone , database, timestamp,file_name)
       manager.add_post(content, phone,timestamp,file_name)   
 
               
def like_post(phone , database ,numbered_posts):
   
       likes=Likes(phone , phone , database,file_name)
       selected=verify_user_selection(numbered_posts)
                 
       likes.add_like(numbered_posts,selected,file_name)

             
                                       
def comment_on_post(phone , database, numbered_posts):
     comment_details=Comments(phone, phone , timestamp, database)    
     handle_comment=CommentsManager(comment_details, file_name,database)
     selected=verify_user_selection(numbered_posts) 
     handle_comment.add_comment(numbered_posts,selected,file_name)
                                                                             
def comment_section(phone , database,numbered_posts):
     comment_details=Comments(phone, phone , timestamp,database)    
     handle_comment=CommentsManager(comment_details, file_name,database) 
     selected=verify_user_selection(numbered_posts)    
     handle_comment.show_all_comments(numbered_posts,selected)                   
                                                                            
                                                                                                                                                                    
def account_interaction():
    print("  Welcome to facebook  ")
    print("_"*22)
    while True:
        print("\n1.Create new account\n2.Sign in")
        option=input("Enter choice:")
    
        if option=="1":
            phone,database=sign_up_flow()
            main_interaction(phone , database,file_name)
            break
    
        elif option=="2":
            phone , database=sign_in()
            main_interaction(phone , database,file_name)       
            break 
        else:
            print("Invalid choice")
        
        
def main_interaction(phone , database , file_name):
    while True:
        main_options()
        choice=input("Enter choice:")
        if choice=="4":
             account_interaction()  
        if choice=="1":
             show_home(phone , database)  
              
        elif choice=="2":
              friends_interaction(phone,database, file_name)
        
        elif choice=="3":
              settings_interaction(phone, database)
         
        else:
                print ("Invalid choice ")

                                            
def posts_interaction(phone, database, numbered_posts):
     while True:
         home_options()
         choice=input("Enter your choice:")
         if choice=="5":
             return 
             
         if choice=="1":
             add_content(phone , database)      
               
         elif choice=="2":
             like_post(phone , database , numbered_posts)
         elif choice=="3":
             comment_on_post(phone , database, numbered_posts)
         elif choice=="4":
              comment_section(phone , database , numbered_posts)

                      
              
def friends_interaction(phone,database, file_name):
  while True:
    friends_options()
    choice=input("Enter choice:")
    if choice=="4":
       return 
    if choice=="1":
        display_friends(database,phone)
    elif choice=="2":
        accept_or_decline_request(phone,database, file_name )
    elif choice=="3":
        send_friend_request(phone ,file_name)


  

def settings_interaction(phone, database):
    while True:
       settings_options()
       choice=input("Enter:")       
       if choice=="3":
           return 
       if choice=="1":
           display_user_profile(database , phone )
       elif choice=="2":
          change_name(phone)
           
account_interaction()                                
               
      
  
         
                