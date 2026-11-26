import pytest
from playwright.sync_api import Page,expect



# CHECKIN DATE TABLE

def select_checkin_date(page, year, month, day):                                # yahan ek function bana lia jisme apne banaaya parameter or function add kar dia
    checkin_month_year = page.locator("h3[aria-live='polite']").nth(0).inner_text()      # (TimeoutError i dont know why)    # do element same tags class attribute hone ki vajah se nth method nth(0) pehla element
    current_month,current_year = checkin_month_year.split(" ")                           # Yahan 2 variables ek sath bana kar store kar dia like a,b = 2,4
                                                                                         # split() is liye ke (month year) DOM me ek sath h just like this   xpath="1">November 2026</h3>  or ham ko alag alag chahiye
    while True:

        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()    # go to the next month

        all_dates = page.locator("table.b8fcb0c66a tbody").nth(0).locator("td").all()

        for date in all_dates:
            if date.inner_text() == day:
                date.click()
                break



# CHECKOUT DATE TABLE

def select_checkout_date(page, year, month, day):
    checkout_month_year = page.locator("h3.e7addce19e.af236b7586").nth(1).inner_text()
    current_month,current_year = checkout_month_year.split(" ")

    while True:


        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()    # go to the next month

        all_dates = page.locator("table.b8fcb0c66a tbody").nth(1).locator("td").all()

        for date in all_dates:
            if date.inner_text() == day:
                date.click()
                break















def test_booking_datepicker(page: Page):
    page.goto("https://www.booking.com/index.en-gb.html?aid=304142&label=mkt123sc-78e39621-9162-4eab-9a98-d87bfbedfe01&chal_t=1795643811057&force_referer=")

    page.get_by_test_id("searchbox-dates-container").click()

# creating own parameters or functions
    select_checkin_date(page,"2025","October","10")
    select_checkout_date(page,"2025","November","5")

    checkin_text = page.locator("button span span[data-testid='date-display-field-start']").inner_text()
    checkout_text = page.locator("button span span[data-testid='date-display-field-end']").inner_text()

    print("CHECK-IN DATE:",checkin_text)
    print("CHECK-OUT DATE:",checkout_text)

    expect(page.locator("button span span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("button span span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)




    Page.wait_for_timeout(5000)






#    pytest -v -s test_bootstrap_date_picker.py --headed