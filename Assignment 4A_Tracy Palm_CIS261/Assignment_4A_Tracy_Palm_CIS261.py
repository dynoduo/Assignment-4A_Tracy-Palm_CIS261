def GetUserName():
    username = input("Enter the user name: ")
    return username

def GetUserPassWord():
    pwd = input("Enter the password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True: 
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole 
        else: 
            userrole = input("Etner role (Admin or User): ")

def printinfo():

    UserFile = open("Users.txt", "r")
    while True: 
        UserDetail = UserFile.readline()
        if not UserDetail: 
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userPassWord = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userPassWord, "Role: ", userrole)

if __name__ == "__main__": 
    UserFile = open("Users.txt", "a+")
    while True: 
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassWord()
        userrole = GetUserRole()

        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)

    UserFile.close()
    printinfo()