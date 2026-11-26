# HOW TO CREATE def function in playwright/  to verify url

from playwright.sync_api import Page, expect


# Page Fixture: Pytest ka built-in fixture jo test ke liye browser page provide karta hai.
# Use: URL open karna, click karna, text fill karna aur elements verify karna.
# Cleanup: Test complete hone par page automatically close ho jaata hai.


def test_verifyPageUrl(page:Page):     # page is fixture / reusable  Pytest mein Fixtures ek feature hai jo test run hone se pehle required setup ya data ready karta hai.
                                       # Example: Browser open karna, login karna, test data prepare karna.
                                       # Matlab baar-baar same setup code likhne ki zaroorat nahi hoti.

    page.goto("https://sadaematam313.wixsite.com/anjuman-sada-e-matam?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZXh0bgNhZW0CMTEAcGRvZgJzcnRjBmFwcF9pZA81NjcwNjczNDMzNTI0MjcAAafEwC2Zo9OWZi1aDwMqMioK72ykwPaRXnYf5Y_Q4F-nWDbMq45SPY6SsCevBA_aem_VVoKjQtJJv9vvAZCefWluA")      # PASSING URL
    expect(page).to_have_url("https://sadaematam313.wixsite.com/anjuman-sada-e-matam?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZXh0bgNhZW0CMTEAcGRvZgJzcnRjBmFwcF9pZA81NjcwNjczNDMzNTI0MjcAAafEwC2Zo9OWZi1aDwMqMioK72ykwPaRXnYf5Y_Q4F-nWDbMq45SPY6SsCevBA_aem_VVoKjQtJJv9vvAZCefWluA")  # EXPECTED URL


## ISKO RUN KARNE KE LIYE TERMINAL ME       python -m pytest -v -s test_playwright.py       likhna hoga.

# Playwright ke Modes of Execution

# 1. Headless Mode
# Browser background mein run hota hai. Screen par browser nahi dikhta.

# 2. Headed Mode
# Browser screen par open hota hai aur hum test execution dekh sakte hain.

# Syntax - python -m pytest -v -s test_playwright.py --headed

# Yaad rakho:
# Headless = Browser hidden
# Headed = Browser visible
# --headed

# DOM - Document Object Model
# ye html css ka code hota h inspect karne ke baad dikhta h



