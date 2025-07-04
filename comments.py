
from datetime import datetime
from user_auth import save_users  ,load_users
from helpers import get_current_time
 
class Comments:
    def __init__(self , owner_id ,user_id, timestamp ,database):
        self.owner_id=owner_id
        self.user_id=user_id
        self.database=database
        self.timestamp=timestamp 
        
    def display_user_comment(self , post_index , comment_index):
        comment=self.database[self.owner_id]["posts"][post_index]["comments"][comment_index]
        user_name=self.database[comment['name'] ]
        print(f"comment by {user_name}: {comment['text']} ")
        
        
class CommentsManager:
    def __init__(self, comments, file_name,database ):
      self.comments=comments
      self.file_name=file_name 
      self.database = comments.database

    def add_comment(self ,numbered_posts,post_index,file_name):
         self.comments.timestamp=get_current_time() 
         user_name=self.database[self.comments.user_id]["name"]
         
         selected=numbered_posts[post_index]
         
         text=input("Write comment:")
         selected["comments"].append({"user":user_name,
                 "text":text,
                 "time":get_current_time() } )
         print("Comment added")
         save_users(self.database,file_name)
         
    def show_all_comments(self ,numbered_posts, post_index):
        selected=numbered_posts[post_index]    
        
        comments=selected["comments"]
        if not comments:
            print("No comments")
            return
            
        print("Comments")
        for i , comment in enumerate(comments, start=1):
             #numbered_comments={i: comment}
             
           
             print(f"{i}.{comment['user']} commented at ⏲️{comment['time']}\n{comment['text']}")
        
             
