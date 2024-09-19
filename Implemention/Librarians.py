from Person import Persons
from InputHandler import InputHandler
from datetime import datetime
from Database import DataBaseConnection
from Members import Member
from Book import Book
from Output_Messages import Menus
class Librarians(Persons):
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
        hire_date=None,
        years_of_experience=None,
    ) -> None:
        if hire_date is None and years_of_experience is None:
            # No arguments (default constructor)
            self.__hire_date = ""
            self.__years_of_experience = ""
            super().__init__()
        else:
            # Constructor with arguments
            self.__hire_date = hire_date
            self.__years_of_experience = years_of_experience
            super().__init__(
                user_name=user_name, name=name,age= age, email=email, id=id,phoneNumber= phoneNumber,address= address, password=password,DOB= DOB
            )
        self.book = Book()
        self.new_member = Member()

    @classmethod
    def with_data(
        cls,
        id,
        user_name,
        name,
        age,
        email,
        address,
        phoneNumber,
        password,
        DOB,
        hire_date,
        years_of_experience,
    ):
        return cls(
        id=id,
        user_name=user_name,
        name=name,
        age=age,
        email=email ,
        address=address,
        phoneNumber=phoneNumber,
        password=password,
        DOB=DOB,
        hire_date=hire_date,
        years_of_experience=years_of_experience,
        )

    @classmethod
    def valid_librarian(cls):
        cls.user_name = input("Enter Username : ")
        cls.password = input("Enter User Password : ")
        return DataBaseConnection.query(
            "librarian",
            f'Where user_name="{cls.user_name}" AND password="{cls.password}"',
            "*",
        )

    def set_hire_date(self, date=""):
        """
        Sets the hire date for an Librarians and calculates their years of experience.

        If a valid date is provided, it uses the date to set the hire date and calculate
        the years of experience. If no date is provided, the current date is used as the
        hire date and years of experience is calculated from today's date.

        Args:
            date (str): A string representing the hire date. Can be empty, in which case
                        today's date is used.
        """
        if date:
            self.__hire_date = InputHandler.set_date_as_arg(date=date)
            if (
                self.__hire_date
            ):  # Check if hire_date does not return error before next statement
                self.__years_of_experience = (
                    datetime.today().date().year - self.__hire_date.year
                )

        else:
            self.__hire_date = datetime.today().date()
            self.__years_of_experience = (
                datetime.today().date().year - self.__hire_date.year
            )


    def get_hire_date(self):
        return self.__hire_date

    def get_years_of_experience(self):
        return self.__years_of_experience

    def get_Librarian_info(self):
        info = super().get_personal_info()
        # info.__delitem__("id")
        info["hire_date"] = self.__hire_date.strftime("%Y-%m-%d")
        info["years_of_experience"] = self.__years_of_experience
        return info


    def add_new_librarian(self):
        self.add_new_person()
        self.set_hire_date()
        info = self.get_Librarian_info()
        info.__delitem__(
            "id"
        )  # This will delete the 'id' key and  database will give it value automatically
        DataBaseConnection.add_data("librarian", **info)



    
    def add_book(self) :
        """
        Allows the librarian to add a new book to the library.
        Interacts with the Book class to collect and store book data.
        """
        # Create a new book instance
        new_book = Book()
        # Call the add_book method from the Book class to fill in details
        new_book.add_book()
        # Get the book information
        book_info = new_book.get_book()
        print(book_info)
        # Add the book to the database
        DataBaseConnection.add_data("book", **book_info)

    def update_book(self,choice,id) : 
        fetched_book_from_database = DataBaseConnection.query("book" , f"WHERE id = {id}" ,"id","title","publicationYear","author","ISBN","isAvailable","bookGenre")
        self.book = Book(*fetched_book_from_database[0])   # Pass Result of Query To Book Object
        self.book.update_book(choice=choice)
        updated_fields=self.book.get_book()
        # book.updated_fields.clear()
        DataBaseConnection.update_columns("book",f"Where id = {id} ",**updated_fields)


    def add_new_member (self) :
        self.new_member.set_name(OutputMessage="Enter , Member Name : ")
        self.new_member.set_user_name(OutputMessage="Enter Member UserName : ")
        self.new_member.set_password(OutputMessage="Enter Member Password : ")
        self.new_member.set_age(outputMessage="Enter Member Age : ")
        self.new_member.set_phoneNumber(OutputMessage="Enter Member PhoneNumber: ")
        self.new_member.set_DOP(OutputMessage="Enter Member Birth Date : ")
        self.new_member.set_email(Output_Message="Enter Member E-mail : ")
        self.new_member.set_address(OutputMessage="Enter Member Address : ")
        self.new_member.set_member_type()
        self.new_member.account.set_membership_date()
        self.new_member.account.set_member_expiration_date()
        info = self.new_member.get_member_info()
        info.__delitem__("id")
        DataBaseConnection.add_data("member" , **info)
        id =DataBaseConnection.query("member" ,f"WHERE user_name='{self.new_member._user_name}' AND password='{self.new_member._password}' ", "id" )
        self.new_member.set_id(value=id[0][0])

    def __str__(self):
        return (
            "Librarian Information\n"
            f"id :{self._id}\n"
            f"name:{self._name}\n"
            f"phoneNumber: {self._phoneNumber}\n"
            f"age: {self._age}\n"
            f"adrress: {self._address}\n"
            f"email : {self._email}\n"
            f"birth date: {self._DOB}\n"
            f"hire_date: {self.__hire_date}\n"
            f"years_of_experience: {self.__years_of_experience}\n"
        )


if __name__ == "__main__":

    l = Librarians()
    l.Show_all_books()
