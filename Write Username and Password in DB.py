import re
def check_email(E):
  # pass the regular expression
  # and the string in search() method
  regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
  if (re.search(regex, E)):
    return True



def check_pass(P):
  l, u, p, d = 0, 0, 0, 0
  for i in P:

      # counting lowercase alphabets
      if (i.islower()):
        l += 1

        # counting uppercase alphabets
      if (i.isupper()):
        u += 1

        # counting digits
      if (i.isdigit()):
        d += 1

        # counting the mentioned special characters
      if (i == '@' or i == '$' or i == '_'):
        p += 1
  if ( (l >= 1 or u >= 1 or p >= 1) and d >= 1):
    return True


Email1 = input('Email:')
Pass1 = input('Password:')
if check_email(Email1):
  Email = Email1
else:
    print("Invalid Email:\n Your Email must be in the following format:\n example@domain.ir or example@domain.com ETC")
if check_pass(Pass1):
  Pass = Pass1
else:
    print("Invalid Password")




import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="mydatabase"
)
cursor = mydb.cursor()
if check_email(Email1) and check_pass(Pass):
  sql = "INSERT INTO user_pass (Email, Password) VALUES (%s, %s)"
  val = (Email, Pass)
  cursor.execute(sql, val)

mydb.commit()
mydb.close()



