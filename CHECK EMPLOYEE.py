# Function To Check if Employee with given Id Exist or Not
 
def check_employee(employee_id):
 
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'
 
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
 
    # Executing the SQL Query
    c.execute(sql, data)
 
    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
     
    if r == 1:
        return True
    else:
        return False
