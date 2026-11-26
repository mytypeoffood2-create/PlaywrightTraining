# PLAYWRIGHT METHODS
from itertools import count, product

# inner_text()       V/S   text_contenet()
# all_inner_text()   V/S   all_text_content()
# all()

###################################################################################################################################
import pytest
from playwright.sync_api import Page,expect

def test_comparison_of_method(page : Page):
    page.goto("https://demowebshop.tricentis.com/")
    products = page.locator("h2.product-title")

    print("######################################## inner_text()    V/S   text_contenet() ########################################")


# NOW DIFFERENCE BETWEEN   inner_text()    V/S   text_contenet()

    print("Using inner_text()   ==>",products.nth(1).inner_text())      # It returns actual text
    print("Using text_content() ==>",products.nth(1).text_content())    # it returns text with spaces and special characters


    # inner_text() - Actual text
    # text_content() - text + spaces + special characters
    # if you want to use text_content() without getting spacec or special character
    # so use .strip() while printing statement with

    print("######################################## text_content() with strip() ########################################")


    # EX -    text_content() with strip()

    count = products.count()   # products.count() to count variable m store kara
    for i in range (count):    # loop
        product_name = products.nth(i).text_content()   # first product ka text lia site se usko product_name ke variable m store kar lia
        print("Product Name:", product_name.strip())    # product_name print kara strip k sath

    # ye zyada lamba process h isi liye better to use inner_text()



    print("########################################_all_inner_text()____V/S____all_text_content()_########################################")

# NOW DIFFERENCE BETWEEN   all_inner_text()   V/S   all_text_content()

    product_name2 = products.all_text_contents()   # using all_text_content()
    print(product_name2)

    print("-------------------------------------------------------------------------------------------------------------------------------------------------")

    product_name3 = products.all_inner_texts()     # using all_inner_text()
    print(product_name3)




# all()

# pehle ham nth() method ka use kar rhe h the sare products me se kisi ek ko laane ke liye
# but ab ham index ki madad se product select karenge or print karenge
# uske liye pehle LOCATOR ko list me convert  kar denge phir list se easily without nth() method ham index se karenge

    product_locator = products.all()
    print("YE RAHA:",product_locator[1].inner_text())





















# pytest -v -s test_playwright_methods.py --headed