# test and verify the title
# test the url of web app
from playwright.sync_api import Page, expect


def test_title(page:Page):
    page.goto("https://www.uipath.com/resources/automation-analyst-reports/business-value-of-uipath-test-cloud?utm_source=google&utm_medium=paid_search&utm_team=pdi&utm_team_geo=global&utm_campaign=India_Tier-1_ENG_Mix_T4_BOAT&utm_term=web%20testing%20tool-p-c-g&utm_content=822405605689&gclsrc=aw.ds&gad_source=1&gad_campaignid=24177431993&gbraid=0AAAAADFZWhrrxRZSaGXZHHbTHGlDAkQ1W&gclid=Cj0KCQiA-8XXBhDaARIsADnEOrAjl9k76A_5fBKqk5a4DqT2aPwAHykb1rrSHr4ZWrLoZtN921QhUw8aAv8UEALw_wcB")
    expect(page).to_have_title("The UiPath Platform™ for Business Orchestration and Automation | UiPath")

def test_url(page: Page):
    page.goto("https://www.uipath.com/?utm_source=google&utm_medium=paid_search&utm_team=pdi&utm_team_geo=global&utm_campaign=India_Tier-1_ENG_Mix_T4_BOAT&utm_term=web%20testing%20tool-p-c-g&utm_content=822405605689&gclid=Cj0KCQiA-8XXBhDaARIsADnEOrAjl9k76A_5fBKqk5a4DqT2aPwAHykb1rrSHr4ZWrLoZtN921QhUw8aAv8UEALw_wcB")
    expect(page).to_have_url("https://www.uipath.com/?utm_source=google&utm_medium=paid_search&utm_team=pdi&utm_team_geo=global&utm_campaign=India_Tier-1_ENG_Mix_T4_BOAT&utm_term=web%20testing%20tool-p-c-g&utm_content=822405605689&gclid=Cj0KCQiA-8XXBhDaARIsADnEOrAjl9k76A_5fBKqk5a4DqT2aPwAHykb1rrSHr4ZWrLoZtN921QhUw8aAv8UEALw_wcB")

