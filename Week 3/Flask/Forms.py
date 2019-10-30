from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class CreateUserForm(Form):
    firstName = StringField("First Name", [validators.Length(min=1, max=150), validators.DataRequired()])
    lastName = StringField("Last Name", [validators.Length(min=1, max=150), validators.DataRequired()])
    membership = RadioField("Membership", choices=[("F", "Fellow"), ("S", "Senior"), ("P", "Professional")], default="F")
    gender = SelectField("Gender", choices=[("", "Select"), ("M", "Male"), ("F", "Female")], default="")
    remarks = TextAreaField("Remarks", [validators.Optional()])
