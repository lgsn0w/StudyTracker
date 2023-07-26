current_user = None
start_time = None

def set_current_user(username):
    global current_user
    current_user = username

def get_current_user():
    global current_user
    return current_user

def set_start_time(time):
    global start_time
    start_time = time

def get_start_time():
    global start_time
    return start_time

def clear_start_time():
    global start_time
    start_time = None
