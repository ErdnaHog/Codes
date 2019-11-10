from flask import Flask, render_template, redirect, request, url_for
from Forms import CreateUserForm
import shelve, User, os

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
    if request.method == "POST":
        db = shelve.open("storage.db", "w")
        usersDict = db["Users"]
        data = request.form.to_dict(flat=False)
        del usersDict[int(list(data.keys())[0])]
        db["Users"] = usersDict
        db.close()
    if os.path.exists("storage.db.dat"):
        db = shelve.open("storage.db", "r")
        usersDict = db["Users"]
        db.close()

        usersList = []
        for value in usersDict.values():
            usersList.append(value)
    else:
        usersList = []

    return render_template("retrieveUsers.html", usersList=usersList, count=len(usersList))

@app.route("/updateUser/<int:id>", methods=["GET", "POST"])
def updateUser(id):
    updateUserForm = CreateUserForm(request.form)
    if request.method == "POST" and updateUserForm.validate():
        db = shelve.open("storage.db", "w")
        userDict = db["Users"]

        user = userDict.get(id)
        user.set_firstName(updateUserForm.firstName.data)
        user.set_lastName(updateUserForm.lastName.data)
        user.set_membership(updateUserForm.membership.data)
        user.set_gender(updateUserForm.gender.data)
        user.set_remarks(updateUserForm.remarks.data)

        db["Users"] = userDict
        db.close()

        return redirect(url_for("retrieveUsers"))
    else:
        db = shelve.open("storage.db", "r")
        userDict = db["Users"]
        db.close()

        user = userDict.get(id)
        updateUserForm.firstName.data = user.get_firstName()
        updateUserForm.lastName.data = user.get_lastName()
        updateUserForm.membership.data = user.get_membership()
        updateUserForm.gender.data = user.get_gender()
        updateUserForm.remarks.data = user.get_remarks()

        return render_template("updateUser.html", form=updateUserForm)

if __name__ == "__main__":
    app.run(debug=True)
