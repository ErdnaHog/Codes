class User:
    countID = 0

    def __init__(self, firstName, lastName, gender, membership, remarks):
        self.__class__.countID += 1
        self.__userID = self.__class__.countID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__membership = membership
        self.__remarks = remarks
        self.__status = "Active"

    def get_userID(self):
        return self.__userID

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_gender(self):
        return self.__gender

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks

    def get_status(self):
        return self.__status

    def set_userID(self, userID):
        self.__userID = userID

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_gender(self, gender):
        self.__gender = gender

    def set_membership(self, membership):
        self.__membership = membership

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_status(self, status):
        self.__status = status
