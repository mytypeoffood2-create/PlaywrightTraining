# DIALOG IN PLAYWRIGHT PYTHON

# 1. Dialog kya hota hai?
# Dialog browser ka popup/message box hota hai.
# Ye user se interaction leta hai.

# 2. Dialog ke types:
# Alert       = Sirf message aur OK button.
# Confirm     = OK aur Cancel buttons.
# Prompt      = User se input leta hai.
# Beforeunload = Page leave karte waqt confirmation.

# 3. Dialog handle karna:

# page.on("dialog", lambda dialog: dialog.accept())
# Dialog open hone par automatically OK click karega.


# 4. Dialog handle karne ke methods:

# dialog.accept()       # OK click karta hai
# dialog.dismiss()      # Cancel click karta hai
# dialog.message       # Dialog ka message deta hai
# dialog.type          # Dialog ka type batata hai
# dialog.default_value # Prompt ki default value deta hai


# 5. Complete example:

# def handle_dialog(dialog):
#     print(dialog.type)       # Dialog ka type print karega
#     print(dialog.message)    # Dialog ka message print karega
#     dialog.accept()          # OK button click karega

# page.on("dialog", handle_dialog)
# Dialog event ko handle_dialog function se connect karta hai.

# page.locator("#alert").click()
# Alert button click karke dialog open karta hai.

####################################################################################################################################################

import pytest
from playwright.sync_api import Page,expect

@pytest.mark.skip    # ye is test ko skip kar dega kyunki dusra test dekhna h mujhe bs hata dena isko baad m
# STEP -1
def test_simple_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

# Registering an event
# STEP-3
    def handle_dialog(dialog):        # creating a nested another def function for STEP -2
        dialog.accept()

# STEP -2
    page.wait_for_timeout(3000)
    page.on("dialog",handle_dialog)    # registering an event before clicking dialog
    page.locator("#alertBtn").click()          # clicking on the button which opens dialog
    page.wait_for_timeout(5000)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# Using lambda() - agar ham ye use kare to function ke andar ek or def function yani nested function banaane ki zarurat nhi h

# STEP -1
def test_simple_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

# Registering an event with lambda
# STEP -2
    page.on("dialog", lambda dialog:dialog.accept())    # registering an event before clicking dialog
    page.wait_for_timeout(3000)
    page.locator("#alertBtn").click()                                  # clicking on the button which opens dialog
    page.wait_for_timeout(5000)









#   pytest -v -s test_dialog.py --headed