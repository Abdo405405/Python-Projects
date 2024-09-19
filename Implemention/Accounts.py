from datetime import datetime, timedelta
from Policies import Policies
from Database import DataBaseConnection
class Account: 

    def __init__(self, member_id=None ,membership_date=None,member_expiration_date=None,membership_type=None,fine_due=None , book_return_date=None,book_borrowing_date=None) -> None:
    
        if member_id == None and membership_type == None and fine_due ==None and membership_date==None and member_expiration_date==None : 
          self._member_expiration_date = None
          self._membership_date = None
          self._fine_due = None
          self._book_borrowing_date = None
          self._book_return_date = None
          self._member_id = None
          self.fine_due = 0
          self._membership_type = None

        else :
          self._member_expiration_date = datetime.strptime(member_expiration_date,"%Y-%m-%d %H:%M:%S") if isinstance(member_expiration_date , str)  else member_expiration_date
          self._membership_date =  datetime.strptime(membership_date,"%Y-%m-%d %H:%M:%S") if isinstance(membership_date , str)  else membership_date
          self._book_borrowing_date = datetime.strptime(book_borrowing_date,"%Y-%m-%d %H:%M:%S") if isinstance(book_borrowing_date , str)  else book_borrowing_date
          self._book_return_date =  datetime.strptime(book_return_date,"%Y-%m-%d %H:%M:%S") if isinstance(book_return_date , str)  else book_return_date
          self._fine_due = fine_due
          self._member_id = member_id
          self._membership_type = membership_type


    def set_membership_date(self): 
        self._membership_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def set_member_expiration_date(self): 
        if self._membership_date is None: 
            print("Error: membership_date is not set")
            return 

        membership_date_obj = datetime.strptime(self._membership_date, "%Y-%m-%d %H:%M:%S")
        
        if self._membership_type == "MEMBERSHIP_10_MINUTES":  
            self._member_expiration_date = timedelta(minutes=10) + membership_date_obj
        elif self._membership_type == "MEMBERSHIP_5_MINUTES": 
            self._member_expiration_date = timedelta(minutes=5) + membership_date_obj
        elif self._membership_type == "MEMBERSHIP_15_DAY":  
            self._member_expiration_date = timedelta(days=15) + membership_date_obj

        else : 
            raise ValueError("Invalid membership type")
        
        # self.__member_expiration_date = datetime.strftime(self.__member_expiration_date, "%Y-%m-%d %H:%M:%S")
    

        
    def set_book_borrowing_date (self , current_time=None ,date=None) : 
         if current_time :
             self._book_borrowing_date = current_time
             return
         if date : 
             self._book_borrowing_date =  datetime.strptime(date,"%Y-%m-%d %H:%M:%S") if isinstance(date , str)  else date
             return

         raise ValueError ("Error :  book_borrowing_date is't has value ")
        
         
    def set_book_return_date(self,current_time=None , date=None) : 
         if current_time :
             self._book_return_date = current_time+ timedelta(minutes=getattr(Policies, "Borrowing_Period", "Attribute not found"))
             return
         if date : 
             self._book_return_date =  datetime.strptime(date,"%Y-%m-%d %H:%M:%S") if isinstance(date , str)  else date
             return 
            

         raise ValueError ("Error :  book_return_date is't has value ")

        

    def get_book_borrowing_date(self) : 
        return self._book_borrowing_date.strftime("%Y-%m-%d %H:%M:%S") if  self._book_borrowing_date else  "Error: No Date is set"
    
    def get_book_return_date(self) : 
        return self._book_return_date.strftime("%Y-%m-%d %H:%M:%S") if  self._book_return_date else  "Error: No Date is set"
    
    def get_member_expiration_date (self) : 
        return datetime.strftime(self._member_expiration_date, "%Y-%m-%d %H:%M:%S") if self._member_expiration_date else "This Field is Empty"
    
    def get_membership_date (self) : 
        return self._membership_date if self._membership_date else "This Field is Empty"
    

    def borrow_book(self ,book_id):
        """
    Allows a Member to Borrow a Book if the Membership is Valid and the Borrowing Limits Are Not Exceeded.

    Args:
        Book_id (int): The ID of the Book to Be Borrowed.

    Process:
        - Retrieves the Number of Books Currently Borrowed by the Member.
        - Retrieves the Current Member ID Associated with the Book (Before Borrowing Process).
        - Checks if the Member's Membership is Still Active by Comparing the Expiration Date.
        - Ensures the Number of Borrowed Books Does Not Exceed the Limit Defined in the Policies.

    Actions:
        - If Membership is Valid and Limits Are Not Exceeded, Updates the Book's Record to Assign It to the Member.
        - Sets the Borrowing Date to the Current Time and Calculates the Return Date Based on the Borrowing Period from Policies.
        - If the Book is Already Borrowed by the Same Member, a Warning is Shown.
        - If the Membership is Expired or the Limits Are Exceeded, Borrowing is Denied.

    Returns:
        None: Outputs a Message Indicating Whether the Book Was Successfully Borrowed or if an Error Occurred (Expired Membership, Book Already Borrowed, or Borrowing Limit Reached).
        """
        query = f"SELECT COUNT(*) AS book_count FROM book WHERE member_id = {self._member_id};"
        num_of_borrowed_books = DataBaseConnection.Direct_Query(query=query)[0]


        current_member_id_of_book = DataBaseConnection.query("book" ,f"WHERE id = {book_id}" ,"member_id")
        Borrowing_Limits = getattr(Policies , "Borrowing_Limits") 
        if self._member_expiration_date <  datetime.now()    : 
            print ("\nSorry 😟 , Your Membership is Expired  ")
            return

        if num_of_borrowed_books > Borrowing_Limits : 
                print("\nSorry 😟, You Have Exceeded Your Borrowing Limit. Please Return a Book Before Borrowing Another One.")
                return
        
        if  current_member_id_of_book[0][0] == self._member_id : 
                print ("\nOHH 🤦‍♂️ ,This Book Already is Borrowed By You ")
                return
        if  current_member_id_of_book[0][0] != None : 
                print ("\nOoops ! 🤦 ,This Book Already is Borrowed By Another One  ")
                return     

        DataBaseConnection.update_columns("book" , f"WHERE id ={book_id} " , member_id = self._member_id  )
        self.set_book_borrowing_date(current_time=datetime.now()) 
        self.set_book_return_date(current_time=datetime.now())
        DataBaseConnection.update_columns("book" , f"WHERE id  = {book_id}" , book_borrowing_date=self._book_borrowing_date , book_return_date=self._book_return_date)
        print( "\nOK ✅ , Please Return Book on Time ‼")     


    def view_borrowed_books(self):    # This Method is in Testing 
        self.__borrowed_books = DataBaseConnection.query("book" ,f" WHERE member_id = {self._member_id}" , "id" , "title" , "author" , "bookGenre" , "book_borrowing_date" , "book_return_date") 
        return self.__borrowed_books

    def return_book(self ,book_id):
        """
        Handles the return process of a book by a library member. It checks if the 
        current member is the one who borrowed the book, checks if the book is being 
        returned late, calculates fines if necessary, and updates the database to 
        reflect the return.
    
        Args:
            book_id (int): The unique ID of the book to be returned.
    
        Returns:
               None
        """
        current_member_id_of_book = DataBaseConnection.query("book" ,f"WHERE id = {book_id}" ,"member_id")[0][0]

        if current_member_id_of_book != self._member_id : 
            print("This book is not yours to return !! ")
            return
        if datetime.now() > self._book_return_date : 
            old_fine = self._fine_due if self._fine_due else 0 
            self._fine_due += (datetime.now() - self._book_return_date).days * getattr(Policies ,"Fines" )
            print(f"You are late, sorry, you have to pay the due fine of this book, which is = {self._fine_due - old_fine}")
            if old_fine : 
                print(f"Sorry, you also need to pay the old due fine, which is = {old_fine}")

            self.pay_fine()
            DataBaseConnection.update_columns('book' , f'WHERE id = {book_id}' ,member_id=None)
            return
        else : 
            DataBaseConnection.update_columns('book' , f'WHERE id = {book_id}' ,member_id=None)
            print("Thank you for returning the book on time. You are a disciplined member 👌 .")

    def pay_fine(self):
        """
        Initiates the fine payment process for the library member. Asks the member if 
        they want to pay the fine now or later, and updates the database accordingly.
        Returns:None
        """
        choice = input("Do you want to pay the fine now or later ? (Yes or No ) : ").lower()
        while True :
            if choice == 'y' or choice == 'yes' or choice == '1' : 
                self._fine_due = 0 
                DataBaseConnection.update_columns("member", f"WHERE id = {self._member_id}",fine_due = 0)
                print("OK , The amount has been paid")
                break
            elif choice == 'no' or choice == 'n' or choice == '0'  : 
                print("OK")
                DataBaseConnection.update_columns("member", f"WHERE id = {self._member_id}",fine_due = self._fine_due)
                break 
            else : 
                choice = input("Please Enter Right Choice : ")



    def get_fine_due (self) :
        return self._fine_due 




