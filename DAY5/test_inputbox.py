import pytest
from playwright.sync_api import Playwright,Page,expect

def test_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box = page.locator("#name")

# checking visibility of element

    expect(text_box).to_be_visible()

# checking element enable or not means working or not

    expect(text_box).to_be_enabled()

# check the attribute of the elements

    expect(text_box).to_have_attribute("maxlength","15")

# Get the value of any attribute

    value = text_box.get_attribute("maxlength")
    print("Max length is:",value)

    id = text_box.get_attribute("id")
    print("ID is:",id)

    PlaceHolder = text_box.get_attribute("placeholder")
    print("PlaceHolder is:",PlaceHolder)

# fill the text

    text_box.fill("Allah hu Akbar")

# Get the input value from the input box

    print("your entered value is:",text_box.input_value())


    page.wait_for_timeout(5000)

