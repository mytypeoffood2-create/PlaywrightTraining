import pytest
from playwright.sync_api import Playwright,Page,expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    sun_checkbox = page.get_by_label("Sunday")
    sun_checkbox.check()
    expect(sun_checkbox).to_be_checked()

    page.wait_for_timeout(500)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# count number of checkboxes present on a page

def test_checkbox2(page: Page):                                                                    # Checkbox test shuru kar rahe hain, taaki website ke checkboxes test kar sakein.
    page.goto("https://testautomationpractice.blogspot.com/")                                      # Website khol rahe hain, kyunki checkboxes isi page par hain.

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday" , "Friday", "Saturday"]         # Hafte ke 7 din likh rahe hain, taaki har din ka checkbox dhoondh sakein.
    checkboxes = []                                                                                # Khali list bana rahe hain, taaki milne wale saare checkbox isme jama kar sakein.
    print("Days list:", days)                                                                      # List ke saare din print kar rahe hain, taaki dekh sakein ki list mein kya-kya hai.

    for day in days:                                                                               # Ek-ek din uthakar check kar rahe hain, taaki kisi bhi din ka checkbox chhoot na jaye.
        checkbox = page.get_by_label(day)                                                          # Us din ke naam se checkbox dhoondh rahe hain, taaki sahi checkbox mil sake.
        checkboxes.append(checkbox)                                                                # Mile hue checkbox ko list mein rakh rahe hain, taaki baad mein sabko ek saath select kar sakein.
        print("checkbox name:", day)                                                               # Din ka naam print kar rahe hain, taaki pata chale kaunsa checkbox mila.
        print("number of checkbox:", len(checkboxes))                                              # List mein jama checkboxes gin rahe hain, taaki pata chale ab tak kitne mile.

# Ab saare checkboxes select karke verify karenge.

    for checkbox in checkboxes:                                  # Jama kiye hue checkboxes ko ek-ek karke nikaal rahe hain, taaki sab par kaam ho sake.
        checkbox.check()                                         # Checkbox par tick laga rahe hain, taaki woh select ho jaye.
        expect(checkbox).to_be_checked()                         # Check kar rahe hain ki tick laga ya nahi, taaki test galat selection par fail ho.

        page.wait_for_timeout(500)                              # Ek second ruk rahe hain, taaki agla checkbox select hone se pehle humein change dikhe.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# check last three checkboxes

    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
    print("checkbox list:", days)


    page.wait_for_timeout(1000)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Randomly check selected checkboxes

    index = [1, 2, 3]                               # In numbers ko choose kar rahe hain, taaki list ke specific checkboxes select hon.

    for i in index:                                 # Har index ko ek-ek karke access kar rahe hain.
        checkbox = page.get_by_label(days[i])       # Index se din ka naam lekar uska actual checkbox dhoondh rahe hain.
        checkbox.check()                            # Checkbox par tick laga rahe hain.
        expect(checkbox).to_be_checked()            # Verify kar rahe hain ki checkbox select hua.
        print("Checked checkbox:", days[i])         # Terminal mein selected checkbox ka naam dikha rahe hain.




# pytest -v -s test_checkbox.py::test_last_checkbox --headed










 # pytest -v -s test_checkbox.py --headed
