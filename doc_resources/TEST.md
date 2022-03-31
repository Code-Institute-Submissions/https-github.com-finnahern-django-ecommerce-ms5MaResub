# Testing

In order to manually test each function of the project I'm going to go through each of the 6 apps and document the expected result of certain actions and compare that to the actual result.

Jump to section:
- [Navbar](#NavBar)
- [Home](#Home)
- [Shop](#Shop)
- [Cart](#Cart)
- [Checkout](#Checkout)
- [Blog](#Blog)
- [User](#User)


# Navbar
#### ACTION: 
Click each of the main navigation links.
#### EXPECTED RESULT:
The site navigates to the indicated html template.
#### ACTUAL RESULT:
As expected.


# Home
#### ACTION: 
Click each of the main navigation links.
#### EXPECTED RESULT:
The site navigates to the shop and blog pages, as indicated.
#### ACTUAL RESULT:
As expected.


# Shop
#### ACTION: 
Click on a book.
#### EXPECTED RESULT:
The product_detail page corresponding to that book's id is rendered.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Submit a search with empty criteria.
#### EXPECTED RESULT:
The shop template is rendered with no filters, showing the full database of 50 books.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Search for "crime".
#### EXPECTED RESULT:
The shop template is rendered with a set including every book in the crime genre and any that might have "crime" in the title or author name.
#### ACTUAL RESULT:
As expected, 10 books in the crime genre are returned.

<br>

#### ACTION: 
Search for "sylvia plath fiction".
#### EXPECTED RESULT:
Returns a set of 11 books, the 10 in the fiction genre and "The Bell Jar" by Sylvia Plath.
#### ACTUAL RESULT:
12 books returned, the above plus "A Beautiful Mind" by Sylvia Nasar. This is actually working correctly.

<br>

#### ACTION: 
Search for "and".
#### EXPECTED RESULT:
Returns a set of books with the string "and" in their title or author.
#### ACTUAL RESULT:
As expected, but the selection of books is odd and not very useful, including authors like **And**rew Roberts and Alex**and**er Dumas as well as any books by 2 authors. This is technically working as intended and I'm not sure what the preferable behaviour would be.

<br>

#### ACTION: 
Search for " ".
#### EXPECTED RESULT:
Possibly same as the empty search criteria.
#### ACTUAL RESULT:
TypeError, Cannot filter against a non-conditional expression.

# Cart
#### ACTION: 
Click add to cart on the product_detail page.
#### EXPECTED RESULT:
The quantity of the desired book is added to the cart.
#### ACTUAL RESULT:
As expected if the quantity field is between 1-99. If the value is outside that range an error message is given by the min and max attributes of the input element. However if the field is empty it crashes and returns a ValueError as the add_to_cart function is expecting an int.

<br>

#### ACTION: 
Click add to cart with non numeral characters in the quantity field.
#### EXPECTED RESULT:
The same error as an empty field.
#### ACTUAL RESULT:
Letters and most non-number characters can't be entered at all. **+**, **-** and **.** can though as they are used as operators but the field creates an error message asking the user to enter a number.

<br>

#### ACTION: 
Click add to cart on the product_detail page after more than 99 of that book are in the cart.
#### EXPECTED RESULT:
Similar error to above as the quantity field also has a range of 1-99.
#### ACTUAL RESULT:
It actually works for seemingly any quantity tested up to 999,999 and calculates the total correctly.

<br>

#### ACTION: 
Click update with 0 in the quantity field.
#### EXPECTED RESULT:
The selected book is removed from the cart.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Click update with a non-numeral character in the quantity field.
#### EXPECTED RESULT:
The field to prevent it from being entered, as above.
#### ACTUAL RESULT:
Throws a ValueError, as the update and remove links are anchor elements, not submit buttons.

<br>

#### ACTION: 
Click remove regardless of the quantity in the cart.
#### EXPECTED RESULT:
The selected book is removed from the cart.
#### ACTUAL RESULT:
As expected.

# Checkout

#### ACTION: 
Add/remove OrderLineItem objects in an order via the admin screen.
#### EXPECTED RESULT:
The order total is updated correctly.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Submit a valid checkout form.
#### EXPECTED RESULT:
A new order object is created using the checkout form data and the contents of the cart and the user is brought to the checkout_success page.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Submit a checkout form checkout form with a valid card, but " " in every required field.
#### EXPECTED RESULT:
The site crashes as the form submits invalid data.
#### ACTUAL RESULT:
As expected, except Stripe succesfully charges the test card. Order object is not instantiated. This has problematic implications for a user earnestly submitting invalid data by mistake. 

# Blog

#### ACTION: 
Create a post using the Add Post button as the admin superuser
#### EXPECTED RESULT:
A new Post object is added to the database and displayed in the blog template
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Edit a post using the Edit Post button as the admin superuser
#### EXPECTED RESULT:
The title and/or body field of the existing Post object is edited.
#### ACTUAL RESULT:
As expected, post slug remains unchanged.

<br>

#### ACTION: 
Delete a post using the Delete Post button as the admin superuser
#### EXPECTED RESULT:
After clicking through the alert, the post object is deleted from the database.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Try to access the Add/Edit/Delete urls as an unregistered user via the browsers address bar.
#### EXPECTED RESULT:
Redirected to the login screen.
#### ACTUAL RESULT:
As expected, except the redirect is to the default allauth login screen and not the custom one.

# User

#### ACTION: 
Register a new account.
#### EXPECTED RESULT:
Get logged into the new account and redirected to home page.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Logout via the dropdown in the navbar.
#### EXPECTED RESULT:
Get logged out and redirected to home page.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Try to login with incorrect username/password.
#### EXPECTED RESULT:
 default allauth invalid login redirect.
#### ACTUAL RESULT:
As expected, but the solution should really be better than this.

<br>

#### ACTION: 
View order history
#### EXPECTED RESULT:
Order history for the current user is displayed as a list with the newest orders on top.
#### ACTUAL RESULT:
As expected.