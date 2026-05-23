
# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.


# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])
names = ["Alice", "Bob", "Charlie"]

def greeting(list_names):
    for name in list_names:
        print(f"hello {name}")
        
greeting(names)