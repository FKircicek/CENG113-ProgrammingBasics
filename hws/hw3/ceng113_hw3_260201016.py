import re

def username_password_check(a,b):    
    users = open("users.txt", "r")
    x = []
    for i in users:
        y = i.split(";")        
        x.append(y)
    all_users = []
    for j in x:
        all_users.append(j[0])
    l = "Wrong password or username\n"
    if a in all_users:
        for k in x:
            if k[0] == a:
                if k[1] == b:
                    l = "Logged in\n"
                elif k[1] != b:
                    l = "Wrong password or username\n"
            elif k[0] != a:
                l = "Wrong password or username\n"
    print(l)
def newuser():
    new_username = input("Please enter a new username:\n")
    new_username1 = ""
    users = open("users.txt", "r")
    x = []
    for i in users:
        y = i.split(";")        
        x.append(y)
    all_users = []
    for j in x:
        all_users.append(j[0])
    if new_username in all_users:
        print("Username not valid\n")
    else:
        if re.search("[a-z]",new_username) or re.search("[0-9]",new_username) or re.search("[A-Z]",new_username):
            new_username1 = new_username
        else:
            print("Username not valid\n")
    new_password = input("Please enter a new password\n")
    new_password1 = ""
    if 4 <= len(new_password) <= 8:
        if re.search("[a-z]",new_password) or re.search("[A-Z]",new_password) and re.search("[0-9]",new_password):
            new_password1 = new_password
        else:
            print("Password not valid\n")
    else:
        print("Password not valid\n")
    users = open("users.txt","a")
    users.write("\n"+new_username1+";"+new_password1+";")
    users.close()
def addfriend(a):
    add_friend = input("Please enter the name of your new friend:\n")
    users = open("users.txt", "r")
    x = []
    for i in users:
        y = i.split(";")        
        x.append(y)
    all_users = []
    for j in x:
        all_users.append(j[0])
    for k in x:
        g = k[2].strip()
        k.remove(k[2])
        k.append(g)
    if add_friend in all_users:
        for l in x:
            if add_friend not in l[2]:
                if l[0] == a:
                    l[2] = l[2]+","+add_friend+"\n"
            else:
                print("Friend not found\n")
    else:
        print("Friend not found\n")        
def show_friends(a):
    users = open("users.txt", "r")
    x = []
    for i in users:
        y = i.split(";")        
        x.append(y)
    for j in x:
        if a == j[0]:
            print(j[2])
        else:
            continue
    
username = ""    
while True:
    menu_text="1.Login/changeuser\n2.Createnewuser\n3.Addfriend\n4.Show my friends\n5. Exit\n"
    print(menu_text)
    option = input("")
    if option == "1":
        username = input("Please enter username:\n")
        password = input("Please enter password:\n")
        username_password_check(username,password)
    elif option == "2":
        newuser()
    elif option == "3":
        if username != "":
            addfriend(username)
        else:
            print("You need to log in first\n")
    elif option == "4":
        if username != "":
            show_friends(username)
        else:
            print("You need to log in first\n")
    elif option == "5":        
        break
    else:
        print("Invalid option\n")
        
        