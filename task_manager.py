# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: adm1n
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# PLEASE USE THE EXAMPLE task.txt FILE I PROVIDE IN THE FOLDER (This format allows for each task to have a number). 
# ALTERNATIVELY YOU CAN RUN THE 'task_manager' without a 'task.txt' file within your folder.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#=====test for commas in variables==========================================================================================================
# commas included in certain variables can cause ValueErrors 
def comma_defence(input_msg, offic_var_name):
    # While true the code below will execute
    #   request the user input a string.
    #   if ',' is not in the variable the code below is ran.
    #     break from the loop
    #   else print an error message and restart the loop
    while True:
        variable = input(input_msg)
        if ',' not in variable:
            break
        else:
            print(f"Oops! Your {offic_var_name} cannot include a comma. Please try again.")
        continue
    # return variable
    return(variable)

                
#=====this function registers new users====================================================================================================
def reg_user():
    
    # While true the code below will execute
    #  Declare 'new_username' variable and make it equal to the return value of the 'comma_defence()' function
    #  ... this will require the user to "input a username"
    #  if 'new_username' is not found as a key in the 'username_password' dictionary break from the while loop
    #  if 'new_username' is found as a key in the previous dictionary display an error message asking the user to try again
    while True:
        new_username = comma_defence("Input a new username: ", "username")
        if new_username not in username_password.keys():
            break
        print("Error: this username already exists. Please try again.")

    # - Request input of a new password 
    # Declare a 'new_password' variable and make equal to the return value of the 'comma_defence()' function
    # ...this will require the user to "input a password"  
    new_password = comma_defence("Input a password: ", "password")

    # - Request input of password confirmation.
    confirm_password = input("Confirm password: ")
        
    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        username_password[new_username] = new_password
        print()
        print("New user added!")
             
        # create a file called 'user.txt' in write mode
        #   declare an empty list variable called 'user_data'
        #   for each element (labelled k) in 'username_password' run the code below
        #   append the key'k' and the value associated value to the 'user_data' list
        #   join the elements of user_data with a '\n' and write to the 'out_file'
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k}, {username_password[k]}")
            out_file.write("\n".join(user_data))

    # if passwords don't match display an error message  
    else:
        print("Passwords do no match")

#=====this function is for adding tasks====================================================================================================
def add_task():

    # declare a variable called 'task_count' and make it equal to the length of 'task_list'
    task_count = len(task_list)
    # While the conditions are True run the code below
    while True:
        # request the user input the name of a person in which a task is 
        # ...assigned and store in a variable called 'task_username'
        # if task_username is not a key in the 'username_password' dictionary run the code below
        #   print an error message to alert that the user does not exist then continue the loop
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue

        # declare a 'task_title' variable and make it equal to the 'comma_defence' function
        # ...this will require the user to input the "Task Title: "
        # request the user input the description of the task and store it in a variable called 'task_description'
        # declare a 'task_description' variable and make it equal to the 'comma_defence' function
        # ...this will require the user to input the "Description of Task: "
        # break from the while loop        
        task_title = comma_defence("Task title: ", "task title")
        task_description = comma_defence("Description of Task: ", "task description")
        break

    # While the condition is true execute the code below    
    while True:
        # try below:
        #  request the user input a due date of a task and store in the variable 'task_due_date'
        #  test to see if 'task_due_date' is the DATETIME_STRING_FORMAT... 
        #  and store it in a variable called 'due_date_time'
        #  if 'task_due_date' was in the correct format break from the while loop
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        # except Value error and display and error message            
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # increment the the 'task_count' variable by one
    # transorm 'task_count' and store in a variable called 'task_number'
    task_count += 1
    task_number = str(task_count)

    # Then get the current date.
    curr_date = date.today()

    #declare a dictionary called 'new_task' within it store the keys with the value variables
    new_task = {
        "task_id": task_number,
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
        }

    # append the new task dictionary to the 'task_list' and then run the 'update_task_file()' function
    # print 'Task successfully added'
    task_list.append(new_task)
    update_task_file()
    print("Task successfully added.")

#=====this function allows users to view all task manager tasks============================================================================
def view_all():
    # Reads the task from task.txt file and prints to the console in the 
    # format of Output 2 presented in the task pdf (i.e. includes spacing
    # and labelling) 
    for t in task_list:
        display_string(t['task_id'], t['title'], t['username'], t['assigned_date'], t['due_date'], t['description'])

#=====this function allows users to view all the tasks assigned to them====================================================================  
#   Reads the task from task.txt file and prints to the console in the 
#   format of Output 2 presented in the task pdf (i.e. includes spacing
#   and labelling)       
def view_mine():

    # For each dictionary (labelled t) in 'task_list' run the code below:
    #   if the username key in the dictionary is equal to the current user run the code below:
    #      run the 'display_string()' function which displays the relevent 'task_list' dictionaries in the console   
    for t in task_list:
        if t['username'] == curr_user:
            display_string(t['task_id'], t['title'], t['username'], t['assigned_date'], t['due_date'], t['description'])


    # While True run the code below will execute
    while True:
        # while True the code below will execute
        #   try:
        #     request the user inputs a specific task number, transform it to an int 
        #     ...and store it in the variable 'specific_task'
        #   except:
        #      if the input is not a number print an error message
        while True:
            try:
                specific_task = int(input('''
Enter a task number to select a specific task assigned to you.
Otherwise if you would like to go back to the main menu please input -1. 
Input a number here: 
'''))
                break
            except Exception:
                print("Oops! That was not a valid number. Try again!")

        # if specific_task is more than or equal to 1 AND also less than or equal to 'task_count' 
        # ...AND either the task 'username' equals the 'curr_user' or 'curr_user' equals 'admin' run the code below
        #   print "You have selected: "
        #  run the display string funtion for the specific task
        if specific_task >= 1 and specific_task <= task_count and ((task_list[(specific_task-1)]['username'] == curr_user) or curr_user == 'admin'):
            print("You have selected: ")
            display_string(task_list[(specific_task-1)]['task_id'], task_list[(specific_task-1)]['title'], task_list[(specific_task-1)]['username'], task_list[(specific_task-1)]['assigned_date'], task_list[(specific_task-1)]['due_date'], task_list[(specific_task-1)]['description'])

        #   While true run the code below
        #      request the user input a letter corresponding to the options found in the input string 
        #      ...and store in a variable called 'specific_task_edit'
            while True:
                specific_task_edit = input(f'''
Select from one of the following options:
c - To mark task number {specific_task} as complete
e - Edit task number {specific_task}
r - Return to the previous menu
''').lower()
                # if 'specific_task_edit' is equal to 'c'
                #   find the 'completed' key of the corresponding list and change its value to True
                #   print a message to acknowledge this change
                #   break from the while loop
                if specific_task_edit == 'c':
                    task_list[(specific_task-1)]['completed'] = True
                    update_task_file()
                    print(f'''
    Task number {specific_task} has now been marked as complete''')
                    break
                
                #else if specific task is equal to 'e'

                elif specific_task_edit == 'e':
                    change_specific_task(specific_task)

                # break from the specific task option menu if 'specific_task_edit' is equal to 'r'  
                elif specific_task_edit == 'r':
                    break
                
                # if user doesn't select a correct option for the selected task print the following
                else:
                    print("You entered an incorrect value.")
                        
        # if after the user is asked to select a task they make 'specific_task' equal to -1 break from the while loop
        # else print to acknowledge they have input an incorrect value
        elif specific_task == -1:
            break

        # else if task number exists but is assigned to another person print error message
        elif specific_task >= 1 and specific_task <= task_count:
            print('''You have input a number for a task assigned to another user. Please try again''')

        # else print an error message
        else:
            print("You've entered a task number which does not exist. Please try again")

#=====this function allows user to change the task details==================================================================================
def change_specific_task(specific_task):
    # if the specific 'task_list' dictionary has a 'completed' key equal to False run the code below
    #   while True run the code below
    #     request the user input a value which is equal to a value displayed in the input string 
    #     ...and store it in a variable called 'task_edit_type'
    if task_list[(specific_task-1)]['completed'] == False:
        while True:
            task_edit_type = input(f'''
Select from one of the following options:
rt - Reassaign task {specific_task} to another user
ed - Edit due date of task {specific_task}
r - return to the previous menu
''').lower()
                                                      
            # if task_edit_type is equal to 'rt'
            if task_edit_type == 'rt':
                # while the conditions are true:
                #  request the user input the name of a user they would like to reassign the task to 
                #   ...and store in a variable called 'reassaign_user'                
                while True:
                    reassign_user = input('''
Please enter the name of the user you would like to reassaign this task: 
''')

                    original_user = task_list[(specific_task-1)]['username']
                    if reassign_user in username_password.keys():
                        task_list[(specific_task-1)]['username'] = reassign_user
                        update_task_file()
                        print(f'''
You have successfully reassaigned task {specific_task} from {original_user} to {reassign_user}''')
                        break
                    # else if 'reassign_user' is equal to 'r' break from the loop
                    elif reassign_user == 'r':
                        break
                    # else print a statement to acknowledge an incorrect username has been entered
                    else:
                        print('''
You entered an incorrect username. Ensure your entry is case sensitive or enter r to return back to the main menu''')
                            
            # else if 'task_edit_type' is equal to 'ed'
            #   while True the code below will run
            #       print asking when the due date should be changed to
            elif task_edit_type == 'ed':
                while True:
                    print('''
What would you like to update the due date of task {specific_task} to. ''')
                    # try:
                    #   request the user input a date in the correct format and store in a variable called 'task_due_date'
                    #   make the 'due_date' key in the corresponding dictionary of 'task_list' equal to 'task_due_date'
                    #   break from the while group
                    try:
                        task_due_date = input("Due date of task (YYYY-MM-DD):")
                        task_list[(specific_task-1)]['due_date'] = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        update_task_file()
                        break
                    # except:
                    #   deliver a message to ackowledge 'task_due_date' was inputted in the incorrect format
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")

            # else if 'task_edit_type' is equal to 'r' break from the while loop
            elif task_edit_type == 'r':
                break                        
            # else print "Please try again"
            else:
                print('''
You inputed an incorrect value. Please try again''')

    # if the task dictionary to be editied has a 'completed' key equal to True print "This task has already been completed"
    else:
        print('''
This task can't be edited as it has already been completed''')

#=====this function displays the task statistics============================================================================================
def display_statistics():
    
    # declare a variable called 'num_tasks' which is equal to the length of 'task_list'
    num_tasks = len(task_list)

    # declare a variable called 'completed_tasks' and make it equal to 0
    # for each dictionary (labelled t) in 'task_list' execute the code below
    #   if the 'completed' key in the dictionary is equal to True increment 'completed_tasks' by 1
    completed_tasks = 0
    for t in task_list:
        if t['completed'] == True:
            completed_tasks += 1

    # declare a variable called 'incomplete tasks' and make it equal to 0
    # for each dictionary (labelled t) in 'task_list' execute the code below
    #   if the 'completed' key in the dictionary is equal to False increment 'incomplete_tasks' by one
    incomplete_tasks = 0
    for t in task_list:
        if t['completed'] == False:
            incomplete_tasks += 1

    # declare a variable called 'overdue_tasks' and make it equal to 0
    # for each dictionary in 'task_list' execute the code below
    #    if the 'completed' key in the dictionary is equal to False and today's date is later than the dictionary's 
    #    ...'due_date' increment 'overdue_tasks' by one
    overdue_tasks = 0
    for t in task_list:
        if t['completed'] == False and date.today() > t['due_date'].date():
            overdue_tasks += 1

    # multiply 'incomplete_tasks' by 100 and divide by 'num_tasks'
    # round this number to the nearest two decimals and store in a variable called 'incomplete_percent'
    # multiply 'overdue_tasks' by 100 and divide the result by 'num_tasks'
    # round this number to the nearest two decimals and store in a variable called 'overdue_percent'
    incomplete_percent = round((incomplete_tasks*100/num_tasks), 2)
    overdue_percent = round((overdue_tasks*100/num_tasks), 2)

    # declare a variable called 'overview_stat' which contains a string containing the task overview statistics
    overview_stat = f"""=====Task Overview Statistics======
Number of tasks generated by task_manager.py:\t\t{num_tasks}
Number of completed tasks: \t\t\t\t{completed_tasks}
Number of uncompleted tasks: \t\t\t\t{incomplete_tasks}
Number of jobs incomplete and overdue: \t\t\t{overdue_tasks}
Percentage of tasks which are incomplete: \t\t{incomplete_percent}%
Perecentage of tasks which are incomplete and overdue: \t{overdue_percent}%"""
        
    # print 'overview_stat'
    print(overview_stat)
    # run the 'update_task_overview_file()' function with overview_stat as an argument
    update_task_overview_file(overview_stat)

    # declare a variable called 'num_users' and make it equal to the length of 'username_password'
    # print a string which contains the number of users and tasks generated to the console
    num_users = len(username_password)
    print(f"""
==========User Overview Statistics==========
Number of users generated by task_manager.py: \t {num_users}
Number of tasks generated by task_manager.py: \t {num_tasks}""")
    
    # declare a list variable called 'all_users' which is equal to the keys of the 'username_password' dictionary
    # declare an empty list variable called 'user_overview'
    all_users = username_password.keys()
    user_overview = []

    # for each 'name' in 'all_users' execute the code below
    #   declare the variables 'user_task_count', 'user_task_complete', 
    #   ...'user_task_incomplete', 'user_overdue_task' and make them equal to zero
    for name in all_users:
        user_task_count = 0
        user_task_complete = 0
        user_task_incomplete = 0
        user_overdue_task = 0   

        #  for each dictionary (labelled t) in 'task_list' execute the code below
        #    if the 'username' key in this dictionary is equal to 'name' increment the 'user_task_count' by one
        #    if the 'username' key in this dictionary is equal to 'name' and the 'completed' key is equal to True 
        #    ...increment 'user_task_complete' by one
        #    if the 'username' key in this dictionary is equal to 'name' and the 'completed' key is equal to False 
        #    ...increment 'user_task_incomplete' by one
        #    if the 'username' key in this dictionary is equal to 'name', the 'completed' key is equal to False, 
        #    ...and the 'due_date' key is less than the date today increment 'user_overdue_task' by one
        for t in task_list:
            if t['username'] == name:
                user_task_count += 1
            if t['username'] == name and t['completed'] == True:
                user_task_complete += 1
            if t['username'] == name and t['completed'] == False:
                user_task_incomplete += 1
            if t['username'] == name and t['completed'] == False and date.today() > t['due_date'].date():
                user_overdue_task += 1

        # if user_task_count is equal to zero execute the code below
        #   declare the variables 'task_assigned_percentage', 'user_complete_percentage', 'user_incomplete_percentage', 
        #   ...'user_overdue_percentage' and make them equal to 'N/A'
        if user_task_count == 0:
            task_assigned_percentage = "N/A"
            user_complete_percentage = "N/A"
            user_incomplete_percentage = "N/A"
            user_overdue_percentage = "N/A"

        # else
        #   multiply 'user_task_count' by 100 and divide the result by 'task_count'
        #   round the previous result to 2 decimal places and store in the variable called 'task_assigned_percentage'
        #   multiply 'user_task_complete' by 100 and divide the result by 'user_task_count'
        #   round the previous result to 2 decimal places and store in the variable called 'user_complete_percentage'
        #   multiply 'user_incomplete_percentage' by 100 and divide the result by 'user_task_count'
        #   round the previous result to 2 decimal places and store in the variable called 'user_incomplete_percentage'
        #   multiply 'user_overdue_task' by 100 and divide the result by 'user_task_count'
        #   round the previous result to 2 decimal places and store in the variable called 'user_overdue_percentage'
        else:
            task_assigned_percentage = round((user_task_count*100/task_count), 2)
            user_complete_percentage = round(((user_task_complete*100)/user_task_count), 2)
            user_incomplete_percentage = round(((user_task_incomplete*100)/user_task_count), 2)
            user_overdue_percentage = round(((user_overdue_task*100)/user_task_count), 2)

        # declare a variable called 'user_stat' which contains a string with an overview template for users of task_manager.py
        user_stat = f'''
===User overview for {name}===
The total number of tasks assigned: \t\t\t\t{user_task_count}
Percentage of all tasks assigned to the user: \t\t\t{task_assigned_percentage}%
Percentange of tasks assigned that are completed: \t\t{user_complete_percentage}%
Percentage of tasks assigned that are incomplete: \t\t{user_incomplete_percentage}%
Percentage of tasks that are incomplete and overdue: \t\t{user_overdue_percentage}%'''

        # print 'user_stat'
        # append 'user_stat' to user_overview
        print(user_stat)
        user_overview.append(user_stat)

    # run the 'update_user_overview_file()' using the arguments 'user_overview' and 'num_tasks' as arguments   
    update_user_overview_file(user_overview, num_tasks)

#=====This function takes in arguments and displays them as a string in the console========================================================
# This function takes the arguments 'task_number', 'title', 'username', 'assigned_date', 'due_date', 'description'
def display_string(task_number, title, username, assigned_date, due_date, description):

    # The 'disp_str' variable is made equal to the values found within a corresponding dictionary in a presentable format
    # 'disp_str' is printed to the console
    disp_str = f"Task Number \t:  {task_number}\n"
    disp_str += f"Task \t\t:  {title}\n"
    disp_str += f"Assigned to \t:  {username}\n"
    disp_str += f"Date Assigned \t:  {assigned_date.strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date \t:  {due_date.strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Description: \n {description}\n"
    return(print(disp_str))

#=====This function will update the 'task_file' containing the list of tasks==============================================================
def update_task_file():
    
    # create a file object called 'task_file' which is linked to a 'tasks.txt' file in write mode
    #   declare an empty list called 'task_list_to_write'
    #   for each dictionary (labelled t) in 'task_list'
    #     declare a list variable called 'str_attrs' which contains the values found in the dictionary
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['task_id'],
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
        #   join 'str_attrs' elements with "," and append to 'task_list_to_write'
        # join the elements of 'task_list_to_write' with "\n" and write to the 'task_file' object
            task_list_to_write.append(", ".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

#=====This function will update the 'task_overview.txt' file==============================================================================
# containing the overall task stats such as how many have been generated, completed, incomplete and overdue
def update_task_overview_file(overview_stat):
    
#   create a file object called 'task_overview_file' which is linked to 'task_overview.txt' in write mode
#       write 'overview_stat' to 'task_overview_file'
    with open("task_overview.txt", 'w') as task_overview_file:
        task_overview_file.write(overview_stat)

#=====this fucntion updates 'user_overview.txt'===========================================================================================
def update_user_overview_file(user_overview, num_tasks):

#   create a file object called 'user_overview_file' which is linked to 'user_overview.txt' in write mode
#       write a string containing information on the number of users and tasks generated to 'user_overview_file'
#   create a file object called 'user_overview_file' which is linked to 'user_overview.txt' in write mode which appends to the latter file
#       join the elements of 'user_overview' with "\n" and write to 'user_overview_file'
    num_users = len(username_password.keys())
    with open("user_overview.txt", 'w') as user_overview_file:
        user_overview_file.write(f"""==========User Overview Statistics==========
Number of users registered with task_manager.py: \t\t{num_users}
Number of tasks generated with task_manager.py:\t\t\t{num_tasks}
""")
    with open("user_overview.txt", 'a') as user_overview_file:
        user_overview_file.write("\n".join(user_overview))

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")

# Declare a variable called 'task_count' and make it equal to 0
# Decalare an empty list called 'task_list'
task_count = 0
task_list = []

# if the length of 'inbox_data' is more than or equal to 1
# ...or if length of the first item in inbox_data split by ',' is equal to 7
# ...the code below is executed
if (len(task_data)) >= 1 and len(task_data[0].split(", ")) == 7:
    # for each task string (labelled 't_str') in task data:
    #   increment 'task_count' by 1
    #   declare a dictionary called 'curr_t'
    for t_str in task_data:
        task_count += 1
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(", ")
        curr_t['task_id'] = task_components[0]
        curr_t['username'] = task_components[1]
        curr_t['title'] = task_components[2]
        curr_t['description'] = task_components[3]
        curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[6] == "Yes" else False
        
        # append 'curr_t' to 'task_list'
        task_list.append(curr_t)

#====This function checks the menu input===================================================================================================
def menu_options(menu):

    if menu == 'r':
        reg_user()
            
    elif menu == 'a':
        add_task()
            
    elif menu == 'va':
        view_all()
            
    elif menu == 'vm':
        view_mine()
            
    elif menu == 'ds' and curr_user == 'admin': 
        display_statistics()
            
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    else:
        print("You have made a wrong choice, Please Try again")

#====Task Overview Report Section==========================================================================================================

#====Login Section=========================================================================================================================
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin, adm1n")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(', ')
    username_password[username] = password

# declare a variable called 'logged_in' which is equal to False
# while 'logged_in' is not True
#  print "Login"
#  request the user input a username and make the input equal to 'curr_user'
#  request the user input a password and make the input equal to 'curr_pass'
#  if 'curr_user' is not found as a key in the 'username_password' dictionary print "User does not exist" and restart the loop
#  else if the value for the 'curr_user' key in the username_password dictionary is not equal to 'curr_pass print "password" and restart the loop
#  else print "Login Successful" and change 'logged_in' to True
logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

# if the current user is the admin use the admin user menu pathway
if curr_user == 'admin':
    # While true execute the code below
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    while True:
        print()
        menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
        menu_options(menu)

# else use the menu pathway for non admin users
else:
    while True:
        print()
        # presents menu without option to display statistics
        menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
        menu_options(menu)