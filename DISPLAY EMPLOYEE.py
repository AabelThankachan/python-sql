# Function to Display All Employees
# from Employee Table


 
def Display_Employees():
     
    # query to select all rows from
    # Employee Table
    sql = 'select * from empd'
    c = con.cursor()
     
    # Executing the SQL Query
    c.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print()
    menu()
