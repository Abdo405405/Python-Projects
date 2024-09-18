import mysql.connector


class DataBaseConnection:

    @classmethod
    def enable_connection(cls):
        cls.mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="library_system"
        )
        cls.mycursor = DataBaseConnection.mydb.cursor()

    @classmethod
    def add_data(cls, table_name, **kwargs):
        # Make connection to The Database
        cls.enable_connection()
        # Ensure the table name is correct
        col = ",".join([f"`{key}`" for key in kwargs.keys()])

        # Handle possible SQL injection issues
        values = tuple(
            [
                f"{value}" if isinstance(value, str) else value
                for value in kwargs.values()
            ]
        )
        len_values = len(values)
        numOfs = len_values * "%s,"
        numOfs = numOfs[:-1]  # Remove the trailing comma

        # Fix the table name and check for reserved keywords
        sql = f"INSERT INTO {table_name} ({col}) VALUES ({numOfs})"
        try:
            cls.mycursor.execute(sql, values)
            DataBaseConnection.mydb.commit()
            # print(cls.mycursor.rowcount, "record inserted.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    @classmethod
    def query(
        cls, table_name, condition, *searched_fields
    ):  # Notice The order of searched fields is essential because fetched data is correpont it
        cls.enable_connection()
        searched_fields = ",".join(searched_fields)
        sql = f"SELECT {searched_fields} from {table_name}  {condition}"
        try:
            cls.mycursor.execute(sql)
            result = cls.mycursor.fetchall()
        except mysql.connector.errors as err:
            print(f"Error: {err}")
        else:
            return result

    @classmethod
    def set_up_database(cls):
        cls.enable_connection()
        # Create the database
        cls.mycursor.execute("CREATE DATABASE IF NOT EXISTS library_system;")

        cls.mycursor.execute("USE library_system;")

        cls.mycursor.execute(
            """
CREATE TABLE IF NOT EXISTS member (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255), 
    phoneNumber VARCHAR(14), 
    user_name VARCHAR(255), 
    password VARCHAR(255), 
    age INT, 
    email VARCHAR(255), 
    address VARCHAR(250),
    DOB DATE,  
    membership_date DATETIME, 
    member_expiration_date DATETIME,  
    membership_type varchar(250) ,
    fine_due float
);
         """
        )


        cls.mycursor.execute(
            """
CREATE TABLE IF NOT EXISTS book (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    title VARCHAR(255), 
    publicationYear DATE, 
    author VARCHAR(300), 
    ISBN VARCHAR(255),  
    isAvailable BOOL, 
    bookGenre VARCHAR(250),
    member_id INT,  -- Added foreign key to link to member
    book_borrowing_date DATETIME , 
    book_return_date DATETIME , 

    FOREIGN KEY (member_id) REFERENCES member(id) ON DELETE SET NULL
);

         """
        )


        # Create the 'librarian' table
        cls.mycursor.execute(
            """
         CREATE TABLE IF NOT EXISTS librarian (
             id INT AUTO_INCREMENT PRIMARY KEY, 
             user_name VARCHAR(255) ,
             name VARCHAR(255), 
             age INT, 
             email VARCHAR(300), 
             address VARCHAR(255), 
             phoneNumber VARCHAR(14), 
             password VARCHAR(200), 
             DOB VARCHAR(100), 
             hire_date DATE, 
             years_of_experience INT
         )
         """
        )

    @classmethod
    def columns_names (cls ,table_name) : 
        cls.enable_connection()
        cls.mycursor.execute(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' ;"

        )
        result=cls.mycursor.fetchall()
        column_names = [r[0] for r in result]
            
        return column_names
    
    @classmethod
    def update_columns(cls,table_name , condition , **updated_fields) :
        cls.enable_connection()
        for field , value in updated_fields.items() :
            try: 
                if value == None  : 
                    sql = f"UPDATE {table_name} SET {field} = NULL  {condition};"

                else : 
                    sql = f"UPDATE {table_name} SET {field} = '{value}'  {condition};"
                cls.mycursor.execute(sql)
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            else:
                cls.mydb.commit()
                # print(cls.mycursor.rowcount, "value updated.")

    @classmethod 
    def Delete (cls , table_name ,id) : 
        cls.enable_connection()
        sql = f"DELETE FROM {table_name} WHERE id = %s" 
        try:
            cls.mycursor.execute(sql , (id,))
        except mysql.connector.errors as err : 
            print(f"Error : {err}")
        else : 
            cls.mydb.commit() 
            print(cls.mycursor.rowcount , "is Deleted ")

    @classmethod 
    def Direct_Query(cls , query) : 
        cls.enable_connection()
        try: 
                cls.mycursor.execute(query)
        except mysql.connector.Error as err:
                print(f"Error: {err}")

        else : 
            return cls.mycursor.fetchone()
        



if __name__ == "__main__":
    d = DataBaseConnection()
    d.set_up_database()




