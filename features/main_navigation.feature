Feature: Each menu in main navigation redirect user to the right page
  Scenario: Open welcome page
    Given I open practiceselenium website
    When I click on menu "Welcome"
    Then "Welcome" page link is correct

  Scenario: Open our passion page
    Given I open practiceselenium website
    When I click on menu "Our Passion"
    Then "Our Passion" page link is correct

  Scenario: Open menu page
    Given I open practiceselenium website
    When I click on menu "Menu"
    Then "Menu" page link is correct

  Scenario: Open menu let's talk tea page
    Given I open practiceselenium website
    When I click on menu "Let's Talk Tea"
    Then "Let's Talk Tea" page link is correct

  Scenario: Open check out page
    Given I open practiceselenium website
    When I click on menu "Check Out"
    Then "Check Out" page link is correct