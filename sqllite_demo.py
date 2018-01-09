import sqlite3

#conn = sqlite3.connect(':memory:') # Just keeps the DB in the RAM. 
conn = sqlite3.connect('employees.db') # Just keeps the DB in the specified file
c = conn.cursor()

try:
    c.execute("""
        CREATE TABLE IF NOT EXISTS employees  (
            first text,
            last text,
            salary float
        )
        """)
    conn.commit()
    
except sqlite3.OperationalError as er:
    print ("Table already exists",er)

# Approach 1 with the hard coded strings and format statements

# Insert statements 
c.execute("INSERT INTO employees values('Teja','P',48000)")
c.execute("INSERT INTO employees values('Pramod','Ch',74000)")
c.execute("INSERT INTO employees values('{}', '{}', {})".format('Imran', 'Syed', 56000.99))
conn.commit()

# Update statements
c.execute("UPDATE employees set salary={} where last='{}'".format(65000,'Syed'))
conn.commit()

# Delete statements
#c.execute("DELETE from employees where last='{}'".format('P'))
#conn.commit()

c.execute("INSERT INTO employees values('Teja','P',48000)")
conn.commit()

# Select statements
c.execute("SELECT * from employees where last='{}'".format("Syed"))
print(c.fetchall())


# Approach 2 with tuples. The issue with hard coded strings is because of sql injection attack

# Insert 
c.execute("INSERT into employees values(?,?,?)",('Seenu','Khandavalli', 52000))
conn.commit()

# Update
c.execute("UPDATE employees set salary=? where last=?",(49000,'Khandavalli'))
conn.commit()

# Select. We need to put the comma if you are supplying only one value
c.execute("SELECT * from employees where last=?",('Ch',))
print(c.fetchall())

# Delete
c.execute("DELETE from employees where last=?",('P'))
conn.commit()

# Approach 3 Using the Dictionary

# Insert
c.execute("INSERT INTO employees values(:first, :last, :salary)", {'first':'Ravi Reddy','last':'Karri','salary':71000})
conn.commit()

# Update
c.execute("UPDATE employees set salary=:sal where last=:last",{'sal':74000,'last':'Karri'})
conn.commit()

# Delete
c.execute("DELETE from employees where last=:l",{'l':'P'})
conn.commit()

# Select. We need to put the comma if you are supplying only one value
c.execute("SELECT * from employees where last like(:l)",{'l':'%Kh%'})
print(c.fetchall())

c.execute("SELECT * from employees")
print (c.fetchall())

