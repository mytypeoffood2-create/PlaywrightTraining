# Bootstrap Dropdown
from itertools import count

# Normal dropdown: HTML ke <select> aur <option> tags se banta hai.

# Bootstrap dropdown: Usually <button> aur menu items se banta hai, jo click karne par open hote hain.
# Iske menu items DOM mein present hote hain, lekin shuru mein hidden ho sakte hain.
# Button par click karne ke baad dropdown menu visible ho jata hai
# Playwright mein Bootstrap Dropdown ko handle karne ke liye usually button par click() karte hain, phir required menu item par click() karte hain.
# Ismein select_option() use nahi hota, kyunki ye normal HTML <select> dropdown nahi hota.


import pytest
from playwright.sync_api import Page, expect

def test_bootstrap_dropdown(page: Page):                                                       # function banaya page class or object ke sath
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")  # site open karvaai

    page.locator("input[name='username']").fill("Admin")      # username fill karvaya site par
    page.wait_for_timeout(1000)
    page.locator("input[name='password']").fill("admin123")   # phir password fill karvaya site par
    page.wait_for_timeout(1000)
    page.click("button[type='submit']")                       # phir login button par click karvaya

    page.get_by_role("link", name="PIM").click()          # jab input kar ke id,class,attribute na mile or mile to kafi bada ho or ( text ho DOM me element ka ) to page.get_by_text() use karo
    page.wait_for_timeout(2000)



# now click on job title dropdown
    print(page.locator("form i").count())       # Maine check kiya ki form ke andar kitne i elements mil rahe hain.
    page.locator("form i").nth(2).click()       # ye nth(3) 3rd droopdown par click karvayega kyunki us page par kafi dropdowns hain form ke andar
    page.wait_for_timeout(2000)



# Important thing / Ab ham ko kisi ek  dropdown ke saare element ka text chahiye, lekin vahan DOM me options hidden dropdown ke, na class,object,attribute kuch nhi to uske liye

# STEP -1
# click on selector hub
#
# see right side on selectorHub 4th or on fifth number -  TURN ON DEBUGGER
#
# # STEP - 3
#
# DEBUGGER on karte hi Screen Freezed ho jayegi tab jo dropdown select karna h uspar turant click karo der mat lgana
#
# # STEP - 3
#
# aesa karne se  DEBUGGER start ho jayega uske baad
#
# ELEMENTS par jaao click karo
#
# uske baad jo dropdown tum ko test karna h Inspector ki madad se select kar ke us par click kar do


# AB HAM KO HIDDEN DROPDOWN LIST MIL GYI FINALLLY SO yahan print karvaate hain

    options = page.locator("div[role='listbox'] span")
    print(" All hidded dropdown's options =>",options.all_text_contents())

    print("---------------------------------------------------------------------------------------------------------------------------")

# Now i print all the options text using loop

    for text in options.all_text_contents():
        print(text)

    count = options.count()
    print(options.count())

# Now select or click on specific option in hidden dropdown

    for text in range(count):
        text2 = options.nth(text).inner_text().strip()
        if text2 == "Automaton Tester":
            options.nth(text).click()
            break

    page.wait_for_timeout(5000)





# pytest -v -s test_bootstrap_dropdown.py --headed