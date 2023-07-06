# Function to Add_Employee

 
def Add_Employ():
 
    Id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Already Exist or Not
    if(check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
     
    else:
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        data = (Id, Name, Post, Salary)
 
        # Inserting Employee details in the Employee
        # Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Added Successfully ")
        menu()
