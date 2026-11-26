# Dynamic XPath     # jab  webapplication par dyanmic buttons ho like ek button h jispar start likha h usko dabaya to vo stop me badal gaya jisse DOM me bhi or attribute ki value me bhi changes agaye aese me kya karein ?


import pytest
from playwright.sync_api import Playwright, Page,expect

def test_handle_dynamic_xpath(page:Page):                            # Test function hai, page Playwright ka fixture hai.
    page.goto("https://testautomationpractice.blogspot.com/")        # Website open karta hai.

    output=page.locator("//button[@name='start' or @name='stop']")   # XPath se un buttons ko locate karta hai jinka name start OR stop hai.

    for i in range(10):                                               # Loop ko 10 baar repeat karta hai.
     output.click()                                                   # Har iteration mein matching button par click karta hai.

    page.wait_for_timeout(2000)                                      # 2000 milliseconds yani 2 seconds wait karta hai.

    page.get_by_text("start or stop").is_visible()                   # Check karta hai ki 'start or stop' text visible hai ya nahi. Result assert nahi hota.

    output = output.all_text_contents()                              # Matching buttons ka text list ke form mein collect karta hai.

    print("your current button is in form of:",output)                # Terminal mein buttons ke text print karta hai.