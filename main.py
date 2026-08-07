import os

password = "admin123"

def login(username, password):
    if username == "admin" and password == "admin123":
        print("Login Success")
    else:
        print("Login Failed")

def add(a,b):
 print(a+b)
 return a+b

login("admin", "admin123")
add(5,6)

print("Webhook Test 2")
print("Automatic Review Test")