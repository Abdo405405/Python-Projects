from tabulate import tabulate
from os import system


def clean_screen():
    system("cls")


class Menus:
    @staticmethod
    def Welcomed_Menu():
        clean_screen()
        Message = [
            ["Welcome To Libary Managment System"],
            ["Process", "Choice"],
            ["login", "1"],
            ["register", "2"],
        ]

        print(tabulate(tabular_data=Message, tablefmt="heavy_grid"))
        while True :
            try : 
                choice = int(input("Enter Your Choice ? (1-2) : ").strip())
                if choice == 1 :
                     return "login"
                elif choice==2 : 
                     return "register"
                else : 
                     return "Invalid Choice"
            except ValueError  :
                 print("Enter A Valid Choice") 
             

    def Login_Menu():
        clean_screen()
        Message = [
            ["Welcome To Login Page"],
            ["Process", "Choice"],
            ["Login as librarian", "1"],
            ["Login as Member", "2"],
            ["Return To Register Page", "3"],

        ]
        
        print(tabulate(tabular_data=Message, tablefmt="heavy_grid"))
        while True : 
            try : 
               choice = int(input("Enter Your Choice ? (1-3) : ").strip())
               processName = -1 if choice > 3 else Message[choice + 1][0] 

            except ValueError : 
                 print("Please Enter A Valid Choice ")
            
            else  : 
                return processName

                 
        

    @staticmethod
    def Librarian_Menu (user=None) : 
        clean_screen()
        Message = [
            ["Welcome To Login Page" , f"Hi {user}"],
            ["Process", "Choice"],
            ["Show All Books", "1"],
            ["Add New Book", "2"],
            ["Update Book", "3"],
            ["Delete Book", "4"],
            ["Add New Member", "5"],
            ["Add New librarian", "6"],
            ["Logout", "7"],
        ]

        print(tabulate(tabular_data=Message, tablefmt="heavy_grid"))
        choice = int(input("Enter Your Choice ? (1-7) : ").strip())
        processName = -1 if choice > 7 else Message[choice + 1][0] 
        return processName
    

    @staticmethod
    def Data_View(data , headers=None) : 
        clean_screen()
        
        if data : 
             print(tabulate(tabular_data=[sublist[:7] for sublist in data] ,headers=headers[:7] ,tablefmt="heavy_grid"))
        else : 
             print ("No Data To Show")

    @staticmethod
    def Updated_Menu () : 
        Message = [
            ["Enter A field That You want to Update It"],
            ["Field", "Choice"],
            ["title ", "1"],
            ["Author ", "2"],
            ["bookGenre ", "3"],
            ["publicationYear ", "4"],
            ["isAvailable", "5"],
            ["ISBN", "6"],
            ["Cancel", "7"],
            

        ]
       
        output =tabulate(tabular_data=Message ,tablefmt="heavy_grid")
        print(output)
        choice=int(input("Yout Choice ? (1-6) : "))
        return choice
    
    @staticmethod
    def Checking_Another_Update()  :
            clean_screen()
            Message = [
            ["Do you want to update another field"],
            ["Process", "Choice"],
            ["Yes", "1"],
            ["No", "2"],
        ]
            output =tabulate(tabular_data=Message ,tablefmt="heavy_grid")
            print(output)
            choice = input("Enter Your Choice :")
            clean_screen()
            # processName = -1 if choice > 2 else Message[choice + 1][0] 
            return choice
    

    @staticmethod 
    def Delete_Menu(name) :
            clean_screen()
            Message = [
            ["Are You Sure To Delete " , f"{name}"],
            ["Process", "Choice"],
            ["Yes", "1"],
            ["No", "2"],
        ]
            output =tabulate(tabular_data=Message ,tablefmt="heavy_grid")
            print(output)
            choice = int(input("Enter Your Choice : "))
            processName = -1 if choice > 2 else Message[choice + 1][0] 
            return processName
    
    @staticmethod 
    def Member_Menu (user=None) : 
        clean_screen()
        Message = [
            ["Welcome To Login Page" , f"Hi {user}"],
            ["Process", "Choice"],
            ["Show My Profile", "1"],
            ["Borrow Book", "2"],
            ["Return  Book", "3"],
            ["View My Books", "4"],
            ["Logout", "5"],
        ]

        print(tabulate(tabular_data=Message, tablefmt="heavy_grid"))
        choice = int(input("Enter Your Choice ? (1-6) : ").strip())
        processName = -1 if choice > 6 else Message[choice + 1][0] 
        return processName
    
    @staticmethod
    def Show_Profile(member) : 
            clean_screen()
            print(member)
            input("Enter , To Return Main Menu")
         
 


