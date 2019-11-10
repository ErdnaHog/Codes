from flask import Flask, render_template, redirect, request, url_for
from Forms import CreateUserForm
import shelve, User

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contactUs")
def contact_us():
    return render_template("contactUs.html")

@app.route("/createUser", methods=["GET", "POST"])
def createUser():
    createUserForm = CreateUserForm(request.form)
    if request.method == "POST" and createUserForm.validate():        
        db = shelve.open("storage.db", "c")
        try:
            usersDict = db["Users"]
            User.User.countID = int(list(usersDict.keys())[-1]) 
        except:
            usersDict = {}
            print("Error in retrieving Users from storage.db")
        #? using class to create user instance
        user_instance = User.User(createUserForm.firstName.data, createUserForm.lastName.data, createUserForm.gender.data, createUserForm.membership.data, createUserForm.remarks.data)
        usersDict[user_instance.get_userID()] = user_instance
        db["Users"] = usersDict        
        db.close()

        return redirect(url_for("retrieveUsers"))
    return render_template("createUser.html", form=createUserForm)

@app.route("/retrieveUsers", methods=["GET", "POST"])
def retrieveUsers():
    usersDict = {}
    db = shelve.open("storage.db", "r")
    usersDict = db["Users"]
    db.close()

    usersList = []
    for value in usersDict.values():
        usersList.append(value)

    return render_template("retrieveUsers.html", usersList=usersList, count=len(usersList))

if __name__ == "__main__":
    app.run(debug=True)
