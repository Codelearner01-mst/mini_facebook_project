from user_auth import  save_users



class Likes:
    def __init__(self , owner_id , user_id,database,file_name):
        self.owner_id=owner_id
        self.user_id=user_id
        self.database=database
        self.file_name=file_name
       
    def add_remove_like(self ,numbered_posts, post_index,file_name ):
        selected=numbered_posts[post_index]    
        if self.user_id not in selected["likes"]:
            selected["likes"].append(self.user_id)
            print(f"♥️{len(selected['likes'])} Liked")
        else:
            if self.user_id in selected["likes"]:
               selected["likes"].remove(self.user_id) 
               print(f"♥️{len(selected['likes'])} remove like")
        
        save_users(self.database,file_name)        
            
   