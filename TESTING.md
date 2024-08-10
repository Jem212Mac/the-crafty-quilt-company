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
| 1            | Check that if a user clicks on a product image on the products listing page, they are taken to a product details page for that product. | Click on a product image from the product listings page.                          | The user id taken to a product details page.                                            | Passed |
| 2            | Check that the product details page displays the product image, name, price, category and a description of the product.                 | Look for a product image, name, price, category, and description for the product. | A product image, name, price, category, and description for the product is displayed.   | Passed |
| 3            | Check that the product details page displays a selector for quantity and buttons to 'keep shopping', and 'add to bag'.                  | Look for a quantity selector and buttons to 'keep shopping' and 'add to bag'.     | A quantity selector, a 'keep shopping' button and an 'add to bag' button are displayed. | Passed |


User Story [#11](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/11).

| Test Case ID | Test Condition / Objective                                             | Test Steps                                      | Expected Results                                                | Status |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------- | ------ |
| 1            | Check that a user can sort on category of product in ascending order.  | Navigate to 'All Products>By Category'          | The products are sorted by Category (A-Z); in ascending order.  | Passed |
| 2            | Check that a user can sort on category of product in descending order. | Change to Category (Z-A) via the sort selector. | The products are sorted by Category (Z-A); in descending order. | Passed |


User Story [#12](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/11).

| Test Case ID | Test Condition / Objective                                                                | Test Steps                                                                                                                                                                      | Expected Results                                                                     | Status |
| ------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------ |
| 1            | Check if the user can search for a product using a word in the product name field.        | Input a word/words into the search bar that is present in at least one product name and check that all products with that word or words in the name are listed.                 | All products with that word or words in the product description field are displayed. | Passed |
| 2            | Check if the user can search for a product using a word in the product description field. | Input a word/words into the search bar that is present in at least one product description and check that all products with that word or words in the description are listed.   | All products with that word or words in the product description field are displayed. | Passed |
| 3            | Check if the user can search for a product using a word in the product author field.      | Input a word/words into the search bar that is present in at least one product author field and check that all products with that word or words in the author field are listed. | All products with that word or words in the product author field are displayed.      | Passed |
| 4            | Check if the user can search for a product using a word in the product brand field.       | Input a word/words into the search bar that is present in at least one product brand field and check that all products with that word or words in the brand field are listed.   | All products with that word or words in the product brand field are displayed.       | Passed |


User Story [#13](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/13).

| Test Case ID | Test Condition / Objective                                                                                                                                       | Test Steps                                                                                                                                            | Expected Results                                                                                        | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------ |
| 1            | Check that when a user searches for a particular word using the search bar, the results are displayed along with the word searched for and the nmber of results. | Input a specific word into the search bar and check that the correct word searched for is displayed along with the results and the number of results. | The results are displayed along with the word that was searched for and the number of results returned. | Passed |


User Story [#10](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/10).

| Test Case ID | Test Condition / Objective                                                                  | Test Steps                                                                            | Expected Results                                              | Status |
| ------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------ |
| 1            | Check that the user can search 'All Products' by Price (low-to-high)                        | Navigate to 'All Products' and select 'Price (low-to-high)' on the sort bar.          | All available products are displayed by price, ascending.     | Passed |
| 2            | Check that the user can search 'All Products' by Price (high-to-low)                        | Navigate to 'All Products' and select 'Price (high-to-low)' on the sort bar.          | All available products are displayed by price, decsending.    | Passed |
| 3            | Check that the user can search 'All Products' by Name (A-Z)                                 | Navigate to 'All Products' and select 'Name (A-Z') on the sort bar.                   | All available products are displayed by name, ascending.      | Passed |
| 4            | Check that the user can search 'All Products' by Name (Z-A)                                 | Navigate to 'All Products' and select 'Name (Z-A)' on the sort bar.                   | All available products are displayed by name, decsending.     | Passed |
| 5            | Check that the user can search 'All Products' by Category (A-Z)                             | Navigate to 'All Products' and select 'Category (A-Z)' on the sort bar.               | All available products are displayed by category, ascending.  | Passed |
| 6            | Check that the user can search 'All Products' by Category (A-Z)                             | Navigate to 'All Products' and select 'Category (Z-A)' on the sort bar.               | All available products are displayed by category, decsending. | Passed |
| 7            | Check that the user can search 'Baby Quilts' (or any other category) by Price (low-to-high) | Navigate to 'Quilts>Baby Quilts' and select 'Price (low-to-high)' on the sort bar.    | All baby quilts are displayed by price, ascending.            | Passed |
| 8            | Check that the user can search 'Baby Quilts' (or any other category) by Price (high-to-low) | Navigate to ' 'Quilts>Baby Quilts'' and select 'Price (high-to-low)' on the sort bar. | All baby quilts are displayed by price, decsending.           | Passed |
| 9            | Check that the user can search 'Baby Quilts' (or any other category) by Name (A-Z)          | Navigate to  'Quilts>Baby Quilts'' and select 'Name (A-Z') on the sort bar.           | All baby quilts are displayed by name, ascending.             | Passed |
| 10           | Check that the user can search 'Baby Quilts' (or any other category) by Name (Z-A)          | Navigate to  'Quilts>Baby Quilts'' and select 'Name (Z-A)' on the sort bar.           | All baby quilts are displayed by name, decsending.            | Passed |
| 11           | Check that the user can search 'Quilts' by Category (A-Z)                                   | Navigate to ' 'Quilts'' and select 'Category (A-Z)' on the sort bar.                  | All quilts are displayed by category, ascending.              | Passed |
| 12           | Check that the user can search 'Quilts' by Category (A-Z)                                   | Navigate to ' 'Quilts'' and select 'Category (Z-A)' on the sort bar.                  | All quilts are displayed by category, descending.             | Passed |


User Story [#3](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/3).

| Test Case ID | Test Condition / Objective                                             | Test Steps                                                                                                               | Expected Results                                                   | Status |
| ------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | ------ |
| 1            | Check that a user can add a selection of products to the shopping bag. | Navigate to a product and select add to bag.  Navigate to another product and select add to bag.  Do this several times. | All of the items selected should be available in the shopping bag. | Passed |


User Story [#4](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/4).

| Test Case ID | Test Condition / Objective                                                                                 | Test Steps                                                                                                                                                                                            | Expected Results                                                                                                                                               | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 1            | Check that if a user has added items to the shopping bag, they can see the contents of the bag at anytime. | Add one or more products to the shopping bag.  Click on the shopping bag icon in the top right corner of the site to open it.  Click elsewhere  within the site and then go back to the shopping bag. | The contents of the shopping bag should be displayed and should remain in the bag even if the user clicks elswhere in the site and then comes back to the bag. | Passed |
| 2            | Check that the bag displays each item that has been added to the bag, and the quantity of each item.       | Add one or more products to the shopping bag.  Click on the shopping bag icon in the top right corner of the site to open it.                                                                         | The bag should display each item that has been added to the bag and the quantity of each item.                                                                 | Passed |
| 3            | Check that the bag displays the total cost for the contents of the bag.                                    | Add one or more products to the shopping bag.  Click on the shopping bag icon in the top right corner of the site to open it.                                                                         | The bag should display the total cost for the items in the bag, including delivery.                                                                            | Passed |


User Story [#14](https://github.com/Jem212Mac/the-crafty-quilt-company/issues/14).

| Test Case ID | Test Condition / Objective                                                                                       | Test Steps                                                                                                                                           | Expected Results                                                                            | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| 1            | Check that a user can select a specific quantity of a product to add to their bag from the product details page. | Navigate to the product details page for a product and input a specific quantity into the quantity bar and click add to bag.                         | The quantity of items selected should be added to the bag.                                  | Passed |
| 2            | Check that user cannot select less than 1 product from product details page.                                     | Navigate to the product details page for a product and and use the - button on the quantity bar to try to select less than one.                      | The - button should be disabled at 1 and should not allow the user to select less than 1.   | Passed |
| 3            | Check that user cannot select more than 99 of a product from the product details page.                           | Navigate to the product details page for a product and and use the + button on the quantity bar to try to select more than 99.                       | The + button should be disabled at 99 and should not allow the user to select more than 99. | Passed |
| 4            | Check that a user can adjust the quantity of a product on the shopping bag page.                                 | Once a product has been added to the bag, navigate to the shopping page and and input a specific quantity into the quantity bar and click Update.    | The quantity of items should be updated.                                                    | Passed |
| 5            | Check that user cannot select less than 1 product from the shopping bag page.                                    | Once a product has been added to the bag, navigate to the shopping page and and use the - button on the quantity bar to try to select less than one. | The - button should be disabled at 1 and should not allow the user to select less than 1.   | Failed |
| 6            | Check that user cannot select more than 99 of a product from the shopping bag page.                              | Once a product has been added to the bag, navigate to the shopping page and and use the + button on the quantity bar to try to select more than 99.  | The + button should be disabled at 99 and should not allow the user to select more than 99. | Failed |

---

## Usability / User Acceptance Testing

In addition to the testing I performed throughout the developement process which was primarily based around the user stories and the acceptance criteria (as detailed above), I also performed some exploratory testing based on the following user journeys with the goal of ensuring that the site would meet the expectations of a user in terms of ease of use, ease of navigation, responsiveness of buttons and links etc.  My aim was to ensure that user's would have a pleasant experience interacting with the site and that the overall display of content to the user was appropriate and appealing (clear, clean and uncluttered).

1. 

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

1. 

---

## Validation:

### HTML Validation:

- [Full HTML Validation Report]()

- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator.

### CSS Validation:

- [Full CSS Validation Report]()

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/) validator.

### JS Validation:

- [Full JS Validation Report]()

- No errors or warning messages were found when passing through the official [JSHint](https://www.jshint.com/) validator, except for an error related to the use of Bootstrap.

### Python Validation:

- [Full Python Validation Report]()

- No errors were found when the code was passed through the [CI Python Linter](https://pep8ci.herokuapp.com/).  This checking was done manually by copying python code and pasting it into the validator.

---

## Lighthouse Reports

### Home Page

![Lighthouse Report - Home Page]()


---