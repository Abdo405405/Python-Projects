import re
import os
from datetime import datetime
from Database import DataBaseConnection
def clean_screen():
    os.system("cls")


class InputHandler:
    """
    A class responsible for handling all user input prompts and validations.
    It can handle inputs from the console or from a JSON file.
    """

    @staticmethod
    def set_alphString_from_user(fieldName="", OutputMessage="") -> str:
        pattern = (
            re.compile(r"[\w\W]+")
            if fieldName == "title" or fieldName == "address"
            else re.compile(r"[A-Za-z\s]+")
        )  # To check if string has only letters or spaces
        while True:
            value = input(f"{OutputMessage}").strip().lower().title()
            if not pattern.fullmatch(value):
                # clean_screen()
                print(
                    f"Error: {fieldName.capitalize()} must contain only letters and spaces.\n"
                )
            else:
                # clean_screen()
                # print(f"{fieldName} added Successfully ")
                return value

    @staticmethod
    def set_alphString_as_args(fieldName, inputValue):
        pattern = (
            re.compile(r"[\w\W]+")
            if fieldName == "title" or fieldName == "address"
            else re.compile(r"[A-Za-z\s]+")
        )  # To check if string has only letters or spaces
        inputValue = inputValue.strip().lower().title()
        if not pattern.fullmatch(inputValue):
            raise ValueError(
                f"Error: {fieldName.capitalize()} must contain only letters and spaces."
            )
        return inputValue

    @staticmethod
    def set_date_from_user(fieldName, OutputMessage) -> str:
        """
        Validate Date (YYYY/mm/dd) format from user input .
        """
        pattern = re.compile(r"^(\d{4})(.)(\d{1,2})\2(\d{1,2})$")
        while True:
            try:
                date = input(f"{OutputMessage}")
                match = pattern.match(date)
                if match:
                    year, delimiter, month, days = (
                        match.groups()
                    )  # it will return [year , delimiter , month , days]
                    year = int(year)
                    month = int(month)
                    days = int(days)
                    check_date = datetime(year, month, days)
                    if check_date > datetime.now():
                        raise ValueError("Date cannot be in the future")
                else:
                    raise ValueError(
                        "Invalid format. Expected format: YYYY/MM/DD, YYYY-MM-DD, or similar"
                    )
            except ValueError as e:
                print(f"{e}")
            else:
                return check_date.date().strftime("%Y-%m-%d")

    @staticmethod
    def set_date_as_arg(date) -> str:
        """
        Validate Date Expected format: YYYY/MM/DD, YYYY-MM-DD, or similar as Argument .
        """
        pattern = re.compile(r"^(\d{4})(.)(\d{1,2})\2(\d{1,2})$")
        try:
            match = pattern.match(date)
            if match:
                year, delimiter, month, days = (
                    match.groups()
                )  # it will return [year , delimiter , month , days]
                year = int(year)
                month = int(month)
                days = int(days)
                check_date = datetime(year, month, days)
                if check_date > datetime.now():
                    raise ValueError("Date cannot be in the future")
            else:
                raise ValueError(
                    "Invalid format. Expected format: YYYY/MM/DD, YYYY-MM-DD, or similar"
                )
        except ValueError as e:
            print(f"{e}")
        else:
            return check_date.date().strftime("%Y-%m-%d")

    @staticmethod
    def set_ispn(data=None) -> str:
        """
        Get ISPN either from user input .
        """
        return input("Enter ISPN of the book: ").strip()

    @staticmethod
    def set_ispn_as_arg(ispn=None) -> str:
        """
        Get ISPN from provided data (file).
        """
        return ispn.strip()

    @staticmethod
    def set_email_from_user(Output_Message=""):
        pattern = re.compile(r"^[\w]+@(gmail|hotmail|yahoo)\.(com)$")
        while True:
            email = input(f"{Output_Message}")
            if pattern.match(email):
                # clean_screen()
                # print("Email Added Successfully")
                return email
            else:
                # clean_screen()
                print("ُError:Invalid Email")

    @staticmethod
    def set_email_as_arg(email):
        pattern = re.compile(r"^[\w]+@(gmail|hotmail|yahoo)\.(com)$")
        if pattern.match(email):
            return email
        else:
            raise ValueError("ُError:Invalid Email")

    @staticmethod
    def set_pos_int_value_from_user(outputMessage, ErrorMessage=""):
        while True:
            try:
                inp = int(input(f"{outputMessage}"))
                if not isinstance(inp, int) or inp <= 0:
                    raise ValueError

            except ValueError:
                print(f"{ErrorMessage}")

            else:
                # clean_screen()
                # print("Age Added Successfully")
                return inp

    def set_pos_int_value_as_arg(inp, ErrorMessage=""):
        try:
            if not isinstance(inp, int) or inp <= 0:
                raise ValueError

        except ValueError:
            print(f"{ErrorMessage}")

        else:
            # clean_screen()
            # print("Age Added Successfully")
            return inp

    @staticmethod
    def set_phoneNumber_from_user(fieldName, OutputMessage):
        pattern = re.compile(r"^(012|011|010|015)\d{8}$")
        while True:
            inp = input(f"{OutputMessage}").strip()
            if not pattern.match(inp):
                # clean_screen()
                print("Invalid Phone Number ")
            else:
                # clean_screen()
                # print("Phone Number Added Successfully")
                return inp

    @staticmethod
    def set_phoneNumber_as_args(fieldName, inputValue):
        pattern = re.compile(r"^(012|011|010|015)\d{8}$")
        if not pattern.match(inputValue):
            # clean_screen()
            raise ValueError("Invalid Phone Number ")
        # clean_screen()
        # print("Phone Number Added Successfully")

    # @staticmethod 
    def check_book_id_is_valid (id) : 
        """
        check if given id is valid , if it is return this book if not raise error and ask agian to get id 
        
        """
        while True : 
            try :
                fetched_book_from_database = DataBaseConnection.query("book" , f"WHERE id = {id}" ,"id","title","publicationYear","author","ISBN","isAvailable","bookGenre")
                if not fetched_book_from_database :  # if list is empty raise error 
                    raise ValueError ("This Book  Doesn't Exist  ") 
                
            except  ValueError as err:
                print(err) 
                id = input ("Enter Again Valid Id : ")

            else : 
                return fetched_book_from_database[0]




