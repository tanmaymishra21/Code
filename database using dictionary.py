
# coding: utf-8

# In[ ]:


#Exist Database
database={"log_in":{"User_ID":[100,101,102,103,104,105], "Password":
                    ["@Tanmoy*1234","@Tarpan*1234","@Sagnik*1234","@Nikita*1234"
                    "@Pritam*1234","@Gautamee*1234"],"Name":["Tanmoy","Tarpan"
                        ,"Sagnik","Nikita","Pritam","Gautamee"]}}  
#Sign in Page
qu=input("do you have any account : \n")
if qu in ("Yes","yes","YES"):
    user_id=int(input("Enter your User ID\n"))
    for i in range(0,6):
        if user_id==database['log_in']['User_ID'][i]:
            print("your id is :",database['log_in']['User_ID'][i])
            pswd=input("Enter your password\n")
            if pswd==database['log_in']['Password'][i]:
                print("welcome!!!!",database['log_in']['Name'][i])
            else:
                print("Click forget password")
        else:
            print("Please enter your correct user ID")
            break
#Sign Up Page            
elif qu in ("NO","no","No"):
    print("Welcome to sign up page!!!!!")
    name=input("Enter your first Name\n")
    last_name=input("Enter your last Name\n")
    Id=input("Enter your id\n")
    paswd=input("Enter your password\n")
    print("hi",name,"!!!","Welcome to Learning_Python's page ")
    
else:
    print("pls enter : yes or no")

#Exit page
ext=input("Do you want to leave this page")
ans=input("Yes or No")
if ans in ("Yes","yes","YES"):
    print("Exit")
else:
    print("Please click Sign in or sign up and keep reading")

