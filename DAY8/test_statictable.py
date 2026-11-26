# STATIC TABLES
# Static Table ek aisi table hoti hai jisme data pehle se fixed hota hai aur runtime par automatically change nahi hota.
# Example: HTML mein normal `<table>` jisme rows aur columns manually likhe hote hain.

# Inside <tbody> the <tr> tag represent  columns & header in DOM
# <th> represent particular header of row                Name | Age | Location
# <td> represent the values of particular column         wali | 22  | Delhi

###################################################################################################################################################################




import pytest
from playwright.sync_api import Page, expect

def test_statictable(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")  # go to website
    table = page.locator("table[name='BookTable'] tbody")       # locating table
    expect(table).to_be_visible()                               # confirming visibility

# Now count the total number of rows in this table

    rows = table.locator("tr")            # table name BookTable hai iske Tbody me puri table hai or tr me sare columns hain
    expect(rows).to_have_count(7)

    count = rows.count()
    print("there are :",count,"rows")


# count total number of columns and headers

    column = table.locator("th")
    expect(column).to_have_count(4)

    count1 = column.count()
    print("there are :",count1,"columns")

# Now read all the data from 2nd row

    second_row = rows.nth(2).locator("td")
    row2 = second_row.all_inner_texts()

    print("Second Column data ===>",row2)

    for i in row2:
        print(i)



# Read all the data from table excluding header / each row's data

    all_rows_data = rows.all()                        # Table ki saari rows ko list mein store kiya.

    for row in all_rows_data[1:]:                     # First row (header) ko skip karke baaki rows par loop chalaya.

        cols = row.locator("td").all_inner_texts()    # Current row ke sabhi columns ka text list mein nikala.

        print(cols)                                   # Current row ke saare column values print kiye.



# Print Book name where Author is Mukesh

    for row in all_rows_data[1:]:                               # First row (header) ko skip karke baaki rows par loop chalaya.
        author_name = row.locator("td").nth(1).inner_text()     # Second column <td> se author ka naam nikala. nth(1) ka inner text

        if author_name == "Mukesh":                             # Check kiya ki author ka naam Mukesh hai ya nahi.
            Book_Name = row.locator("td").nth(0).inner_text()   # First column <td> se book ka naam nikala.
            print(author_name, ":", Book_Name)                  # Author aur book ka naam print kiya.




# Calculate total price of all the books from last row
    total_price = 0
    for row in all_rows_data[1:]:

        price = row.locator("td").nth(3).inner_text()
        total_price+= int(price)
        print("Total price:", total_price)





# pytest -v -s test_statictable.py --headed
