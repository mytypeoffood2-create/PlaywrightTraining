# flipkart project

# Get flipkart hidden element through debugger
# search wali ball on search bar
# select first item which shown first and click on it then you will see the new page
# select all the products of the page and get print names and price of all


import pytest
from playwright.sync_api import Page, expect

def test_flipkart_dropdown(page : Page):
    page.goto("https://www.flipkart.com/")
    page.locator("input[name='q']").first.click()
    page.wait_for_timeout(3000)
    page.locator("input[name='q']").first.fill("wali ball")
    page.wait_for_timeout(3000)
    page.locator("img.iSAepO.HImJXk").first.click()
    page.wait_for_timeout(3000)

    portion = page.locator("div.nZIRY7")


    print("There are :",portion.count(),"portions")

    print("list count:",portion.all_text_contents())

    for items in portion.all_text_contents():
        print(items)



    names = page.locator("a.pIpigb").all_text_contents()
    prices = page.locator("div.hZ3P6w").all_text_contents()

    for name, price in zip(names, prices):
        print("Product:", name)
        print("Price:", price)
        print("----------------")






def test_youtube(page: Page):
    page.goto("https://www.youtube.com/")
    page.locator("input[name='search_query']").fill("syed wali mohammad rizvi")
    page.wait_for_timeout(3000)
    page.locator("button.ytSearchboxComponentSearchButton").click()
    page.wait_for_timeout(3000)

    page.goto("https://www.youtube.com/watch?v=ECMzBxYRyCc")
    page.wait_for_timeout(5000)

    # page.locator("div#placeholder-area").fill("Mashallah Maula salamat rakhe aap dono ko")
    # page.wait_for_timeout(3000)
    #
    # page.locator("button[aria-label='Comment']").click()
    # page.wait_for_timeout(5000)



    page.locator("div#placeholder-area").click()

    comment = page.locator("#contenteditable-root")
    comment.fill("Mashallah Maula salamat rakhe aap dono ko")



# pytest -v -s practice_hidden_dropdown.py --headed