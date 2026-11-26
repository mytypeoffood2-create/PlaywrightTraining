# DYNAMIC TABLE
# Dynamic Table mein data change hota rehta hai.
# Goal: Chrome ka current CPU Load nikaalna aur verify karna.

# Dynamic Table ek aisi table hoti hai jisme data runtime par change hota rehta hai.
#
# IMPORTANT POINTS:
#
# 1. Changing Data: Table ki values automatically change hoti rehti hain.
# 2. Rows: Table mein multiple records hote hain.
# 3. Dynamic Value: CPU Load jaise values continuously update ho sakti hain.
# 4. Locator: Required row aur column ko locate karna.
# 5. Loop: Har row ko ek-ek karke check karna.
# 6. Condition: Required record ko identify karna.
# 7. Break: Required record milne par loop stop karna.
# 8. Assertion: Extracted value ko page ke displayed text se verify karna.
#
# PLAYWRIGHT:
# 1. locator() = Element locate karna.
# 2. all() = Matching elements ki list banana.
# 3. nth() = Specific column select karna.
# 4. inner_text() = Text extract karna.
# 5. has-text() = Specific text wala element locate karna.
# 6. expect() = Result verify karna.
#
# IMPORTANT:
# Dynamic Table mein fixed value par depend nahi karte. Pehle current value extract karte hain, phir usko verify karte hain.

###################################################################################################################################################################


import pytest                                                                # Pytest testing framework import kiya, taaki test run kar sakein.
from playwright.sync_api import Page, expect                                 # Page browser control ke liye aur expect assertion ke liye import kiya.


def test_dynamic_table(page: Page):                                          # Test function banaya; page fixture browser page provide karta hai.
    page.goto("https://practice.expandtesting.com/dynamic-table")            # Dynamic Table website open ki, kyunki hume isi ka data test karna hai.

    # LOCATING THE TABLE
    rows = page.locator("table.table.table-striped tbody tr").all()          # Table ki saari rows ko list mein collect kiya, taaki har row check kar sakein.

    # FINDING CHROME ROW
    cpu_load = ""                                                            # Empty variable banaya, jisme Chrome ka CPU Load store hoga.

    for row in rows:                                                         # Table ki har row ko ek-ek karke check karne ke liye loop lagaya.
        process_name = row.locator("td").nth(0).inner_text()                 # Current row ke first column se process ka naam nikala.

        if process_name == "Chrome":                                         # Check kiya ki current row Chrome ki hai ya nahi.
            cpu_load = row.locator("td:has-text('%')").inner_text()          # Chrome wali row ke andar % wale cell se CPU Load nikala.
            print("CPU LOAD OF Chrome:", cpu_load)                           # Extract kiya hua CPU Load terminal mein display kiya.
            break                                                            # Chrome mil gaya, isliye unnecessary rows check karna band kar diya.

    # ASSERTION
    expect(page.locator("p#chrome-cpu")).to_contain_text(cpu_load)           # Verify kiya ki page par Chrome CPU ka text extracted CPU Load ko contain karta hai.

    page.wait_for_timeout(5000)                                              # Browser ko 5 seconds open rakha, taaki headed mode mein result dekh sakein.


# TERMINAL COMMAND
# pytest -v -s test_dynamic_table.py --headed