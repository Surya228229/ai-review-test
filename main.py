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
print("Webhook Final Test")

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query


API_KEY = "my-secret-api-key-12345"

def delete_user(user_id):
    query = "DELETE FROM users WHERE id = " + user_id
    return query

def find_user(users, target):
    for user in users:
        if user["name"] == target:
            return user

    return None


def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)