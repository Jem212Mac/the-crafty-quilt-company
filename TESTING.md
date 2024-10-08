# Testing

## Manual Testing

### User Story Testing

User story testing was performed throughout site development, for each new feature, before it was merged into the master file.  User story testing was based primarily on the acceptance criteria for each of the user stories.


User Story [#1](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/1).

| Test Case ID | Test Condition / Objective                                                                                                                                                               | Test Steps                                                                                                            | Expected Results                                                                                                               | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------ |
| 1            | Check that if a user clicks on 'Shop Now' a list of all products available in the store is diplayed.  Each product should display a product image, name, category and price.     | Navigate to the home page of the site and click on 'Shop Now'.                                                        | A list of all products available in the store is displayed.  Each product displays a product image, name, category, and price. | Passed |
| 2            | Check that if a user clicks on 'All Products' a list of all products available in the store is diplayed.  Each product should display a product image, name, category and price. | Navigate to the home page of the site and then navigate to 'All Products>All Products' from the main site navigation. | A list of all products available in the store is displayed.  Each product displays a product image, name, category, and price. | Passed |


User Story [#2](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/2).

| Test Case ID | Test Condition / Objective                                                                                                              | Test Steps                                                                        | Expected Results                                                                        | Status |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------ |
| 3            | Check that if a user clicks on a product image on the products listing page, they are taken to a product details page for that product. | Click on a product image from the product listings page.                          | The user is taken to a product details page.                                            | Passed |
| 4            | Check that the product details page displays the product image, name, price, category and a description of the product.                 | Look for a product image, name, price, category, and description for the product. | A product image, name, price, category, and description for the product is displayed.   | Passed |
| 5            | Check that the product details page displays a selector for quantity and buttons to 'keep shopping', and 'add to bag'.                  | Look for a quantity selector and buttons to 'keep shopping' and 'add to bag'.     | A quantity selector, a 'keep shopping' button and an 'add to bag' button are displayed. | Passed |


User Story [#11](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/11).

| Test Case ID | Test Condition / Objective                                             | Test Steps                                      | Expected Results                                                | Status |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------- | ------ |
| 6            | Check that a user can sort on category of product in ascending order.  | Navigate to 'All Products>By Category'          | The products are sorted by Category (A-Z); in ascending order.  | Passed |
| 7            | Check that a user can sort on category of product in descending order. | Change to Category (Z-A) via the sort selector. | The products are sorted by Category (Z-A); in descending order. | Passed |


User Story [#12](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/11).

| Test Case ID | Test Condition / Objective                                                                | Test Steps                                                                                                                                                                      | Expected Results                                                                     | Status |
| ------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------ |
| 8            | Check if the user can search for a product using a word or phrase in the product name field.        | Input a word/phrase into the search bar that is present in at least one product name and check that all products with that word or phrase in the name are listed.                 | All products with that word or phrase in the product name field are displayed. | Passed |
| 9            | Check if the user can search for a product using a word or phrase in the product description field. | Input a word/phrase into the search bar that is present in at least one product description and check that all products with that word or phrase in the description are listed.   | All products with that word or phrase in the product description field are displayed. | Passed |
| 10            | Check if the user can search for a product using a word or phrase in the product author field.      | Input a word/phrase into the search bar that is present in at least one product author field and check that all products with that word or phrase in the author field are listed. | All products with that word or phrase in the product author field are displayed.      | Passed |
| 11            | Check if the user can search for a product using a word or phrase in the product brand field.       | Input a word/phrase into the search bar that is present in at least one product brand field and check that all products with that word or phrase in the brand field are listed.   | All products with that word or phrase in the product brand field are displayed.       | Passed |


User Story [#13](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/13).

| Test Case ID | Test Condition / Objective                                                                                                                                       | Test Steps                                                                                                                                            | Expected Results                                                                                        | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------ |
| 12            | Check that when a user searches for a particular word using the search bar, the results are displayed along with the word searched for and the number of results. | Input a specific word into the search bar and check that the correct word searched for is displayed along with the results and the number of results. | The results are displayed along with the word that was searched for and the number of results returned. | Passed |


User Story [#10](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/10).

| Test Case ID | Test Condition / Objective                                                                  | Test Steps                                                                            | Expected Results                                              | Status |
| ------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------ |
| 13            | Check that the user can search 'All Products' by Price (low-to-high)                        | Navigate to 'All Products' and select 'Price (low-to-high)' on the sort bar.          | All available products are displayed by price, ascending.     | Passed |
| 14            | Check that the user can search 'All Products' by Price (high-to-low)                        | Navigate to 'All Products' and select 'Price (high-to-low)' on the sort bar.          | All available products are displayed by price, decsending.    | Passed |
| 15            | Check that the user can search 'All Products' by Name (A-Z)                                 | Navigate to 'All Products' and select 'Name (A-Z') on the sort bar.                   | All available products are displayed by name, ascending.      | Passed |
| 16            | Check that the user can search 'All Products' by Name (Z-A)                                 | Navigate to 'All Products' and select 'Name (Z-A)' on the sort bar.                   | All available products are displayed by name, decsending.     | Passed |
| 17            | Check that the user can search 'All Products' by Category (A-Z)                             | Navigate to 'All Products' and select 'Category (A-Z)' on the sort bar.               | All available products are displayed by category, ascending.  | Passed |
| 18            | Check that the user can search 'All Products' by Category (Z-A)                             | Navigate to 'All Products' and select 'Category (Z-A)' on the sort bar.               | All available products are displayed by category, decsending. | Passed |
| 19            | Check that the user can search 'Baby Quilts' (or any other category) by Price (low-to-high) | Navigate to 'Quilts>Baby Quilts' and select 'Price (low-to-high)' on the sort bar.    | All baby quilts are displayed by price, ascending.            | Passed |
| 20            | Check that the user can search 'Baby Quilts' (or any other category) by Price (high-to-low) | Navigate to ' 'Quilts>Baby Quilts'' and select 'Price (high-to-low)' on the sort bar. | All baby quilts are displayed by price, decsending.           | Passed |
| 21            | Check that the user can search 'Baby Quilts' (or any other category) by Name (A-Z)          | Navigate to  'Quilts>Baby Quilts'' and select 'Name (A-Z') on the sort bar.           | All baby quilts are displayed by name, ascending.             | Passed |
| 22           | Check that the user can search 'Baby Quilts' (or any other category) by Name (Z-A)          | Navigate to  'Quilts>Baby Quilts'' and select 'Name (Z-A)' on the sort bar.           | All baby quilts are displayed by name, decsending.            | Passed |
| 23           | Check that the user can search 'Quilts' by Category (A-Z)                                   | Navigate to ' 'Quilts'' and select 'Category (A-Z)' on the sort bar.                  | All quilts are displayed by category, ascending.              | Passed |
| 24           | Check that the user can search 'Quilts' by Category (Z-A)                                   | Navigate to ' 'Quilts'' and select 'Category (Z-A)' on the sort bar.                  | All quilts are displayed by category, descending.             | Passed |


User Story [#3](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/3).

| Test Case ID | Test Condition / Objective                                             | Test Steps                                                                                                               | Expected Results                                                   | Status |
| ------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | ------ |
| 25            | Check that a user can add a selection of products to the shopping bag. | Navigate to a product and select add to bag.  Navigate to another product and select add to bag.  Do this several times. | All of the items selected should be available in the shopping bag. | Passed |


User Story [#4](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/4).

| Test Case ID | Test Condition / Objective                                                                                 | Test Steps                                                                                                                                                                                            | Expected Results                                                                                                                                               | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 26            | Check that if a user has added items to the shopping bag, they can see the contents of the bag at anytime. | Add one or more products to the shopping bag.  Click on the shopping bag icon in the top right corner of the site to open it.  Click elsewhere within the site and then go back to the shopping bag. | The contents of the shopping bag should be displayed and should remain in the bag even if the user clicks elswhere in the site and then comes back to the bag. | Passed |
| 27            | Check that the bag displays each item that has been added to the bag, and the quantity of each item.       | Add one or more products to the shopping bag.  Click on the shopping bag icon in the top right corner of the site to open it.                                                                         | The bag should display each item that has been added to the bag and the quantity of each item.                                                                 | Passed |
| 28            | Check that the bag displays the total cost for the contents of the bag.                                    | Add one or more products to the shopping bag.  Click on the shopping bag icon in the top right corner of the site to open it.                                                                         | The bag should display the total cost for the items in the bag, including delivery.                                                                            | Passed |


User Story [#14](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/14).

| Test Case ID | Test Condition / Objective                                                                                       | Test Steps                                                                                                                                           | Expected Results                                                                            | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| 29            | Check that a user can select a specific quantity of a product to add to their bag from the product details page. | Navigate to the product details page for a product and input a specific quantity into the quantity bar and click add to bag.                         | The quantity of items selected should be added to the bag.                                  | Passed |
| 30            | Check that a user cannot select less than 1 product from the product details page.                                     | Navigate to the product details page for a product and use the - button on the quantity bar to try to select less than one.                      | The - button should be disabled at 1 and should not allow the user to select less than 1.   | Passed |
| 31            | Check that a user cannot select more than 99 of a product from the product details page.                           | Navigate to the product details page for a product and and use the + button on the quantity bar to try to select more than 99.                       | The + button should be disabled at 99 and should not allow the user to select more than 99. | Passed |
| 32            | Check that a user can adjust the quantity of a product on the shopping bag page.                                 | Once a product has been added to the bag, navigate to the shopping bag page and input a specific quantity into the quantity bar and click Update.    | The quantity of items should be updated.                                                    | Passed |
| 33            | Check that a user cannot select less than 1 product from the shopping bag page.                                    | Once a product has been added to the bag, navigate to the shopping bag page and use the - button on the quantity bar to try to select less than one. | The - button should be disabled at 1 and should not allow the user to select less than 1.   | Passed |
| 34            | Check that a user cannot select more than 99 of a product from the shopping bag page.                              | Once a product has been added to the bag, navigate to the shopping bag page and use the + button on the quantity bar to try to select more than 99.  | The + button should be disabled at 99 and should not allow the user to select more than 99. | Passed |


User Story [#15](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/15).

| Test Case ID | Test Condition / Objective                                                     | Test Steps                                                                   | Expected Results                                                                                                                               | Status  |
| ------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 35            | Check that a user can checkout the selections in their bag to make a purchase. | Add one or more products to the shopping bag and click on 'secure checkout'. | The user is taken to a screen where they can see their order details and can input their delivery details and card details to make a purchase. | Passed. |


User Story [#16](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/16).

| Test Case ID | Test Condition / Objective                                                                                                                | Test Steps                                                                                                                                                                                                                          | Expected Results                                                                                                     | Status |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------ |
| 36            | Check that a logged in user can input their delivery details when making a purchase and select to save those delivery details.            | Log in.  Add one or more products to the shopping bag and select 'secure checkout'.  Add delivery details for the purchase and select to save as default delivery details.  Enter card details to make the purchase.                | The order should be processed with those delivery details and the user should receive an order confirmation message. | Passed |
| 37            | Check that saved delivery details are saved to the the users profile and that the saved details are prepopulated for their next purchase. | Having made the above purchase, select My Profile and check that the delivery details have been saved to the user's profile.  Process another purchase and check that the delivery details are prepopulated at the checkout screen. | The default delivery details should be saved to the user profile and should be prepopulated for their next purchase. | Passed |


User Story [#19](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/19).

| Test Case ID | Test Condition / Objective                                                                 | Test Steps                                                                                                                              | Expected Results                                                                                                            | Status |
| ------------ | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------ |
| 38            | Check that an order confirmation screen is displayed to a user after they make a purchase. | Add one or more products to the shopping bag.  Select 'secure checkout' and input delivery details and card details to make a purchase. | An order confirmation screen should be displayed after a successful purchase with details of what was ordered and the cost. | Passed |


User Story [#17](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/17).

| Test Case ID | Test Condition / Objective                                                                                                                                                                      | Test Steps                                                                                                                                                                                                                                                                                                                                                                        | Expected Results                                                                                                                                                                                                                                                                                                          | Status |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 39            | Check that if a user makes a successful purchase using stripes test card details, the successful payment is visible in stripe.                                                                  | Add one or more items to the shopping bag and select secure checkout.  Add delivery details and the stripe test card details and select complete order.  Login to stripe and navigate to developers > events and check for the payment.                                                                                                                                           | A payment succeeded message for the order for the order amount at the appropriate date and time should be visible.                                                                                                                                                                                                        | Passed |
| 40            | Check that if a user makes a successful purchase using stripes test card details, an order confirmation is displayed.                                                                           | Add one or more items to the shopping bag and select secure checkout.  Add delivery details and the stripe test card details and select complete order.                                                                                                                                                                                                                           | If the payment and order are successful, an order confirmation should be displayed to the user.                                                                                                                                                                                                                           | Passed |
| 41            | Check that if invalid card details are entered, an error message is displayed to the user and they can renter valid card details.                                                               | Add one or more items to the shopping bag and select secure checkout.  Add delivery details and invalid test card details (e.g. invalid end date).                                                                                                                                                                                                                                | An error message should be displayed to the user (e.g. Your card's expiration date is in the past) and the user can re-enter valid card details to complete the purchase.                                                                                                                                                   | Passed |
| 42            | Check that if a user makes a purchase using stripes test card details that require authentication, and that authentication fails, an error is displayed to the user and the order is not saved. | Add one or more items to the shopping bag and select secure checkout.  Add delivery details and the stripe test card details for a card requiring authorisation and select complete order.   A pop message will appear asking for authentication.  Select Fail.                                                                                                                   | An error message should be displayed to the user (e.g. We are unable to authenticate your payment method).  The order is not saved and the user can re-enter valid card details to complete the purchase.                                                                                                                   | Passed |
| 43            | Check that if the user closes the page or the site goes down before the order is processed, but after the payment is taken, the order is created from the stripe webhook.                       | Add one or more items to the shopping bag and select secure checkout.  Add delivery details and the stripe test card details and select complete order, but quickly close the website before the order is processed.  Login to stripe and navigate to developers > events and check for the payment.  Select the payment_intent.succeeded message and check the webhook attempts. | The webhook response for the payment will be: Webhook received: payment_intent.succeeded: SUCCESS: Created order in webhook.  An order with a stripe pid that matches the event in stripe should be visible in the admin and the order should be visible in the order history in the user's profile. | Passed |


User Stories [#5](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/5) and [#8](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/8).

| Test Case ID | Test Condition / Objective                                                                             | Test Steps                                                                             | Expected Results                                                                                                                                                                                                                                                                                            | Status |
| ------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 44            | Check that a user can register for an account.                                                         | Click on Register and input a username and password.                                   | A password should be required to be input twice.                                                                                                                                                                                                                                                            | Passed |
| 45            | Check that the user receives a verification email after registering.                                   | Once registered, check for an email requesting the user to verify their email address. | An email should be sent to the user with a link for verification.                                                                                                                                                                                                                                           | Passed |
| 46            | Once they have verified their email, they will be able to access their account and their user profile. | Click on the verification link to verify the email address.                            | Clicking on the link, the user should get a confirmation message to let them know their email address has been verified and they should be able to access their user profile.                                                                                                                               | Passed |
| 47            | Check that an unverified user cannot login.                                                            | Repeat the steps above but do not click on the link to verify the email address.       | Attempt to login without verifying. The user should see a message 'We have sent an e-mail to you for verification. Follow the link provided to finalize the signup process. Please contact us if you do not receive it within a few minutes.'  The user cannot login until they verify their email address. | Passed |


User Story [#6](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/6).

| Test Case ID | Test Condition / Objective                                                                                      | Test Steps                                                                                         | Expected Results                                                                                                                                                        | Status |
| ------------ | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 48            | Check that once a user has registered and verified ther email, thay can login with their username and password. | Login as a registered and verified user with a username and password.                              | The user should see a message to let them know they have successfully logged in.                                                                                        | Passed |
| 49            | Check that once they log in, they can access their user profile.                                                | Login as a registered and verified user with a username and password and navigate to user profile. | The user should be able to access their user profile.                                                                                                                   | Passed |
| 50            | If they are a superuser, check that they can access product management.                                         | Login as a superuser and navigate to 'Manage Products'.                                            | The user should be able to access product management to add a product.                                                                                                  | Passed |
| 51            | Check that if they logout they can no longer access their user profile or product management.                   | Navigate to and select logout.                                                                     | The user should see a message to let them know they have successfully logged out and they should no longer be able to access their user profile or product management. | Passed |


User Story [#7](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/7).

| Test Case ID | Test Condition / Objective                                                                                             | Test Steps                                               | Expected Results                                                                                                                                                                                                                   | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 52            | Check that a user can click on forgot password and they will be sent an email with a link to reset their password. | Select login and then select forgot password.            | The user will be asked to input their email address and can click on Reset My Password.  They will be sent an email with a link to reset their password.                                                                          | Passed |
| 53            | Check that a user can use the link to change / reset their password.                                                   | From the email, click on the link to reset the password. | The user will be asked to input a new password twice to change their password.  They will see a message to let them know they have successfully changed their password and they should then be able to use that password to login. | Passed |


User Story [#9](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/9).

| Test Case ID | Test Condition / Objective                                                                              | Test Steps                                                                                                                                                                     | Expected Results                                                           | Status |
| ------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------ |
| 54            | Check that a logged in user can access their profile and input / update their default delivery details. | Login as an authenticated user and navigate to User Profile.  Input or update default delivery details.                                                                        | The user should be able to input or update their default delivery details. | Passed |
| 55            | Check that a logged in user can access their profile and see their order history.                       | Login as an authenticated user and navigate to User Profile.  Check to see that the user's order history is visible.  If there are no orders, make some purchases and recheck. | The user should be able to see their order history.                        | Passed |
| 56            | Check that a user that is not logged in cannot access a user profile.                                      | Logout.  Navigate to User Profile.                                                                                                                                             | User Profile should not be an available / visible option.                  | Passed |

User Story [#18](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/18).

| Test Case ID | Test Condition / Objective                                                                                 | Test Steps                                                                                                                                                                                     | Expected Results                                                                                 | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------ |
| 57            | Check that a non logged in user receives an email confirmation of their order after a successful purchase. | Do not login.  Add one or more items to the shopping bag and select secure checkout.  Add your email address, delivery details, and payment details at the checkout and select Complete Order. | If the purchase is successful, the user should receive an email with confirmation of their order. | Passed |
| 58            | Check that a logged in user receives an email confirmation of their order after a successful purchase.     | Login.  Add one or more items to the shopping bag and select secure checkout.  Add/update your email address, delivery details, and payment details at the checkout and select Complete Order. | If the purchase is successful, the user should receive an email with confirmation of their order. | Passed |


User Story [#25](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/25).

| Test Case ID | Test Condition / Objective                                                                | Test Steps                                                | Expected Results                                                       | Status |
| ------------ | ----------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------- | ------ |
| 59            | Check that a logged in superuser can add new products to the site via product management. | Login in as a superuser.  Navigate to 'Manage Products'.  | The user should be able to input and submit details for a new product. | Passed |
| 60            | Check that a user that is not a superuser cannot access product management.               | Login as a standard user.  Navigate to 'Manage Products'. | 'Manage Products' should not be visible to the user.                    | Passed |
| 61            | Check that user not logged in cannot access product management.                           | Do not login.  Navigate to 'Manage Products'.             | 'Manage Products' should not be visible to the user.                    | Passed |


User Story [#26](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/26).

| Test Case ID | Test Condition / Objective                                                                                                                                                              | Test Steps                                                                                                          | Expected Results                                                                                                                           | Status |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| 62            | Check that a logged in superuser can see an Edit link under products on the product listings page.                                                                                      | Login as a superuser.  Navigate to 'All Products'.                                                                  | The superuser should see an edit link under each product in the product listings page.                                                     | Passed |
| 63            | Check that a logged in superuser can see an edit link under products on the product details page.                                                                                       | Login as a superuser.  Navigate to 'All Products'.  Click on a product.                                             | The superuser should see an edit link under the product in the product details page.                                                       | Passed |
| 64            | Check that a logged in user can click on the edit link on either the product listing or product details page and it opens up a page to allow them to edit the existing product details. | Click on an edit link from the product listings page or an edit link under product details.                         | A page should open up with a form that allows the super user to edit the prouct details.                                                   | Passed |
| 65            | Check that a logged in superuser can edit the product details.                                                                                                                          | Edit the product details in the form and click Update Product.                                                      | The superuser should be able to edit the product details and submit them.  Viewing the product details should show that they have changed. | Passed |
| 66            | Check that a user that is not a superuser cannot edit a product's details.                                                                                                              | Do not login, or login as a standard user (not superuser) and navigate to a product listing and/or product details. | The user should not see a link to Edit the product.                                                                                        | Passed |


User Story [#27](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/27).

| Test Case ID | Test Condition / Objective                                                                                                                                   | Test Steps                                                                                                          | Expected Results                                                                        | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------ |
| 67            | Check that a logged in superuser can see a Delete link under products on the product listings page.                                                          | Login as a superuser.  Navigate to 'All Products'.                                                                  | The superuser should see a Delete link under each product in the product listings page. | Passed |
| 68            | Check that a logged in superuser can see a Delete link under products on the product details page.                                                          | Login as a superuser.  Navigate to 'All Products'.  Click on a product.                                             | The superuser should see a Delete link under the product in the product details page.   | Passed |
| 69            | Check that a logged in user can click on the Delete link on either the product listing or product details page and it will delete the product from the site. | Click on a Delete link from the product listings page or a Delete link under product details.                       | The product should be deleted and will no longer be available to purchase.              | Passed |
| 70            | Check that a user that is not a superuser cannot Delete a product.                                                                                           | Do not login, or login as a standard user (not superuser) and navigate to a product listing and/or product details. | The user should not see a link to Delete the product.                                   | Passed |


User Stories [#30](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/30) and [#31](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/31).

| Test Case ID | Test Condition / Objective                                                                     | Test Steps                                                                                                                                                                                                                                                                                                                                   | Expected Results                                                                                                                                                                                   | Status |
| ------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 71            | Check that a logged in user can write a review for a product, adding a rating and description. | Login.  Navigate to a specific product and scroll down to 'Write a review'.  Select a rating and add a description. Click submit.                                                                                                                                                                                                             | The review will be visible to the person that wrote the review, though it needs approval from a superuser before it is visible to all site users.                                                  | Passed |
| 72            | Check that a logged in user can edit a review that they have written.                          | For the review just created, click on 'edit'.                                                                                                                                                                                                                                                                                                | The review will repopulate the 'write a review' section and can be edited by the user and updated.                                                                                                   | Passed |
| 73            | Check that a logged in user can delete a review that they have written.                        | For the review just created, click on 'delete'.                                                                                                                                                                                                                                                                                              | The user wil be asked to confirm that they want to delete the review.  Clicking on delete will delete the review and a message will be displayed to let the user know the review has been deleted. | Passed |
| 74            | Check that another user cannot edit or delete a review written by someone else.                | Login.  Navigate to a specific product and scroll down to 'Write a review'.  Select a rating and add a description.  Click submit.  Logout and login as a superuser and access the admin.  Click on the review just created and approve it.  Logout and login as a different user from the one that created the review.  Scroll to the review. | There should not be any edit or delete buttons visible for the user that did not create the review.                                                                                                | Passed |


User Story [#34](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/34).

| Test Case ID | Test Condition / Objective                                                                                                                             | Test Steps                                                                                             | Expected Results                                                                                                            | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ------ |
| 75            | Check that a user can complete a Contact Us form with their email address and some description to contact the site owner.                               | Navigate to 'Contact Us' on the main navigation bar.  Complete the Contact Us form and click 'Submit'. | The User is able to complete the form giving their name, email address, and a message.                                      | Passed |
| 76            | Check that on completion of a Contact Us form, the user receives a message to confirm the form submission and to let them know when to expect a reply. | Navigate to 'Contact Us' on the main navigation bar.  Complete the Contact Us form and click 'Submit'. | When the user submits their form, they will see a message to let them know it was received and when they can expect a reply. | Passed |


User Story [#28](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/28).

| Test Case ID | Test Condition / Objective                                                                                    | Test Steps                                                                                                                        | Expected Results                                                                                                                                                        | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 77            | Check that a logged in user can add products to their wishlist to purchase at a later date.                   | Login.  Navigate to one or more products and click 'Add to Wishlist'.  Navigate to 'My Wishlist' to view the added products.      | The user will see a message to let them know the products were added to the wishlist.  The products should be added and visible in the user's wishlist.                 | Passed |
| 78            | Check that a logged in user can remove products from their wishlist.                                          | Login.  Navigate to 'My Wishlist'.  Select a product in the wishlist and click on 'Remove from Wishlist'.                         | The user will see a message to let them know the product was removed the wishlist.  The product should be removed from the wishlist.                                  | Passed |
| 79            | Check that if a user has not logged in, they cannot access a wishlist, and cannot add products to a wishlist. | Do not login.  Navigate to 'My Wishlist'. Navigate to one or more products and click 'Add to Wishlist'. | There should be no option visible for the user to view 'My Wishlist'.  When the user clicks on 'Add to Wishlist' for a product they will be directed to the login page. | Passed |


User Story [#29](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/29).

| Test Case ID | Test Condition / Objective                                                    | Test Steps                                                                                                                 | Expected Results                                                                                                                | Status |
| ------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 80            | Check that a user can view items in their wishlist and add them to their bag. | Login.  Navigate to 'My Wishlist'.  Select an Item in the wishlist and click on 'Product Details'.  Click on 'Add to Bag'. | The user should see a message to confirm the product was added to their bag and should be able to continue with their shopping. | Passed |

---


## Usability / User Acceptance Testing

In addition to the testing I performed throughout the developement process which was primarily based around the user stories and the acceptance criteria (as detailed above), I also performed some exploratory testing based on the following user journeys with the goal of ensuring that the site would meet the expectations of a user in terms of ease of use, ease of navigation, responsiveness of buttons and links etc.  My aim was to ensure that user's would have a pleasant experience interacting with the site and that the overall display of content to the user was appropriate and appealing (clear, clean and uncluttered).

1. Viewing 'All Products' or a subset of Products dependent on the menu item chosen.
2. Viewing a specific products details.
3. Adding a product to the shopping bag.
4. Adding several products to the shopping bag.
5. Selecting checkout and entering delivery details and payment details to make a purchase.
6. Searching for a product or description or author or brand via the search bar.
7. Sorting the products displayed according to the various sort options available.
8. Adding a product as a superuser.
9. Editing a product as a superuser.
10. Deleting a product as a superuser.
11. Viewing My Profile.
12. Editing My Profile.
13. Viewing My Wishlist.
14. Adding a product to my wishlist.
15. Removing a product from my wishlist.
16. Adding a product from my wishlist to the shopping bag.
17. Registering a new account.
18. Verifying an email address.
19. Signing In.
20. Signing Out.
21. Completing the Contact Us form.
22. Subscribing to the newsletter.
23. Clicking on the site's facebook link.

All input fields / forms were checked with both positive and negative tests to ensure that users could not submit empty fields, and that feedback to the user was appropriate.

---

## Browser Testing

The site was tested on the below browsers, without issue:
1. Chrome
2. Safari

---

## Device Testing / Responsive Testing

The site was tested throughout the developement process to ensure that it is fully responsive using chrome development tools.  Each page of the site was checked at each of the break points to ensure that the design and layout looked good.  I also tested the site at points between the usual breakpoints.

Testing was also performed on the following devices to ensure that the site was fully responsive:
1. Samsung Galaxy Flip mobile phone.
2. Samsung Galaxy Tab A7.
3. Standard Laptop.
4. Widescreen monitor.

---

## Bugs

Testing was performed throughout the development process, and I tried to fix bugs as soon as I observed them.  The following bugs were fixed during the development process:

1. When I originally added the image for the homepage, I had a typo in my code that prevented it from loading.  I fixed the typo and resolved the loading issue.
2. When I first created my products.html template it was outside the products folder, causing the products to not display.  I moved the template into the correct folder to resolve this.
3. I had an Unbound Local Error caused by an indentation error in my product views.py file.  I fixed the indentation and resolved this.
4. At various points I realise I used $ rather than £ as the currency.  I went through the code and changed these.
5. I realised at one point that styling of my crisy forms was not correct.  The form fields were shorter than expected.  This was caused by a typo in the settings.py file for the crispy template pack.  I fixed the typo and the crispy forms styling was resolved.
6. I had some difficulty with my database as a result of repeatedly adding and then removing a wishlist app several times.  This caused an operation error where the wishlist tables were not being created.  I had to flush the database and rebuild it to fix this issue.
7. I then had an operation error because the order table was not created.  I had to run migrations specifically for the checkout pp to fix this.
8. Originally, I had a fixed bottom footer on my site, and as a result, the content on some of the pages was being hidden under the footer.  I went through a process of adding some bottom margin to elements at the bottom of these pages to make the content visible.  Eventually, however, I changed to a footer without a fixed bottom.
9. The heading for the mailchimp newsleeter was appearing larger on three pages (profile, checkout, and checkout success); i discovered this was because I had added the css script for the newsletter to the css extra block on the product details page, and it was being overwritten by custom css for these pages.  I moved the newsletter css to the core css block and this resolved the issue.
10. After I added the mailchimp newsletter, I noticed a problem where, if a user was not logged in, and added an product to bag, the subscribe button for the newsletter was activated rather than the add to bag button.  There were also problems with several other submit buttons which all seemed to result in adding a product to bag.  I discovered that this was because I had not closed the add to bag form.  I replaced a closing div with a closing form and these issues were resolved.
11. I had a problem where the close buttons on the review delete modal were not working.  This was because I used bootstrap 5 elements rather than bootstrap 4 ones.  I changed these and the issues were resolved. 

---

## Validation:

### HTML Validation:

- [Full HTML Validation Report](documentation/validation/html_validation_report.pdf)

- No errors were found when passing through the official [W3C](https://validator.w3.org/) validator except for errors in the add_product and edit_product templates due to the use of crispy forms. This checking was done manually by copying the view page source code (Ctrl+U) and pasting it into the validator.

### CSS Validation:

- [Full CSS Validation Report](documentation/validation/css_validation.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/) validator.

### JS Validation:

- [Full JS Validation Report](documentation/validation/js_validation_report.pdf)

- No errors or warning messages were found when passing through the official [JSHint](https://www.jshint.com/) validator, except for errors related to the use of Bootstrap and Stripe.

### Python Validation:

- [Full Python Validation Report](documentation/validation/python_validation_report.pdf)

- No errors were found when the code was passed through the [CI Python Linter](https://pep8ci.herokuapp.com/).  This checking was done manually by copying python code and pasting it into the validator.

---

## Lighthouse Report

 - [Full Lighthouse Report](documentation/validation/lighthouse_report.pdf)

---