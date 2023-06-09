devops=["Docker","Kubernetes","Python","Bash","Git"]
development=("Agile","Webapp","DB")
dic_1={"Name":"Bhushan","Emp ID":"12345"}
dic_2={"Name":"Shailesh","Emp ID":"16543"}

name=input("Type your name: ")
user_skill=input("Type the Skills you know: ")

if user_skill in devops and (name in dic_1.values() or (name in dic_2.values())):
    print(f"{name} has matched the {user_skill} skill in the devops team")
elif user_skill in development and (name in dic_1.values() or name in dic_2.values()):
    print(f"{name} has matched the {user_skill} skill in the development team")
elif user_skill in devops and (name not in dic_1.values() or name not in dic_2.values()):
    print("Please Enter the correct name of the Employee")
elif user_skill in development and (name not in dic_1.values() or name not in dic_2.values()):
    print("Please Enter the correct name of the Employee")
elif user_skill not in devops and (name in dic_1.values() or name in dic_2.values()):
    print(f"{name},Please Enter the correct name of the Skill")
elif user_skill not in development and (name in dic_1.values() or name in dic_2.values()):
    print(f"{name},Please Enter the correct name of the Skill")
else:
    print("Please check the spelling and reEnter correctly")
