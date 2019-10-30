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
        usersDict = {}
        db = shelve.open("storage.db", "c")

        try:
            usersDict = db["Users"]
        except:
            print("Error in retrieving Users from storage.db")
        user = User.User(createUserForm.firstName.data, createUserForm.lastName.data, createUserForm.membership.data, createUserForm.gender.data, createUserForm.remarks.data)
        db["Users"] = usersDict
        usersDict[user.get_userID()] = user
        print(user.get_firstName(), user.get_lastName(), "was stored in shelve successfully with userID =", user.get_userID())

        db.close()

        return redirect(url_for("home"))
    else:
        print("Hi")
    return render_template("createUser.html", form=createUserForm)

if __name__ == "__main__":
    app.run(debug=True)
