# Function to Remove Employee with given Id



def Remove_Employ():

    Id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
     
    else:
         
        # Query to Delete Employee from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Removed")
        menu()
 
