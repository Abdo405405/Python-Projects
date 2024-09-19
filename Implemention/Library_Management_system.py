from Librarians import Librarians
from Members import Member
from Book import Book
from Database import DataBaseConnection
from Output_Messages import Menus
from time import sleep
from os import system

def clean_screen():
    system("cls")


class Library:

    def __init__(self) -> None:
        self.user_type = ""
        self.user_name = ""
        self.password = ""
        self.librarian = Librarians()

    def Login_as_Librarian(self):
            user_data = Librarians.valid_librarian()
            if user_data:
                print("Yout Are LogedIN ✅ ")
                sleep(2)
                self.librarian = Librarians.with_data(*user_data[0])
                while True :
                    choice = Menus.Librarian_Menu(user=self.librarian.get_name())
                    if choice == "Show All Books" :   ## here Error
                        self.librarian.Show_all_books()
                        input("\nPress To Show Main Menu  ")
                    elif choice== "Add New Book":                              # Add Book
                        clean_screen()
                        self.librarian.add_book()
                        input("\nPress To Show Main Menu  ")
                    elif choice == "Update Book":                             # Update Book 
                        clean_screen()
                        id = input("Enter ID of The Book : ")
                        self.librarian.update_book(choice=0 , id=id)  # this line to fetch this book by update nothing
                        while True :  
                            print(self.librarian.book)
                            choice = Menus.Updated_Menu()
                            if choice == 7 : 
                                break 
                            self.librarian.update_book(choice=choice , id=id)
                            choice = Menus.Checking_Another_Update()
                            if choice == 'Yes' or choice == 'y' or choice == '1' : 
                                continue
                            elif choice == "No" or choice == 'n' or choice == '0': 
                                break 
                            else : 
                                print("Wrong Choice !")
                                sleep(2)

                    elif choice == "Delete Book":
                        id = input("Enter ID of The Book : ")
                        while True : 
                            book_name = DataBaseConnection.query("book" , f"WHERE id = {id}" , 'title')
                            choice = Menus.Delete_Menu(book_name[0][0])
                            if choice == "Yes" : 
                                DataBaseConnection.Delete("book",id=id)
                                print(f"The Book ({book_name[0][0]}) Deleted Successfully ")
                                input("\n\n\nEnter To Return To Main Menu ")
                                break
                            elif choice == "No" :
                                print("Process is Canceled")
                                sleep(2)
                                break
                            else : 
                                print("Wrong Choice")
                                sleep(2)
                                continue

                            
                    elif choice == "Add New Member": 
                        clean_screen()
                        self.librarian.add_new_member()
                        print(f"OK ✅ , The Member ({self.librarian.new_member.get_name()}) Added Successfully ")
                        input("\n\n\nEnter To Return To Main Menu ")

                    elif choice == "Add New librarian": 
                        new_librarian = Librarians()
                        new_librarian.add_new_librarian()
                        clean_screen()
    
                    elif choice == "Logout": 
                        break

                    else : 
                        print("Wrong Choice !")
                        sleep(2)
            else:
                print("Wrong Username or password ❌")
                sleep(2)

    def Login_as_Member(self) : 
        user_data = Member().valid_Member()
        self.member = Member.with_data(*user_data[0])
        if user_data : 
                print("Yout Are LogedIN ✅ ")
                sleep(2)
                while True : 
                       choice = Menus.Member_Menu(self.member.get_name())
                       if choice == "Show My Profile" : 
                           Menus.Show_Profile(self.member)
        
                       elif  choice == "Borrow Book" : 
                           clean_screen()
                           print("You want To Borrow Book , Ummmm 🧐")
                           sleep(2)
                           self.member.Show_all_books()
                           book_id = input("\nOk , Put First Can Enter ID Of This Book: ")
                           self.member.account.borrow_book(book_id=book_id)
                           input("\n\n\nEnter To Return To Main Menu")
        
                       elif choice == "View My Books" : 
                           Menus.Data_View(data=self.member.account.view_borrowed_books() ,headers= ["id" , "title"  , "Author" , "bookGenre" , "book_borrowing_date" , "book_return_date"])
                           input("\n\n\nEnter To Return To Main Menu")
        
                       elif  choice == "Return  Book" : 
                           book_id = int(input("\nOk , Put First Can Enter ID Of This Book: "))
                           book_info = DataBaseConnection.query('book' , f"WHERE id = {book_id}",'*')
                           self.member.account.set_book_return_date(date=book_info[0][9])
                           self.member.account.return_book(book_id=book_id)
                           sleep(2)
    
                       elif choice == "Logout" : 
                           break 
           
           
        else : 
            print("Wrong Username or password ❌")
            sleep(2)
    
    
    
    
    def Login (self) : 
        while True : 
            self.user_type = Menus.Login_Menu()
            if self.user_type == "Login as librarian"  : 
             clean_screen()
             self.Login_as_Librarian()

            elif self.user_type == "Login as Member" : 
                clean_screen()
                self.Login_as_Member()

            elif self.user_type == "Return To Register Page" :
                break

            else : 
                print("Wrong Choice")
                sleep(2)
                continue

    
    def Register(self) : 
        pass


    def start(self):
        while True :
            Welcomed_Menu_choice = Menus.Welcomed_Menu()
            if Welcomed_Menu_choice == "login":
                clean_screen()
                self.Login()
    
            elif Welcomed_Menu_choice == "register":
                clean_screen()
                self.Register()

            else : 
                print("Wrong Choice")
                sleep(2)
                continue

        

    def Quit(self) : 
        print("Have A Nice Day , Good By 🤧 ")
        exit()
l = Library()
l.start()
