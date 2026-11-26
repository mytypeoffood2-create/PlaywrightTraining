# PAGINATION TABLE
#
# Pagination Table ek aisi table hoti hai jisme large data multiple pages mein divided hota hai.
#
# IMPORTANT FEATURES:
#
# 1. Search: Table mein data search karna.
# 2. Sorting: Data ko Ascending / Descending order mein arrange karna.
# 3. Show Entries: Ek page par kitni rows dikhani hain.
# 4. Next: Agle page par jaana.
# 5. Previous: Pichhle page par jaana.
# 6. Page Number: Direct kisi page par jaana.
# 7. Info: Total aur currently displayed records dekhna.
#
# PLAYWRIGHT:
# 1. locator() = Element locate karna.
# 2. all() = Saari matching rows collect karna.
# 3. nth() = Specific element select karna.
# 4. click() = Button click karna.
# 5. inner_text() = Text extract karna.
#
# IMPORTANT:
# Complete table data extract karne ke liye har page ko visit karna zaroori hai.

###################################################################################################################################################################

import pytest
from playwright.sync_api import Page,expect

def test_pagination_table(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")

    has_more_pages = True
    while has_more_pages:
        rows = page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())

        next_button = page.locator("button[aria-label='Next']")
        is_disabled = next_button.get_attribute("class")

        if "disabled" in is_disabled:
            has_more_pages = False
        else:
            next_button.click()



# Checking Filter row dropdown is working properly or not on web application

def test_filter_rows(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")
    dropdown = page.locator("#dt-length-0")
    dropdown.select_option("25")

    rows = page.locator("#example tbody tr")
    print("number of rows: ", rows.count())
    expect(rows).to_have_count(25)










#      pytest -v -s test_pagination_table.py --headed