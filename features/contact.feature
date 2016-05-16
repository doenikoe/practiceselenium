Feature: Send email to store owner
  Scenario: Open http://www.practiceselenium.com/let-s-talk-tea.html website and fill the contact form
    Given I open contact page
    And I fill the form with values
    And I hit submit button
    Then Thank you message appear