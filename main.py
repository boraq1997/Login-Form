import tkinter
import json

jsonFile = 'users.json'

with open(jsonFile, 'r') as users:
    data = json.load(users)

root = tkinter.Tk()
root.title("LOGIN PAGE")
root.geometry("340x440")
root.configure(bg="#333333")

def login():
    usersAuth = {user['username']: user['password'] for user in data['users']}
    username = usernameEntry.get()
    password = passwordEntry.get()
    
    if len(username) > 0 and len(password) > 0:
        if username in usersAuth:
            storedPassword = usersAuth[username]
            if storedPassword == password:
                login_status.config(text=f"login successful, welcome {username}", fg="green")
            else:
                login_status.config(text=f"sorry password is not correct", fg="red")
        else:
            login_status.config(text=f"sorry username is not correct", fg="red")
    else:
        login_status.config(text="username and password can't be empty", fg="yellow")

frame = tkinter.Frame(bg="#333333")
frame.pack()

label = tkinter.Label(frame, text="LOGIN", bg="#333333", fg="#FF3399", font=('Candara', 15))
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

labelUsername = tkinter.Label(frame, text="USERNAME: ", bg="#333333", fg="white", font=('Candara', 13))
usernameEntry = tkinter.Entry(frame, font=('Candara', 15))
labelUsername.grid(row=1, column=0)
usernameEntry.grid(row=1, column=1, pady=20)

labelPassword = tkinter.Label(frame, text="PASSWORD: ", bg="#333333", fg="white", font=('Candara', 13))
passwordEntry = tkinter.Entry(frame, show="*", font=('Candara', 15))
labelPassword.grid(row=2, column=0)
passwordEntry.grid(row=2, column=1, pady=20)

loginButton = tkinter.Button(frame, text="LOGIN", font=('Candara', 15), bg="#FF3399", fg="#FFFFFF", command=login)
loginButton.grid(row=3, column=0, columnspan=2, pady=30)

login_status = tkinter.Label(root, text="", bg="#333333", fg="white", font=('Candara', 12))
login_status.pack()

root.mainloop()