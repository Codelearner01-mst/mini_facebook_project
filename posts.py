#What we need:
#The user posts
#The time the user posted
import json
from helpers import get_current_time
from datetime import datetime 
from User_data import  save_users,load_users,user_database


#Let make a class called post
def update_user_data(database , user_id , content , timestamp,file_name):
        
       main_data=database[user_id]
       if "posts" not in main_data:
           main_data["posts"]=[]
       new_post= {"content": content , "timestamp": timestamp,  "likes":[], "comments":[] }
       main_data["posts"].append(new_post) 
                                
       return new_post
       
class Post:
    def __init__(self , content, author_id , database , timestamp,file_name):
        self.content=content 
        self.author_id=author_id
        self.database=database
        self.timestamp = timestamp
 
        self.filename=file_name
        
     
    def display_post(self):
        print(f"{self.timestamp}: {self.author_id}.{self.content}")
        
class Postmanager(Post):
    def __init__(self,content, author_id, database , timestamp,file_name):
          super().__init__(content, author_id , database, timestamp,file_name)
                    
    def add_post(self , content, author_id, timestamp,file_name):
         timestamp=get_current_time()
         print("Database",self.database)              
         content=input("Add post:") 
         user_post=update_user_data(self.database , author_id , content, timestamp,file_name)  
         print(f"Type of database: {type(self.database)}")
         print(f"keys in database:{list(self.database.keys())}") 
         
         if file_name:
          try:
              save_users(self.database,file_name)
          except TypeError as e:
              print("JSON error:",e)

                  
         print("Post added!\n")
         save_users(self.database , file_name) 
         
         return user_post
         
         
        
         
    def show_all_posts(self):
         all_posts=[]
         numbered_posts={}      
      
         full_database=self.database
         for user_id, user in full_database.items():
             print("User" , (user_id,user) )          
             for post in user.get("posts", []):     
                 all_posts.append((user_id , post))
        
         if not all_posts:
              print("No feed")
              print(full_database)
         
         print("\n-----All posts-----")
         for num, (user_id, post) in enumerate(all_posts, start=1):
             author_name=self.database[user_id]["name"]
                              
             print(f"{num}. {author_name} - {post['content']} @ {post['timestamp']} ♥️{len(post['likes'])} 🗨️{len(post['comments'])}")
             numbered_posts[num]=post
         
         
         
            
           
         return numbered_posts
                     

         