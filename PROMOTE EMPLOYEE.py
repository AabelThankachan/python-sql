# Function to Promote Employee

def Promote_Employee():
    Id = int(input("Enter Employ's Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
 
        # Query to Fetch Salary of Employee with
        # given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
 
        # Query to Update Salary of Employee with
        # given Id
        sql = 'update empd set salary=%s where id=%s'
        d = (t, Id)
    	
        # Executing the SQL Query
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        menu()

