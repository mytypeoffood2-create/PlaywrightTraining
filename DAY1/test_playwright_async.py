# Asynchronous
# Ek task wait kar raha ho toh program doosre tasks bhi execute kar sakta hai.

# Await
# Asynchronous task ke complete hone ka wait karta hai. Sirf async def ke andar use hota hai.

# Asynchronous
# Ek task wait kar raha ho toh program doosre tasks bhi execute kar sakta hai.

# Await
# Asynchronous task ke complete hone ka wait karta hai. Sirf async def ke andar use hota hai.


# for exaple...

from playwright.async_api import async_playwright,Page, expect  # Playwright ki asynchronous API, Page aur expect import kar rahe hain.

async def test_verify_url():                     # Asynchronous test function bana rahe hain.
    async with async_playwright() as p:          # Playwright start kar rahe hain aur p se browser access karenge.
        browser = await p.chromium.launch()      # Chromium browser launch kar rahe hain.
        my_page = await browser.new_page()       # Browser mein naya tab open kar rahe hain.
        my_page.goto("https://demowebshop.tricentis.com/")
        await expect(my_page).to_have_url("https://demowebshop.tricentis.com/")  # Check kar rahe hain ki page ka URL expected URL hai ya nahi.


# This give output
#
# async def functions are not natively supported.
# You need to install a suitable plugin for your async framework, for example:
#   - anyio
#   - pytest-asyncio
#   - pytest-tornasync
#   - pytest-trio
#   - pytest-twisted
# ============================================================================= short test summary info =============================================================================
# FAILED test_playwright_async.py::test_verify_url - Failed: async def functions are not natively supported.
# ================================================================================ 1 failed in 0.11s