# XPath         XML Path Language      Extensible Markup Language.

# XPath ka full form XML Path Language hai. XPath ek locator hai jiska use website ke HTML DOM mein kisi element ko uske tag, ID, class, attribute ya text ke basis par locate karne ke liye hota hai.

# XPath ke 2 types hote hain:

# 1. Absolute XPath: HTML ke root element se target element tak poora path define karta hai.
# Example: `/html/body/div/form/input`

# 2. Relative XPath: HTML structure mein element ko directly uske attributes, ID, class ya text ke basis par locate karta hai.
# Example: `//input[@id='username']`

# Relative XPath zyada preferred hota hai kyunki ye Absolute XPath ke comparison mein HTML structure changes se kam affect hota hai.\

#========================================================================================================================================================================
import pytest
from playwright.sync_api import Page,expect


# 1. Absolute XPath (Full XPath)

def test_xpath_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    logo= page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()


# ABSOLUTE XPATH
# Step 1: Logo par right-click karo.
# Step 2: Inspect select karo.
# Step 3: left side kone me selector se logo par click karo
# Step 4: DOM me jo line highlight ho us par right click karo
# Step 5: Copy > Copy XPath select karo.

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Relative XPath         syntax -    //tagname[@attribute="value"]

# question - locate logo of web application
    logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()


    print("===============================================Relative XPath with contains()=============================================================================================")


# 2.A - Relative XPath with contains()              # koi specify eliment search karne ke liye like sirf vo dhoondo jinme computer text add ho
# text.contains()  &   all_text_contains()    very imp...


    product=page.locator("//h2//a[contains(@href,'computer')]")        # h2 tag h, uske andar ek or tag h a, contains formulla h, @herif attribute h, computer value h
    print("product count:", product.count())                            # ye count karega kitne aese eliment h jisme computer text add h
    expect(product).to_have_count(product.count())                      # ab ye hame total count dega aese eliments ka jo computer text contain kar rhe hain

    print("---------------------------------------------------------------------------------------------------")

# ab agar hame in chaaro products me se pehla chahiye product or uska naam kya h to ham ye karenge

    print("first product name:",product.first.text_content())            # first pehla product capture karega, text_contain us web page ke us eliment me kya text h vo lakar dega

    print("last product name:", product.last.text_content())            # same but ye last product eliment ke text ko lakar dega

    print("---------------------------------------------------------------------------------------------------")

    product_titles = product.all_text_contents()                        # ye saare products layega jinka text computer contain karta h
    print("All products:",product_titles)

# making list with using looping statement
    print("_____________list________________")
    print("printing all titles in a list using looping statement")
    for i in product_titles:
        print(i)

    # pytest -v -s test_xpath_locators.py --headed

print("===============================================Relative XPath with starts-with()=============================================================================================")

# 2.B - Relative XPath with starts-with()

def test_starts_with(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    items = page.locator("//h2//a[starts-with(@href,'/build')]")
    print("Items Count:",items.count())
    expect(items).to_have_count(items.count())

    print("FIRST ITEM:",items.first.text_content())
    print("LAST ITEM:",items.last.text_content())

    items_text = items.all_text_contents()
    print("Items Text:",items_text)

    print("_____________list________________")
# LIST PF ITEMS USING LOOP
    for i in items_text:
        print(i)

# pytest -v -s test_xpath_locators.py::test_starts_with  --headed
# pytest - v - s test_xpath_locators.py - -headed

    print("---------------------------------------------------------------------------------------------------")

# 2.C - Relative XPath with text() - is represent the inner text of the eliment

    registration_link = page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()


# 3.C Relative XPath with last()

    google_text_link = page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google_text_link).to_have_text("Google+")


# 3.C Relative XPath with positon()

    twitter_text_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_text_link).to_have_text("Twitter")


















































# DIFFERENCE

# 1. Absolute XPath
# HTML ke root se element tak poora path.
# Example: /html/body/div[4]/div[1]/a/img
# HTML structure change hui toh XPath break ho sakta hai.
# Maintain karna difficult hai.


# 2. Relative XPath
#Element ko directly tag, ID, class ya attribute se locate karte hain.
# Example: //img[@alt='Tricentis Demo Web Shop']
# HTML structure change hone par bhi aksar kaam karta hai.
# Maintain karna easy hai.

# 3. Dono ka use
# Element locate, click, fill aur verify karne ke liye.

# 4. Kaunsa better hai?
# Relative XPath generally better hai.
# Real projects mein Relative XPath prefer karo.
# Absolute XPath learning aur quick inspection ke liye use kar sakte ho.


