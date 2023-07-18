Feature: ship and submit
  Scenario:shiping address and conform order
    Given launch chrome browser
    When open url "https://www.saucedemo.com/"
    And wait for some period
    And enter username "standard_user" and password  "secret_sauce"
    And click on login button
    Then user verify title
    And click on product
    And click on add to_cart
    And click on cart logo
    And click on checkout
#    Then verify add_to_cart page
    And enter first_name "soma" and last_name "pujari" and zip "411039"
    And click on continue
    And verify total
    And click on finish
    Then verify order
    And close browser


