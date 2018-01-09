
import _mysql

try:
  conn = _mysql.connect("localhost", "root", "root", "test")
except Exception as e:
  print ("Connection Error ->", e)
  sys.exit()

sql = "INSERT INTO employee(name, location, salary, team) VALUES('Imran', 'HYD', 50000, 'Testing')"
conn.query(sql)
print("Row Inserted... ")

sql = "INSERT INTO employee(name, location, salary, team) VALUES('Pramod', 'PUN', 35000, 'DEV')"
conn.query(sql)
print("Row Inserted... ")

sql = "update employee set location='America', salary = 190000 where team='DEV'"
conn.query(sql)
print("Row Updated... ")

sql = "delete from employee where team = 'Testing'"
conn.query(sql)
print("Row Deleted... ")

sql = "select * from employee"
conn.query(sql)
print("Rows Retrieved... ")

result = conn.store_result()

print ("Number of rows", result.num_rows())

# Reading one record by one

row = result.fetch_row()

while(row):
    for i,n,l,s,t in row:
        print (str(i),str(n,'utf-8'),str(l,'utf-8'),str(s,'utf-8'),str(t), sep='\t')
    row = result.fetch_row()

# Reading by batch of five rows
row = result.fetch_row(5)

while(row):
    for i,n,l,s,t in row:
        print (str(i),str(n,'utf-8'),str(l,'utf-8'),str(s,'utf-8'),str(t), sep='->')
    print ("******************************************************************************")
    row = result.fetch_row(5)
    


conn.close()
