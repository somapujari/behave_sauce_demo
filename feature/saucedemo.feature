Feature: login saucedemo

  Scenario: login to sauce demo application
    Given launch chrome browser
    When open url "https://www.saucedemo.com/"
    And wait for some period
    And enter username "standard_user" and password  "secret_sauce"
    And click on login button
    Then user verify title
    And close browser


  Scenario Outline: login with valid and invalid user
    Given launch chrome browser
    When open url "https://www.saucedemo.com/"
    And wait for some period
    And enter username "<username>" and password  "<password>"
    And click on login button
    Then user verify title
    And close browser

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | locked_out_user         | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |
      | soma_pujari             | secret_sauce |

