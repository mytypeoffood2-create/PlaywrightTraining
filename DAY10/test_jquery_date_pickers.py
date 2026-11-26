# JQUERY DATE PICKER

# jQuery Date Picker ek calendar widget hai, jisse user input field ya popup calendar se date select kar sakta hai.

# IMPORTANT FEATURES:
# 1. Calendar: Popup calendar open hota hai.
# 2. Previous: Pichhle month par jaana.
# 3. Next: Agle month par jaana.
# 4. Date Selection: Required date select karna.
# 5. Month/Year: Month aur year change karna.
# 6. Date Format: Date ka format set karna.
# 7. Date Range: Minimum aur maximum selectable date set karna.
# 8. Today: Current date select karna.

# IMPORTANT JQUERY CODE:
# $( "#datepicker" ).datepicker();

# Is code se input field par Date Picker initialize hota hai.

# PLAYWRIGHT:
# 1. locator() = Date input locate karna.
# 2. click() = Calendar open karna.
# 3. inner_text() = Calendar ka text read karna.
# 4. get_attribute() = Input ki value ya attribute check karna.
# 5. expect() = Selected date verify karna.

# IMPORTANT:
# Date Picker mein calendar se date select kar sakte hain ya input field mein date enter kar sakte hain.

#############################################################################################################################################

import pytest
from playwright.sync_api import Page, expect

# If fill() method is allowed in date picker or calendar on site

def test_jquery_date_pickers(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")

    # APROACH - 1   fill text in date input

    date_input.fill("12/21/2004")           # format - mm/dd/yyyy
    page.wait_for_timeout(5000)

    expect(date_input).to_have_value("12/21/2004")
    print("first test passed")

    # If fill() method is not allowed in date picker or calendar on site so...

    # TRUE IS next CALENDER KO AAGE LEJAANE KA LIKE      > JAN,FEB,MARCH,APR
    # FALSE IS previous CALENDER KO PEECHE LE JAANE KA LIKE <

    is_future = False
    year = "2004"
    month = "February"
    day = "21"

    date_input.fill("")
    date_input.click()

    select_date(page, year, month, day, is_future)


def select_date(page, target_year, target_month, target_day, is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").inner_text()
        current_year = page.locator(".ui-datepicker-year").inner_text()

        if current_month == target_month and current_year == target_year:
            break

        if is_future:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    # Selecting date from the date picker
    all_dates = page.locator(".ui-datepicker-calendar td").all()

    for dt in all_dates:
        date_text = dt.inner_text().strip()

        if date_text == target_day and dt.locator("a").count() > 0:
            dt.locator("a").click()
            break

    print("Selected date:", page.locator("#datepicker").input_value())
    page.wait_for_timeout(6000)


# pytest -v -s test_jquery_date_pickers.py --headed