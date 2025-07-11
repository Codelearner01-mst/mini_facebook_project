#What we need:
#The user posts
#The time the user posted
from helpers import get_current_time
from user_auth import  save_users


#Let make a class called post
def update_user_data(database , user_id , content , timestamp):
        
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
        
     
    def display_post(self,numbered_posts,post_index,file_name):
        #This logic works but it a bit unclear to me
        #Dont understand why it works
        selected=numbered_posts[post_index]
        for user_id,user_info in self.database.items():
           author_name=self.database[user_id]["name"]
           for post in user_info.get("posts", []):
             if post==selected:
               print(f"\nPost by {author_name} - {selected['timestamp']}\n {selected['content']} 👍{len(selected['likes'])} 🗨️{len(selected['comments'])}")
             
                       
class PostManager(Post):
    def __init__(self, content, author_id, database, timestamp, file_name):
        super().__init__(content, author_id, database, timestamp, file_name)

    def add_post(self, content=None, author_id=None, timestamp=None, file_name=None):
        if not content:
            content = input("Add post: ")
        if not timestamp:
            timestamp = get_current_time()
        user_post = update_user_data(self.database, author_id or self.author_id, content, timestamp)
        print("Post added!\n")
        save_users(self.database, file_name or self.filename)
        return user_post

    def show_all_posts(self, debug=False):
        all_posts = []
        numbered_posts = {}
        full_database = self.database
        if debug:
            print(f"All posts {all_posts}")
        for user_id, user in full_database.items():
            if debug:
                print("User", (user_id, user))
            for post in user.get("posts", []):
                all_posts.append((user_id, post))
        if debug:
            print(f"All posts {all_posts}")
        if not all_posts:
            print("No feed")
        print("\n-----All posts-----")
        for num, (user_id, post) in enumerate(all_posts, start=1):
            author_name = self.database[user_id]["name"]
            print(f"{num}. {author_name} - {post['content']} @ {post['timestamp']} ♥️{len(post['likes'])} 🗨️{len(post['comments'])}")
            numbered_posts[num] = post
        if debug:
            print(f"numbered posts{numbered_posts}")
        return numbered_posts


