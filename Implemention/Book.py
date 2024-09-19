import re
import os
import time
from InputHandler import InputHandler
from enum import Enum
from tabulate import tabulate

def clean_screen():
    os.system("cls")


def sleep():
    time.sleep(2)


class Book:
    updated_fields ={}
    def __init__(self , id=None ,title=None , publicationYear=None , author=None , ISBN=None ,isAvailable=None ,bookGenre=None) -> None:
        if id==None and title==None and  publicationYear ==None and author==None and ISBN==None and isAvailable==None and bookGenre==None :
            self.__id = 0
            self.__title = ""
            self.__author = ""
            self.__publicationYear = ""
            self.__ISBN = ""
            self.__isAvailable = False
            self.__bookGenre = ""
        else : 
            self.__id = id
            self.__title = title
            self.__author = author
            self.__publicationYear = publicationYear
            self.__ISBN = ISBN
            self.__isAvailable = isAvailable
            self.__bookGenre = bookGenre

    @classmethod
    def with_data (cls , id ,title , publicationYear , author , ISBN ,isAvailable ,bookGenre) :
        return cls(id ,title , publicationYear , author , ISBN ,isAvailable ,bookGenre)

    def set_ISBN (self , value=None) : 
        if value == None : 
            self.__ISBN =InputHandler.set_ispn()

        else : 
            self.__ISBN = InputHandler.set_ispn_as_arg(value)

    def set_title(self , value=None) : 
        if value == None : 
                self.__title = InputHandler.set_alphString_from_user(
                    "Title", OutputMessage="Enter the Title of the book:")
        else : 
            self.__title = InputHandler.set_alphString_as_args('Title' , value)
    
    def set_author(self , value=None) : 
        if value == None : 
                self.__author = InputHandler.set_alphString_from_user(
                    "author name ", OutputMessage="Enter the Author of the book : "   
                )
        else : 
                self.__author = InputHandler.set_alphString_as_args("Author" ,value)

    def set_publicationYear (self , value=None) :       ####### here 
        if value == None : 
                self.__publicationYear = InputHandler.set_date_from_user("PublicationYear" , "Enter A PublicationYear : ")
        else : 
                self.__publicationYear = InputHandler.set_date_as_arg(value)

    def set_bookGenre(self ,value =None) :
        if value == None : 
                self.__bookGenre = InputHandler.set_alphString_from_user(
                    "Genre", OutputMessage="Enter the Genre of the book : "
                )

        else: 
                self.__bookGenre = InputHandler.set_alphString_as_args( "Genre",value)




    def set_isAvailable (self , value=None) : 
        self.__isAvailable = value

    def get_ISBN(self) : 
        return self.__ISBN
    def get_book(self):
        return {
            "ISBN": self.__ISBN,
            "title": self.__title,
            "author": self.__author,
            "publicationYear": self.__publicationYear,
            "isAvailable": self.__isAvailable,
            "bookGenre": self.__bookGenre,
        }

    def add_book(self):
        try:
            title = InputHandler.set_alphString_from_user(
                "title", OutputMessage="Enter the Title of the book:"
            )
            ISPN = InputHandler.set_ispn()  # Design Specific Pattern
            bookGenre = InputHandler.set_alphString_from_user(
                "Genre", OutputMessage="Enter the Genre of the book : "
            )
            author = InputHandler.set_alphString_from_user(
                "author name ", OutputMessage="Enter the Author of the book : "
            )
            publicationYear = InputHandler.set_date_from_user(
                fieldName="Publication Year",
                OutputMessage="Enter the publication year of the book (YYYY/mm/dd): ",
            )

        except ValueError as e:
            clean_screen()
            print(f"{e}")

        else:
            self.__title = title
            self.__ISBN = ISPN
            self.__author = author
            self.__bookGenre = bookGenre
            self.__publicationYear = publicationYear
            self.__isAvailable = True

        # def add_book(self , data ,file_path) :    # This Overloading Funcion That Read Data From joson File
        pass


    def update_book(self ,choice):
            if choice == 1:
                self.set_title()
                # Book.updated_fields["title"] = self.__title
            elif choice == 2:
                self.set_author()
                # Book.updated_fields["author"] = self.__author
                
            elif choice == 3:
                self.set_bookGenre()
                # Book.updated_fields["bookGenre"] = self.__bookGenre
            elif choice == 4:
                self.set_publicationYear()
                # Book.updated_fields["publicationYear"] = self.__publicationYear
            elif choice == 5:
                self.remove_book()

            elif choice == 6 :    # Cancel
                 self.set_ISBN()

            elif choice == 7 :    # Cancel
                 pass 
            else:
                pass



    def remove_book(self):
        while True:
            choice = input(
                f"The Book ({self.__title}) Will be Removed , Are You sure ? (Y/N) : "
            ).lower()
            if choice == "y" or choice == "yes":
                self.__isAvailable = not self.__isAvailable
                print(f"The Book ({self.__title}) Removed Successfully ")
                sleep()
                break
            elif choice == "n" or choice == "no":
                print("The Process is Canceled ")
                sleep()
                break
            else:
                print("Wrong Choice ! ")

    def __str__(self) -> str:
        if (
            self.__author != None
            and self.__bookGenre != None
            and self.__publicationYear != None
            and self.__ISBN != None
            and self.__title != None
              ):
            tabulate_data = [["ID" , "Title" , "PublicationYear" , "Author" , "ISBN" ,"IS_Available" ,"BookGenre"] , [self.__id ,self.__title , self.__publicationYear ,self.__author ,self.__ISBN ,self.__isAvailable ,self.__bookGenre]]
            return tabulate(tabular_data=tabulate_data ,tablefmt="heavy_grid")
        return "Incomplete Book Information"



if __name__ == "__main__":
    book = Book()
    book.add_book()
    # book.update_book()
    print(book)
