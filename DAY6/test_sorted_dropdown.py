import pytest
from playwright.sync_api import Page, expect

# check dropdown is sorted or not

def test_single_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown_option = page.locator("#animals>option")    # sorted list
    # dropdown_option = page.locator("#colors>option")    # un-sorted list


    options_text = [text.strip() for text in dropdown_option.all_text_contents()]

    original_list = options_text.copy()    # this is un sorted
    sorted_list = sorted(original_list)    # this is sorted list

    # now we compare both lists to confirms list are same or different or in sequence
    # EX:-    A F S Y G M G Q E         UNSORTED
    #         A B C D E F G H I         SORTED

    print("Original list:", original_list)
    print("Sorted list:", sorted_list)



    if original_list==sorted_list:
        print("Dropdown options are sorted correctly")
    else:
        print("Dropdown options are not sorted correctly")


# pytest -v -s test_sorted_dropdown.py --headed


