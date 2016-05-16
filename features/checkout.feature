Feature: User must fill every needed information in the billing form before submit
  Scenario: Open http://www.practiceselenium.com/check-out.html website and click place order
    Given I open check out form
    When I hit place order button without entered any information
    Then I unable to submit the form and I still at the same page
