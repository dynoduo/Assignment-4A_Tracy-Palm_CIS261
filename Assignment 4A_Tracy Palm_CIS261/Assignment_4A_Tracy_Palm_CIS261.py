def GetUserName():
    UserName = input("Enter the user name: ")
    return UserName

def GetUserPassWord():
    UserPwd = input("Enter the password: ")
    return UserPwd

def GetUserRole():
    UserRole = input("Enter role (Admin or User): ")
    while True: 
        if (UserRole.upper() == "ADMIN" or UserRole.upper() == "USER"):
            return UserRole
        else: 
            UserRole = input("Enter role (Admin or User): ")

def printinfo():

    UserFile = open("Users.txt", "r")
    while True: 
        UserDetail = UserFile.readline()
        if not UserDetail: 
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        UserName = UserList[0]
        UserPassWord = UserList[1]
        UserRole = UserList[2]
        print("User Name: ", UserName, "Password: ", UserPassWord, "Role: ", UserRole)

if __name__ == "__main__": 
    UserFile = open("Users.txt", "a+")
    while True: 
        UserName = GetUserName()
        if (UserName.upper() == "END"):
            break
        UserPwd = GetUserPassWord()
        UserRole = GetUserRole()

        UserDetail = UserName + "|" + UserPwd + "|" + UserRole + "\n"
        UserFile.write(UserDetail)

    UserFile.close()
    printinfo()