from InputHandler import InputHandler
from abc import abstractmethod
from Database import DataBaseConnection
from Output_Messages import Menus
class Persons:
    def __init__(
        self,
        id=None,
        user_name=None,
        name=None,
        age=None,
        email=None,
        address=None,
        phoneNumber=None,
        password=None,
        DOB=None,
    ) -> None:

        if  user_name is not None and name is not None and age is not None and email is not None and id is not None and phoneNumber is not None and address is not None and password is not None and DOB is not None:
            self._user_name = user_name
            self._name = name
            self._age = age
            self._email = email
            self._id = id
            self._phoneNumber = phoneNumber
            self._address = address
            self._password = password
            self._DOB = DOB
        else:
            self._user_name = ""
            self._name = ""
            self._age = 0
            self._email = ""
            self._id = 0
            self._phoneNumber = ""
            self._address = ""
            self._password = ""
            self._DOB = ""

    @classmethod
    def with_data(
        cls, user_name, name, age, email, id, phoneNumber, address, password, DOB
    ):
        return cls(user_name, name, age, email, id, phoneNumber, address, password, DOB)
    

    def set_password(self, value="" ,OutputMessage="Enter , Your Password: "):
        if value:
            self._password = value
        else:
            value = input(OutputMessage)
            self._password = value


    def get_password(self):
        return self._password


    def set_user_name(self, value="",OutputMessage="Enter , Your UserName: "):
        if value:
            self._user_name = value
        else:
            value = input(OutputMessage)
            self._user_name = value

    def get_user_name(self) : 
        return self._user_name


    def set_id(self,value=0,OutputMessage="Enter ID : "):
        print(value)
        if value : 
            self._id = InputHandler.set_pos_int_value_as_arg(value ,ErrorMessage="Invalid ID")
        else:
          self._id = InputHandler.set_pos_int_value_from_user(outputMessage=OutputMessage , ErrorMessage="Invalid Id ")

    def get_id(self):
        return self._id


    def set_name(self, value="",OutputMessage="Please Enter Your Name : "):
        if value:
            self._name = InputHandler.set_alphString_as_args("name", inputValue=value)
        else:
            self._name = InputHandler.set_alphString_from_user(
                fieldName="name", OutputMessage=OutputMessage
            )

    def get_name(self):
        return self._name



    def set_DOP(self, value="",OutputMessage="Enter Your Birth Date (YYYY/mm/dd): "):
        if value:
            self._DOB = InputHandler.set_date_as_arg(
                fieldName="Birth Date", InputValue=value
            )
        else:
            self._DOB = InputHandler.set_date_from_user(
                fieldName="Birth Date",
                OutputMessage=OutputMessage,
            )
    
    def get_DOP(self):
        return self._DOB


    def set_address(self, value="",OutputMessage="Please Enter Your Address : "):
        if value:
            self._address = InputHandler.set_alphString_as_args(
                fieldName="address", inputValue=value
            )
        else:
            self._address = InputHandler.set_alphString_from_user(
                fieldName="address", OutputMessage=OutputMessage
            )
    
    def get_address(self):
        return self._address
   

    def set_phoneNumber(self, value="",OutputMessage="Please Enter Your Phone Number : "):
        if value:
            self._phoneNumber = InputHandler.set_phoneNumber_as_args(
                fieldName="Phone Number", inputValue=value
            )
        else:
            self._phoneNumber = InputHandler.set_phoneNumber_from_user(
                fieldName="Phone Number",
                OutputMessage=OutputMessage,
            )

    def get_phoneNumber(self):
        return self._phoneNumber
    

    def set_email(self, value="" ,Output_Message="Please Enter Your E-mail : " ):
        if value:
            self._email = InputHandler.set_email_as_arg(email=value)
        else:
            self._email = InputHandler.set_email_from_user(Output_Message=Output_Message)

    def get_email(self):
        return self._email


    def set_age(self, age=0 ,outputMessage="Please , Enter Your Age: "):
        if age:
            self._age = InputHandler.set_pos_int_value_as_arg(
                inp=age, ErrorMessage="Invalid Age"
            )
        else:
            self._age = InputHandler.set_pos_int_value_from_user(
                outputMessage=outputMessage, ErrorMessage="Invalid Age"
            )

    def get_age(self):
        return self._age


    def get_personal_info(self):
        return {
            "id": f"{self._id}",
            "user_name": f"{self._user_name}",
            "password": f"{self._password}",
            "name": f"{self._name}",
            "phoneNumber": f"{self._phoneNumber}",
            "age": f"{self._age}",
            "address": f"{self._address}",
            "email": f"{self._email}",
            "DOB": f"{self._DOB}",
        }



    def add_new_person(self):
        # self.set_id()
        self.set_name()
        self.set_user_name()
        self.set_password()
        self.set_age()
        self.set_phoneNumber()
        self.set_DOP()
        self.set_email()
        self.set_address()


    def Show_all_books (self) : 
        all_books_query =  DataBaseConnection.query("book", "","*")
        Menus.Data_View(data=all_books_query,headers=DataBaseConnection.columns_names("book"))
