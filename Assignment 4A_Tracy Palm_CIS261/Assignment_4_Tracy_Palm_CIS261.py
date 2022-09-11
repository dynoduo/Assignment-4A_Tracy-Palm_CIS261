from datetime import datetime

def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter the users name: ")
    UserRole = "None"
    while True: 
        UserDetail = UserFile.readline()
        if not UserDetail: 
            return UserRole, UserName
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        if UserName == UserList[0]:
           UserRole = UserList[2]
           return UserRole, UserName
    return UserRole, UserName
 

def get_name():

    name = input("Enter employee name: ")

    return name

 

def get_dates_worked():

    from_date = input("Enter the start date (mm/dd/yyyy): ")

    to_date = input("Enter the last date worked (mm/dd/yyyy): ")

    return from_date, to_date

 

def get_total_hours():

    total_hours = float(input("Enter total hours: "))

    return total_hours

 

def get_hourly_rate():

    hourly_rate = float(input("Enter hourly rate: "))

    return hourly_rate

 

def get_gross_pay(total_hours, hourly_rate):

    gross_pay = float(total_hours) * float(hourly_rate)

    return gross_pay

 

def get_tax_rate():

    tax_rate = float(input("Enter tax rate (in %): "))

    return tax_rate

   

def calculate_tax(gross_pay, tax_rate):

    tax = float(gross_pay) * float(tax_rate / 100)

    return tax

 

def calculate_netpay(gross_pay, tax_rate):

    tax = calculate_tax(gross_pay, tax_rate)

    net_pay = float(gross_pay) - float(tax)

    return net_pay

 

def PrintEmpInfo(DetailsPrinted):

    total_employees = 0

    total_hours = 0.00

    total_gross_pay = 0.00

    total_tax = 0.00

    total_net_pay = 0.00

    EmpFile = open("Employees.txt", "r")

    while True:

        rundate = input ("Enter start date for the report (MM/DD/YYYY) or All for all of the data in the file: ")

        if (rundate.upper() == "ALL"):

            break

        try:

            rundate = datetime.strptime(rundate, "%m/%d/%Y")

            break

        except ValueError:

            print("Invalid date format. Please try again.")

            print()

            continue

    while True:

        EmpDetails = EmpFile.readline()

        if not EmpDetails:      

            break

        EmpDetails = EmpDetails.replace("\n", "")

        EmpList = EmpDetails.split("|")

        from_date = EmpList[0]

        if (str(rundate).upper() != "ALL"):

           checkdate = datetime.strptime(from_date, "%m/%d/%Y")

           if (checkdate < rundate):

               continue
        to_date = EmpList[1]

        name = EmpList[2]

        hours = float(EmpList[3])

        hourly_rate = float(EmpList[4])

        tax_rate = float(EmpList[5])

        gross_pay = get_gross_pay(hours, hourly_rate)

        tax = calculate_tax(gross_pay, tax_rate)

        net_pay = calculate_netpay(gross_pay, tax_rate)

        print(from_date, to_date, name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}", f"{tax_rate:,.00%}", f"{tax:,.2f}", f"{net_pay:,.2f}")

        total_employees += 1

        total_hours += hours

        total_gross_pay += gross_pay

        total_tax += tax

        total_net_pay += net_pay

        EmpTotals["total_employees"] = total_employees

        EmpTotals["total_hours"] = total_hours

        EmpTotals["total_gross_pay"] = total_gross_pay

        EmpTotals["total_tax"] = total_tax

        EmpTotals["total_net_pay"] = total_net_pay

        DetailsPrinted = True

    if (DetailsPrinted):

        PrintTotals(EmpTotals)

    else:

        print("No detailed information to print")

 

def PrintTotals(EmpTotals):

    print()

    print(f'The total number of employees: {EmpTotals["total_employees"]}')

    print(f'The total hours worked: {EmpTotals["total_hours"]:,.2f}')

    print(f'The total gross pay: {EmpTotals["total_gross_pay"]:,.2f}')

    print(f'The total tax deductions: {EmpTotals["total_tax"]:,.2f}')

    print(f'The total net pay: {EmpTotals["total_net_pay"]:,.2f}')

 
if __name__ == "__main__":

    UserRole, UserName = Login()

    DetailsPrinted = False
    
    EmpTotals = {}

    if (UserRole.upper() == "NONE"):

        print(UserName, " is invalid.")
        
    else: 

        if (UserRole.upper() == "ADMIN"):

           EmpFile = open("Employees.txt", "a+")

           while True:

                name = get_name()

                if (name.upper() == "END"):

                    break

                from_date, to_date = get_dates_worked()

                hours = get_total_hours()

                hourly_rate = get_hourly_rate()

                tax_rate = get_tax_rate()

                EmpDetails = str(from_date) + "|" + str(to_date) + "|" + name + "|" + str(hours) + "|" + str(hourly_rate) + "|" + str(tax_rate) + "\n"

                EmpFile.write(EmpDetails)

        EmpFile.close()

    PrintEmpInfo(DetailsPrinted) 

