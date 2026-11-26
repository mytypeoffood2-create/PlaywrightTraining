# LOCATORS IN PLAYWRIGHT            Yaad rakho: Locate → Action → Validate.
from playwright.sync_api import Page


# Inke through hum website ke elements ko identify karke un par actions perform karte hain.

# Locator ka matlab hai website ke kisi Web Element ko identify ya locate karna.

# Example: Website par Login button hai. Playwright ko batana padega ki Login button kahan hai.
# Iske liye Locator use hota hai.

#=============================================================================================================================================

# Web Automation ke 3 main steps

# 1. Identifying / Locating the Web Elements

# Website par jis element par kaam karna hai, use identify karna.

# Example: Login button, Username field, Password field.
#----------------------------------------------------------------------------------

# 2. Performing Actions
# Identify kiye gaye element par action perform karna.

# Example:
# - Click karna
# - Text fill karna
# - Checkbox select karna

#----------------------------------------------------------------------------------

# 3. Validations (Assertions)
# Check karna ki action ke baad expected result mila ya nahi.

# Example: Login karne ke baad Dashboard open hua ya nahi.

#=====================================================================================================================================

# Locating the Elements ke Methods
# Playwright mein elements locate karne ke 3 methods:

# 1. Playwright Built-in Locators
# Playwright ke already available locator methods.

# 2. XPath
# XPath ka use HTML structure ke through Web Element ko locate karne ke liye hota hai.

# 3. CSS Selector
# CSS Selector ka use HTML elements ki ID, Class aur attributes ke through locate karne ke liye hota hai.

#=========================================================================================================================================================

# These are the recommended built-in locators.

#1. page.getByRole()            to locate by explicit and implicit accessibility attributes.
#2. page.getByText()            to locate by text content.
#3. page.getByLabel()           to locate a form control by associated label's text.
#4. page.getByPlaceholder()     to locate an input by placeholder.
#5. page.getByAltText()         to locate an element, usually image, by its text alternative.
#6. page.getByTitle()           to locate an element by its title attribute.
#7. page.getByTestId()          to locate an element based on its data-testid attribute (other attributes can be configured).

#=========================================================================================================================================================
#7. page.getByAltText()       # Used to veify all type of images,logos, on web application

# question - site par logo present h ya nhi verify karo
import pytest

from playwright.sync_api import Page, expect

def test_verify_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")           # isko logo variable bana kar store kar dia
    expect(logo).to_be_visible()


# get_by_alt_text() = Image ke alt attribute se image locate karta hai.
# logo              = Located element ko variable mein store karta hai.
# to_be_visible()   = Check karta hai ki element screen par visible hai ya nahi.

#===============================================================================================================================================================================
#2. page.getByText()      web application par text content verify karne ke liye use hota h ke text h ya nhi web app par

def test_verify_text(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    text = page.get_by_text("Welcome to our store")
    expect(text).to_be_visible()

#===============================================================================================================================================================================
#1. page.getByRole()    ka use website ke elements ko unke role (type) aur accessible name ke basis par locate karne ke liye hota hai.

# 1. page.get_by_role()

def test_verify_eliment(page:Page):
    page.goto("https://demowebshop.tricentis.com/register")      # Register page open karta hai
    eliment = page.get_by_role(role="heading",name ="Register")  # Register naam ki heading ko locate karega
    expect(eliment).to_be_visible()                              # Check karta hai ki heading screen par visible hai ya nhi

#===============================================================================================================================================================================
#3. page.getByLabel()   ka use form ke input fields ko unke label ke basis par locate karne ke liye hota hai.
# Example: Username, Email, Password jaise fields ko locate karna.

def test_verify_label(page:Page):
    page.goto("https://demowebshop.tricentis.com/register")
    name = page.get_by_label("First name:").fill("wali")
    lastname = page.get_by_label("Last name:").fill("rizvi")
    Email = page.get_by_label("Email:").fill("walimdqa@gmail.com")
    page.wait_for_timeout(5000)

#===============================================================================================================================================================================
#4. page.getByPlaceholder()   website par un input boxes ko dhoondhta hai jinmein user kuch likh sakta hai,
# jaise Search Box, Email Box ya Password Box.

def test_verify_placeholder(page:Page):
    page.goto("https://www.youtube.com/")
    search = page.get_by_placeholder("Search")
    search.fill("Syed wali mohammad rizvi")
    page.wait_for_timeout(5000)
    search.press("Enter")

# pytest -v -s test_locators.py::test_verify_placeholder --headed

#===============================================================================================================================================================================
# 6. page.get_by_title()     # HTML element ke title attribute ki value se element locate karta hai.

def test_verify_title(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    title = page.get_by_title("Home page link")
    expect(title).to_be_visible()
    expect(title).to_have_text("Home")

# pytest -v -s test_locators.py::test_verify_title --headed

# short way
def test_verify_title2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")

# pytest -v -s test_locators.py::test_verify_title2 --headed

#=========================================================================================================================================================
#7. page.getByTestId()      unique data-testid se kisi bhi HTML element ko reliably locate karne ke liye kiya jata h

def test_verify_testid(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")


