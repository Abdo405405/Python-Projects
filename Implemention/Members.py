from Person import Persons
from Database import DataBaseConnection
from InputHandler import InputHandler
from datetime import datetime ,timedelta
from Policies import Policies
from  Accounts import Account
from tabulate import tabulate
# Take care fields in Class != fields in database Here 
class Member(Persons):
    def __init__(
        self,
        id=None,
        name=None,
        phoneNumber=None,
        user_name=None,
        password=None,
        age=None,
        email=None,
        address=None,
        DOB=None,
        membership_date=None,
        member_expiration_date=None,
        membership_type=None,
        fine_due=None,
    ) -> None:
        
        if id==None and name==None and phoneNumber==None and user_name==None and password==None and age==None and email== None and address==None and DOB==None and membership_date==None and member_expiration_date ==None and fine_due==None and  membership_type==None:
            self._fine_due = None 
            self._membership_type = None
            self._membership_date =None
            self._member_expiration_date = None
            super().__init__()
        else :
            self._fine_due = fine_due 
            self._membership_type = membership_type
            self._membership_date =membership_date
            self._member_expiration_date = member_expiration_date
            self.account = Account(member_id=id , membership_date=membership_date , member_expiration_date=member_expiration_date ,membership_type=membership_type ,fine_due=fine_due )
            super().__init__(id=id ,name=name , phoneNumber=phoneNumber ,user_name=user_name,password=password ,email=email,age=age,address=address,DOB=DOB)

    
    @classmethod
    def with_data(cls, id,name, phoneNumber,user_name,password,age,email,address,DOB,membership_date,member_expiration_date,membership_type,fine_due):
        return cls(
        id=id,
        name=name,
        phoneNumber=phoneNumber,
        user_name=user_name,
        password=password,
        age=age,
        email=email,
        address=address,
        DOB=DOB,
        membership_date = membership_date,
        member_expiration_date=member_expiration_date , 
        membership_type=membership_type ,
        fine_due= fine_due 
        )
    
    def set_member_type (self) :
        print ("\nChoice Type OF Your MemberShip 👇")
        print("1 - MEMBERSHIP_5_MINUTES ")
        print("2 - MEMBERSHIP_10_MINUTES ")
        print("3 - MEMBERSHIP_15_DAY ")
        choices = {1  :"MEMBERSHIP_5_MINUTES" , 2 : "MEMBERSHIP_10_MINUTES" , 3 : "MEMBERSHIP_15_DAY" }
        while True : 
           choice = int(input("Enter Your Choice (1-3) : "))
           if 0 < choice <= 3  :
               self.__membership_type = choices[choice]
               self.create_account()
               break
           else : 
               print("INVALID MEMBERTYPE ")

    def get_member_type(self) : 
        return  self.__membership_type.name 
    

    def create_account(self) : 
        self.account = Account(member_id=self._id , membership_date=None , member_expiration_date=None ,membership_type=self.__membership_type , fine_due=0) 

    def get_member_info (self) : 
        info = self.get_personal_info()
        print(self._membership_type)
        membership_type = self._membership_type
        membership_date = self.account.get_membership_date()
        member_expiration_date = self.account.get_member_expiration_date()
        fine_due = self.account.get_fine_due()
        info["membership_date"] =membership_date
        info["member_expiration_date"] =member_expiration_date
        info["membership_type"] =membership_type 
        info["fine_due"] =fine_due
        return info 

    @classmethod
    def valid_Member(cls) : 
        username = input("Enter Username : ")
        password = input("Enter User Password : ")
        return DataBaseConnection.query(
            "member",
            f'Where user_name="{username}" AND password="{password}"',
            "*",
        )



    def __str__(self) -> str:
        headers = ["Attribute", "Value"]
        data = [
            ("ID", self._id),
            ("Name", self._name),
            ("Phone Number", self._phoneNumber),
            ("Username", self._user_name),
            ("Password", self._password),
            ("Age", self._age),
            ("Email", self._email),
            ("Address", self._address),
            ("DOB", self._DOB),
            ("Membership Date", self._membership_date),
            ("Member Expiration Date", self._member_expiration_date),
            ("Membership Type", self._membership_type),
            ("Fine Due", self.account.get_fine_due())
        ]
        
        return tabulate(data, headers, tablefmt="fancy_grid")

      
import time
if __name__ == "__main__" : 
    mem = Member(id=1)
    mem.account.borrow_book(book_id=6) 
    print(mem.account.get_book_borrowing_date())
    print(mem.account.get_book_return_date())
    print(mem.account.view_())
    time.sleep(4)
    print(mem.account.return_book())


