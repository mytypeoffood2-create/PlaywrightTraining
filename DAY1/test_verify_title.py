# HOW TO verify url and HOW TO  TEST THE title OF WEB APPLICATION

from playwright.sync_api import Page, expect


# TO TEST URL OF WEB APP
def test_verify_url(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    my_url = page.url
    print("this is my url", my_url)
    expect(page).to_have_url("https://demowebshop.tricentis.com/")


# TO TEST AND VERIFY THE TITLE OF WEB APP
def test_verify_title(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    my_title = page.title()
    print("this is my title", my_title)
    expect(page).to_have_title("Demo Web Shop")


# use this to run in terminal -    python -m pytest -v -s test_verify_title.py::test_verify_title --headed      /  ye 1st command: Sirf test_verify_title function run karega
# pytest -v -s test_verify_title.py  --headed --browser firefox                                                 / or agar ye use karo to 2nd command: test_verify_title.py file ke saare tests Firefox browser mein run karega.
# pytest -v -s test_verify_title.py --headed --numprocesses 2                                                   / --numprocesses 2  Tests ko 2 parallel workers mein run karta hai.

# 1. python:            Python interpreter ko command deta hai.
# 2. -m:                Python ko bolta hai ki kisi module ko run karo.
# 3. pytest:            Pytest testing framework ko run karta hai.
# 4. -v:                Verbose, yani detailed test results dikhata hai.
# 5. -s:                Test ke print() statements ka output dikhata hai.
# 6. test_verify_title.py:    Tumhari test file ka naam hai.

# Yaad rakhna:

# -v = Detailed result
# -s = Print output
# pytest = Testing framework
# python -m = Python ke through module run karna.