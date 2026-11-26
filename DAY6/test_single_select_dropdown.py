# DROPDOWNS
# 1 - SELECT DROPDOWNS
# Having 'select' tag in DOM
# Options are embedded in 'option' tag

# A - single select     # B - multiple select

#---------------------------------------------------------------------------
# BOOTSTRAP DROPDOWN
# Having div / button tags
# Options are embedded inside the div tag only

#---------------------------------------------------------------------------
# HIDDEN DROPDOWNS
# Options are hidden from the DOM

############################################################################################################################################
import pytest
from playwright.sync_api import Page, expect


# Single select dropdown

# task 1  go to webpage select India country from dropdown

#       method - 1 through label
def test_single_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//select[@id='country']").select_option("India")  # through by label
    page.wait_for_timeout(5000)

#       method - 2 through index

    dropdown = page.locator("//select[@id='country']")   # through index 7
    dropdown.select_option(index=7)
    value = dropdown.input_value()
    print("according to your index:", value)

    page.wait_for_timeout(5000)

# task 2  how to check no. of options in dropdown      Tag/attribute > option


    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text = [text.strip()  for text in dropdown_options.all_text_contents()]
    print("FULL LIST:", options_text)
    page.wait_for_timeout(1000)

    for option in options_text:             # print countries using loop()
        print(option)






# pytest -v -s test_single_select_dropdown.py --headed


