# CSS - Cascading Style Sheets

'''
CSS website ke HTML elements ki styling aur design control karta hai,
jaise colour, size, font, spacing aur layout.

Playwright mein CSS Selectors se HTML elements locate kar sakte hain.

Yaani HTML website ka structure banata hai aur CSS uska design karta hai.

CSS Selectors ka use elements ko locate karne ke liye karte hain,
jab humein HTML ke tag, ID, class ya attributes ke basis par
element ko identify karna ho.

Examples:
1. Tag
2. ID
3. Class
4. Attribute
5. Tag + Class
6. Tag + Attribute
7. Tag + Class + Attribute


Bas ye yaad rakho:
CSS syntax	Meaning
1.input#username	                Tag + ID combination                       representing hash #
2.input.search-box        	        Tag + Class combination                    representing dot .
3.input[type="text"]      	        Tag + Attribute combination                representing square brackets []
4.input.search-box[type="text"]	    Tag + Class + Attribute combination        tag.class[attribute=value]

tag = input yani tag input hota hai
tag is optional

'''

# -------------------------------------------------------------------------------------------------------------------------------------------
# Tag + id  combination #

import pytest
from playwright.sync_api import Page,expect

def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("T-Shirt")
    page.wait_for_timeout(5000)

# -------------------------------------------------------------------------------------------------------------------------------------------
# tag + class combination .

    page.locator("input.search-box-text").fill("jackets")  # agar class eliment ki value m space ho to space se pehle ki value copy karo bs baad ki nhi agar baad ki bhi karoge to test run nhi hoga
    page.wait_for_timeout(5000)

# pytest -v -s test_css_locators.py --headed

# -------------------------------------------------------------------------------------------------------------------------------------------
# Tag + Attribute Combination []
# if we have not id and class present in DOM so we have to use this

def test_verify_attribute(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[name=q]").fill("Shoue")        # DOM me unique attribute pick karo koi bhi then square bracket me paste karo or usme se double cort " " hata do
    page.wait_for_timeout(5000)

# pytest -v -s test_css_locators.py::test_verify_attribute --headed

# -------------------------------------------------------------------------------------------------------------------------------------------
# Tag + Class + Attribute combination    tag.[]

def test_verify_tca(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text[name=q]").fill("Tag + Class + Attribute combination")
    page.wait_for_timeout(5000)

# pytest -v -s test_css_locators.py::test_verify_tca --headed

# -------------------------------------------------------------------------------------------------------------------------------------------

# Absolute path or css  and Relative css

# 1. Absolute XPath: HTML ke root se element tak poora path likhkar locate karna.

# Example:
# `/html/body/div/div/form/input`

# 2. Relative XPath: Element ko directly uske tag, ID, class ya attribute se locate karna.

# Example:
# `//input[@id='username']`

# 3. CSS ID: ID ke through element locate karna.

# Example:
# `page.locator("#username")`

# 4. CSS Class: Class ke through element locate karna.

# Example:
# `page.locator(".search-box")`

# 5. CSS Attribute: Attribute aur uski value ke through element locate karna.

# Example:
# `page.locator('input[type="text"]')`

# Yaad rakho: Absolute XPath poore HTML structure par dependent hota hai,
# jabki Relative XPath directly element ko target karta hai.