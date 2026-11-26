import pytest
from playwright.sync_api import Playwright,Page,expect

def test_radio_buttons(page: Page):  # Radio button testing ke liye test function hai.
    page.goto("https://testautomationpractice.blogspot.com/")  # Website open karta hai.

    radio_button = page.locator("#male")        # ID male ke through radio button locate karta hai.
    expect(radio_button).to_be_visible()        # Check karta hai ki radio button visible hai.
    expect(radio_button).to_be_enabled()        # Check karta hai ki radio button enabled hai.

    expect(radio_button).not_to_be_checked()    # Check karta hai ki radio button selected nahi hai.
    radio_button.check()                        # Radio button ko select karta hai.


    radio_button.check()                        # Radio button ko select karta hai.
    expect(radio_button).to_be_checked()        # Verify karta hai ki radio button select ho gaya hai.

    page.wait_for_timeout(5000)

# pytest -v -s test_radio_buttons.py --headed