import pytest
from playwright.sync_api import Page, expect

# Multiple select in dropdown

# task 1  go to webpage select multiple options from a dropdown

def test_single_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#colors").select_option(["Red","Green","Blue"])  # by label
    page.wait_for_timeout(5000)

# method 2 through value

    page.locator("#colors").select_option(value=["White","Yellow","Green"])
    page.wait_for_timeout(5000)

# method 3 through index

    page.locator("#colors").select_option(index=[2,4,6])








# pytest -v -s test_multiple_select_dropdown.py --headed


