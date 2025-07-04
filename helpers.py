from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
    

def user_choice( selected_post):
    try:
        # selected_post is like "1", so convert to 0-based index
        index = int(selected_post) 
        return index
    except:
     #   print("Invalid post number.")
        return None

def select_post_from_lists():
    selected_post=input("Enter post number:")
    selected_index=user_choice( selected_post)
    return selected_index
     
def verifying(selected , user_post):
    return selected is None or selected < 0 or selected > len(user_post)
             #   return "Invalid post number"