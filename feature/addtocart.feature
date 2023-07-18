Feature: add to cart
  Scenario:  add to cart to sauce demo app
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
    Then verify add_to_cart page





