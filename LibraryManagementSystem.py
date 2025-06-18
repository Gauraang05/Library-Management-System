#CREATING DATABASE
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="gaur2005")
mycursor=mydb.cursor()
mycursor.execute("Create database if not exists library_management_system")
mycursor.execute("use library_management_system")


#CREATING TABLES
mycursor.execute("create table if not exists card_holders(card_no int primary key, name varchar(50) not null, phone_no char(10) unique, address varchar(60), dob date)")
mycursor.execute("create table if not exists books(book_name varchar(30) not null, book_id int primary key, genre varchar(10), authors_name varchar(50), language varchar(15), quantity int)")
mycursor.execute("create table if not exists library_transactions(card_no int,foreign key(card_no) references card_holders(card_no), book_id int, foreign key(book_id) references books(book_id), book_name varchar(30), issue_date date, return_date date)")
mycursor.execute("create table if not exists ordered_books(order_id varchar(10) primary key, book_name varchar(30), delivery_date date, price int not null, quantity int not null)")
mydb.commit()


#TO CREATE A LIBRARY ACCOUNT
def create(): #1
 print("If you want to continue press 1")
 print("If you want to go back press 2")
 print(" ")
 a=int(input("Enter your choice:- "))
 if a==1:
     print("FILL ALL THE DETAILS OF ACCOUNT HOLDER")
     card_no=str(input("Enter card number:- "))
     name=str(input("Enter name (limit 50 characters):- "))
     phone_no=str(input("Enter phone number:- "))
     address=str(input("Enter address (limit 60 characters):- "))
     dob=str(input("Enter date of birth(yyyy-mm-dd):- "))
     mycursor.execute("insert into card_holders values('"+card_no+"','"+name+"','"+phone_no+"','"+address+"','"+dob+"')")
     mydb.commit()
     print("ACCOUNT IS SUCCESSFULLY CREATED!")

 """else:
 continue"""

                  
#TO SEE DETAILS OF CARD HOLDER
def details(): #2
 card_no=str(input("Enter card no:- "))
 mycursor.execute("select * from card_holders where card_no='"+card_no+"'")
 for i in mycursor:
     print(i)


#TO UPDATE INFORMATION OF CARD HOLDER
def update(): #3
 print("press 1 to update Name")
 print(" ")
 print("press 2 to update Phone Number")
 print(" ")
 print("press 3 to update Address")
 print(" ")
 print("press 4 to update Date Of Birth")
 print(" ")
 ch1=int(input("Choose from the above options:- "))


#TO UPDATE NAME
 if ch1==1:
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)
     card_no=str(input("Enter card number:- "))
     name=str(input("Enter new name:- "))
     mycursor.execute("update card_holders set name='"+name+"' where card_no='"+card_no+"'")
     mydb.commit()
     print("NAME HAS BEEN SUCCESSFULLY UPDATED!")
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)


#TO UPDATE PHONE
 elif ch1==2:
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)
     card_no=str(input("Enter card number:- "))
     phone_no=str(input("Enter new phone number:- "))
     mycursor.execute("update card_holders set phone_no='"+phone_no+"' where card_no='"+card_no+"'")
     mydb.commit()
     print("PHONE NUMBER HAS BEEN SUCCESSFULLY UPDATED!")
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)
                  

#TO UPDATE ADDRESS
 elif ch1==3:
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)
     card_no=str(input("Enter card number:- "))
     address=str(input("Enter new address:- "))
     mycursor.execute("update card_holders set address='"+address+"' where card_no='"+card_no+"'")
     mydb.commit()
     print("ADDRESS HAS BEEN UPDATED!")
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)

                  
#TO UPDATE DATE OF BIRTH
 elif ch1==4:
     mycursor.execute("select * from card_holders")
     for i in mycursor:
         print(i)
     card_no=str(input("Enter card number:- "))
     dob=str(input("Enter new date of birth(yyyy-mm-dd):- "))
     mycursor.execute("update card_holders set dob='"+dob+"' where card_no='"+card_no+"'")
     mydb.commit()
     print("DATE OF BIRTH HAS BEEN UPDATED!")
     mycursor.execute("select * from card_holders")
     for i in mycursor:
        print(i)

#INVALID CHOICE
 else:
    print("INVALID OPTION!")

                  
#TO DELETE AN ACCOUNT
def delete_account(): #4
 mycursor.execute("select * from card_holders")
 records=mycursor.fetchall();
 for record in records:
     print(record)
 card_no=str(input("Enter card number: "))
 mycursor.execute("delete from card_holders where card_no='"+card_no+"'")
 mydb.commit()
 print("ACCOUNT DELETED SUCCESSFULLY!")
 mycursor.execute("select * from card_holders")
 for i in mycursor:
    print(i)


#TO ADD NEW BOOK6
def new_book(): #5
 print("FILL ALL BOOK DETAILS")
 book_name=str(input("Enter book name:- "))
 book_id=str(input("Enter book id:- "))
 genre=str(input("Enter genre:- "))
 authors_name=str(input("Enter the author's name (max 50 characters):- "))
 language=str(input("Enter the language of book:- "))
 quantity=str(input("Enter quantity of book:- "))
 mycursor.execute("insert into books values('"+book_name+"','"+book_id+"','"+genre+"','"+authors_name+"','"+language+"', '"+quantity+"')")
 mydb.commit()
 print("BOOK ADDED SUCCESSFULLY!")
 for i in mycursor:
     print(i)


#TO SEE BOOK DETAILS
def book_details(): #6
 mycursor.execute("select * from books")
 for i in mycursor:
     print(i)


#TO UPDATE BOOK DETAILS
def update_bookdetails(): #7
 print("press 1 to update Book Name")
 print(" ")
 print("press 2 to update Genre")
 print(" ")
 print("press 3 to update Author's Name")
 print(" ")
 print("press 4 to update Language")
 print(" ")
 ch1=int(input("Choose from the above options:- "))

 
#TO UPDATE NAME
 if ch1==1:
     mycursor.execute("select * from books")
     for i in mycursor:
         print(i)
     book_id=str(input("Enter book id:- "))
     book_name=str(input("Enter new name:- "))
     mycursor.execute("update books set book_name='"+book_name+"' where book_id='"+book_id+"'")
     mydb.commit()
     print("BOOK NAME HAS BEEN UPDATED!")
     mycursor.execute("select * from books")
     for i in mycursor:
        print(i)


#TO UPDATE GENRE
 elif ch1==2:
     mycursor.execute("select * from books")
     for i in mycursor:
         print(i)
     book_id=str(input("Enter book id:- "))
     genre=str(input("Enter new genre:- "))
     mycursor.execute("update books set genre='"+genre+"' where book_id='"+book_id+"'")
     mydb.commit()
     print("GENRE HAS BEEN UPDATED!")
     mycursor.execute("select * from books")
     for i in mycursor:
        print(i)

 
#TO UPDATE AUTHOR'S NAME
 elif ch1==3:
     mycursor.execute("select * from books")
     for i in mycursor:
         print(i)
     book_id=str(input("Enter book id:- "))
     author=str(input("Enter new author's name:- "))
     mycursor.execute("update books set authors_name='"+author+"' where book_id='"+book_id+"'")
     mydb.commit()
     print("AUTHOR'S NAME HAS BEEN UPDATED!")
     mycursor.execute("select * from books")
     for i in mycursor:
        print(i)

                  
#TO UPDATE LANGUAGE
 else:
     mycursor.execute("select * from books")
     for i in mycursor:
         print(i)
     book_id=str(input("Enter book id:- "))
     language=str(input("Enter new language:- "))
     mycursor.execute("update books set language='"+language+"' where book_id='"+book_id+"'")
     mydb.commit()
     print("LANGUAGE HAS BEEN UPDATED!")
     mycursor.execute("select * from books")
     for i in mycursor:
        print(i)


#TO DELETE A BOOK
def delete(): #4
 mycursor.execute("select * from books")
 records=mycursor.fetchall();
 for record in records:
     print(record)
 book_id=str(input("Enter book id:- "))
 mycursor.execute("delete from books where book_id='"+book_id+"'")
 mydb.commit()
 print("BOOK DELETED SUCCESSFULLY!")
 mycursor.execute("select * from BOOKS")
 for i in mycursor:
    print(i)


#TO LEND A BOOK
def book_lend(): #9
 print("If you want to continue press 1")
 print("If you want to go back press 2")
 print(" ")
 a=int(input("Enter your choice:- "))
 if a==1:
     card_no=str(input("Enter card number:- "))
     book_id=str(input("Enter book id:- "))
     book_name=str(input("Enter book name:- "))
     issue_date=str(input("Enter issue date(yyyy-mm-dd):- "))
     print("If book not returned then enter(0000-00-00)")
     return_date=str(input("Enter return date(yyyy-mm-dd):- "))
     mycursor.execute("insert into library_transactions values('"+card_no+"','"+book_id+"','"+book_name+"', '"+issue_date+"','"+return_date+"')")
     mydb.commit()


#TO RETURN A BOOK
def book_return(): #10
 print("If you want to continue press 1")
 print("If you want to go back press 2")
 print(" ")
 a=int(input("Enter your choice:- "))
 """if a==2: continue"""
 if a==1:
     card_no=str(input("Enter card number:- "))
     return_date=str(input("Enter return date(yyyy-mm-dd):- "))
     mycursor.execute("update library_transactions set return_date='"+return_date+"' where card_no='"+card_no+"'")
     mydb.commit()


#TO SEE LENDING HISTORY
def lending_history(): #11
 card_no=str(input("Enter card no:- "))
 mycursor.execute("select * from library_transactions where card_no='"+card_no+"'")
 for i in mycursor:
     print(i)


#TO ORDER A NEW BOOK
def order_book(): #12
 order_id=str(input("Enter the order id:- "))
 book_name=str(input("Enter the name of the book:- "))
 delivery_date=str(input("Enter the delivery date of book(yyyy-mm-dd):- "))
 price=str(input("Enter the price of the book:- "))
 quantity=str(input("Enter number of books ordered:- "))
 mycursor.execute("insert into ordered_books values('"+order_id+"','"+book_name+"','"+delivery_date+"','"+price+"', '"+quantity+"')")
 mydb.commit()


#TO UPDATE ORDER DETAILS
def update_orderdetails(): #13
 print("Press 1 to update the name of book")
 print(" ")
 print("Press 2 to update the delivery date")
 print(" ")
 print("Press 3 to update the price of the book")
 print(" ")
 ch1=int(input("Choose from the above options:- "))

 
#TO UPDATE BOOK NAME
 if ch1==1:
     mycursor.execute("select * from ordered_books")
     for i in mycursor:
         print(i)
     order_id=str(input("Enter order id:- "))
     book_name=str(input("Enter new name:- "))
     mycursor.execute("update ordered_books set book_name='"+book_name+"' where order_id='"+order_id+"'")
     mydb.commit()
     print("BOOK NAME HAS BEEN UPDATED SUCCESSFULLY!")
     mycursor.execute("select * from ordered_books")
     for i in mycursor:
        print(i)


#TO UPDATE DELIVERY DATE
 elif ch1==2:
     mycursor.execute("select * from ordered_books")
     for i in mycursor:
         print(i)
     order_id=str(input("Enter order id:- "))
     delivery_date=str(input("Enter new delivery date(yyyy-mm-dd):- "))
     mycursor.execute("update ordered_books set delivery_date='"+delivery_date+"' where order_id='"+order_id+"'")
     mydb.commit()
     print("DELIVERY DATE HAS BEEN UPDATED!")
     mycursor.execute("select * from ordered_books")
     for i in mycursor:
        print(i)

                  
#TO UPDATE PRICE
 if ch1==3:
    mycursor.execute("select * from ordered_books")
    for i in mycursor:
        print(i)
    order_id=str(input("Enter order id:- "))
    price=str(input("Enter new price:- "))
    mycursor.execute("update ordered_books set price='"+price+"' where order_id='"+order_id+"'")
    mydb.commit()
    print("PRICE HAS BEEN UPDATED!")
    mycursor.execute("select * from ordered_books")
    for i in mycursor:
        print(i)


#TO DISPLAY ORDERING HISTORY
def order_history(): #14
 order_id=str(input("Enter order id:- "))
 mycursor.execute("select * from ordered_books where order_id='"+order_id+"'")
 for i in mycursor:
     print(i)


#MAIN     
while True:
 print("\n")
 print("*"*80)
 print("1. Create a new account")
 print("2. See card holder details")
 print("3. Update card holder info")
 print("4. Delete the account")
 print("5. Add a new book")
 print("6. See books")
 print("7. Update book details")
 print("8. Delete a book")
 print("9. Lend a book")
 print("10. Return a book")
 print("11. Display lending history")
 print("12. Order a new book")
 print("13. Update order details")
 print("14. Display ordering history")
 print("15. Exit")
 print("*"*80)
 print("\n")
 ch=int(input("Enter your choice:- "))
 if ch == 1:
     create()
 elif ch == 2:
     details()
 elif ch == 3:
     update()
 elif ch == 4:
     delete_account()
 elif ch == 5:
     new_book()
 elif ch == 6:
     book_details()
 elif ch == 7:
     update_bookdetails()
 elif ch == 8:
     delete()
 elif ch == 9:
     book_lend()
 elif ch == 10:
     book_return()
 elif ch == 11:
     lending_history()
 elif ch == 12:
     order_book()
 elif ch == 13:
     update_orderdetails()
 elif ch == 14:
     order_history()
 else:
     break
