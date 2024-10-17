#!/usr/bin/env python
import json
import os
import flask as fk
#import sqlite3

#con = sqlite3.connect("data.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE Todo(Task, Status)")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

data = "data.json"
with open(data, 'r') as f:
    todo = json.load(f)


print("Welcome to Todo List.")
print("How you doin?")

while True:
    print()

    print("1.Add a new task")
    print("2.Edit existing task")
    print("3.Delete task")
    print("4.Mark as done")
    print("5.View tasks")
    print("6.Exit")
    
    print()
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            dictonary={}
            key = input("Enter the task:")
            value = False
            dictonary[key]=value
            if key in todo:
                print("Task already exists enter another tasks")
            else:
                todo.update(dictonary)
                print("New task added.")

        case 2:
            a = input("Enter the key you want to edit: ")
            new_key = input("Enter the new key: ")
            if new_key in todo:
                print("Task already exists enter another tasks")
            else:
                todo.update({new_key: todo.pop(a)})
                print("Task edited.")

        case 3:
            to_del = input("Enter the key you want to delete: ")
            todo.pop(to_del)

        case 4:
            a = input("Enter the task name you have completed: ")
            if todo[a]==True:
                print("Task already done.")
            else:
                todo[a]=True

        case 5:
            print("\nYou have Following task today.")
            for i in todo:
                print(i, ": ", todo[i])

        case 6:
            if os.path.exists(data):
                with open("data.json", "w") as outfile:
                    json.dump(todo, outfile)
                break

        case _:
            print("Invalid Option Choose again")

