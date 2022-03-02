d1={"user1":1,"user2":2,"user3":3,"user4":4,"user5":5,"user6":5,"user7":7,"user8":8,"user9":9,"user10":10}
username=input("Enter your username : ")
if username  not in d1.keys():
    print("you are not a valid user of the system.")
else:
    password=eval(input("Enter your password :"))
    if password in d1.values() and username in d1.keys():
        print("You have sucessfully logged in")
    else:
        print("you entered wrong password ")
