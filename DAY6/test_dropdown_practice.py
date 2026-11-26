import pytest
from playwright.sync_api import Page, expect

def test_single_dropdown(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")  # Website open karo

    dropdown_list = page.locator("#colors>option")  # Colors dropdown ke saare options locate karo
    # dropdown_list = page.locator("#animals>option")  # Animals dropdown check karne ke liye is line ko use karo

    options_text = [text.strip() for text in dropdown_list.all_text_contents()]  # Saare options ka text read karo aur extra spaces hatao

    original_list = options_text.copy()  # Original options ki alag copy banao, taaki original order safe rahe

    sorted_list = sorted(original_list)  # Original list ki alphabetical sorted copy banao

    print("Original list is:", original_list)  # Dropdown ka original order print karo
    print("Sorted list is:", sorted_list)  # Alphabetical order wali list print karo

    if sorted_list == original_list:  # Check karo dono lists ka order same hai ya nahi
        print("Sorted dropdown")  # Same order hai, matlab dropdown already sorted hai
    else:
        print("Unsorted dropdown")  # Order different hai, matlab dropdown unsorted hai

# pytest -v -s test_dropdown_practice.py --headed  # Test run karne ki command