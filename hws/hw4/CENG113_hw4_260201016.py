# 260201016
import pandas as pd
#For now i used 'pandas' to generate table. If i find another way i'll change it 
file = open("TaskList.txt","r")
x = []
for i in file:
    a = i.replace("\n","")
#'\n' removed from the elements
    x.append(a)
task_list = []
for j in x:
    b = j.split(",")
    task_list.append(b)
#created a nested list
print("Welcome to Hero’s 5 Labors!")
hp = 3000
print("Remaining HP for Hero : ", hp)
hp_pegasus = 550
print("Remaining HP for Pegasus : ", hp_pegasus)
speed_hero = 20
speed_pegasus = 50
#all variables that we use
print("Here are the tasks left that hero needs to complete:")
table = pd.DataFrame(task_list,columns = ["TaskName","ByFootDistance","ByPegasus","HPNeeded"], dtype = int)
print(table)
all_tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
#created a list to check input
total_hour = 0
while True:
    if hp <= 0:
        print("Game Over")
        break
    #checking hp
    while True:    
        task_name = input("Where should Hero go next? ")
        if task_name in all_tasks:
            break
        else:
            print("Invalid option")
            continue
    #checking task name
    while True:
        travel = input("How do you want to travel?(Foot/Pegasus) ")
        if task_name == "Task1":
            if travel == "Foot":
                print("You cannot go there by foot.")
            elif travel == "Pegasus":
                break
            else:
                print("Invalid option.")
        elif task_name == "Task2":
            if travel == "Foot":
                print("You cannot go there by foot.")
            elif travel == "Pegasus":
                break
            else:
                print("Invalid option.")
        else:
            break
    #checking travel type
    for i in task_list:
        if task_name in i:
            if travel == "Foot":
                hour = int(i[1]) / speed_hero
                hp = hp - ((hour * 10) + int(i[3]))
                break
            elif travel == "Pegasus":
                hour = int(i[2]) / speed_pegasus
                hp = hp - int(i[3])
                hp_pegasus = hp_pegasus - (hour * 15) 
                break
    #calculating remaining hp
    total_hour = total_hour + hour
    print("Time passed : ", total_hour, "hour")
    print("Remaining HP for Hero : " , hp)
    print("Remaining HP for Pegasus : ", hp_pegasus)
    if hp <= 0:
        print("Game Over")
        break
    #checking heros and pegasus hp
    hour = 0
    while True:
        return_home = input("How do you want to go home?(Foot/Pegasus) ")
        for i in task_list:
            if task_name in i:
                if return_home == "Foot":
                    hour = int(i[1]) / speed_hero
                    hp = hp - (hour * 10)
                    break
                elif return_home == "Pegasus":
                    hour = int(i[2]) / speed_pegasus
                    hp_pegasus = hp_pegasus - (hour * 15)
                    if hp_pegasus < 120:
                        print("Pegasus does not have enough HP.")
                    else:    
                        break
                else:
                    print("Invalid option")
        if return_home == "Foot":
            break
        elif return_home == "Pegasus":
            break
        else:
            continue
    #checking 'return_home' and calculating heros and pegasus hp
        
    total_hour = total_hour + hour
    print("Hero arrived home")
    print("Time passed : ", total_hour, "hour")
    print("Remaining HP for Hero : " , hp)
    print("Remaining HP for Pegasus : ", hp_pegasus)
    for i in task_list:
        if task_name in i:
            task_list.remove(i)
    
    if task_list == []:
        print("Congratulations, you have completed the task.")
        break
    else:
        table = pd.DataFrame(task_list,columns = ["TaskName","ByFootDistance","ByPegasus","HPNeeded"], dtype = int)
        print(table)
hall_of_fame = open("HallOfFame.txt","a")
name = input("What is your name ? ")
h = name + " " + str(total_hour) + "\n"
hall_of_fame.write(h)
hall_of_fame.close()
hall_of_fame = open("HallOfFame.txt","r")
j = []
    
for i in hall_of_fame:
    k = i.split(" ")
    j.append(k)
print(j)
print("Hall Of Fame")
halloffame = pd.DataFrame(j,columns = ["Name","Finish Time"], dtype = str)
print(halloffame)


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
