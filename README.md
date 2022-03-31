# Corner Bookshop

[Link to deployed site.](https://cornerbooks-ms5.herokuapp.com/)

A project using Django to create a commercial grade ecommerce website. The site uses a Postgres database to handle a number of bespoke data models to dynamically serve content and respond to user actions.

I believe this project serves a strong base and many of its functions can be repurposed into future ecommerce applcations and other projects. Unfortunately there are a number of features I would have liked to include for a more complete user experience that were not feasible due to time constraints. These are detailed in [improvements](#Improvements) section below.

The deployed website can be found at the link above. The credentials for the admin superuser have been provided with the project submission. If you wish to test account functionality, regular user accounts can be created using the site's registration form accessible via the main nav bar.

# UX/Design
Given the brief to create an ecommerce site, the design is focused on making the user experience simple and accessible. The process of browsing the store, adding products to the cart and checking out should be as seamless as possible. Details about each book are easily visible from the main store page, or only a click away to get more information. The main nav bar from the base template is fixed to the top of the view window allowing easy access to every part of the site.

### Wireframes
Before writing a single line of code, I mocked up some wireframes using [Invision](https://www.invisionapp.com/), an online took I found. I ended up sticking quite closely to this early vision. The wire frames can be found [here](https://github.com/finnahern/django-ecommerce-ms5/tree/main/doc_resources/wireframes)

### User stories

Along with designing a wireframe mockup of the site I wrote a set of user stories at the onset of the project to get an idea of the functionality the site would need. I used Github's built in [project board](https://github.com/finnahern/django-ecommerce-ms5/projects/1) to track my progress on achieving these goals, most of which can be seen in the final product although some had to be shelved due to time constraints. I've included the original user stories below.

### Customer

As a customer I want to be able to:

- Browse books and add ones I want to my cart without interrupting my navigation of the site.
- Specify the quantity of each book I want to add to my cart so I can order multiple copies of a book with one click.
- Search for books, so I can quickly find if what I'm looking for is available.
- Pay for my order using my bank card, with as few barriers to this transaction as possible.
- Receive a visual cue confirming my order, so I know it's been processed correctly.
- View detailed information about each book in the store, to help decide if it's right for me.
- Browse the store's blog for news and updates.
- View my order history to see what I purchased previously and when and how much I paid.

### Store owner

As the store owner I want to be able to:

- Add new products to the database and have them automatically display on the website so customers can purchase them.
- Edit details of existing products, such as price if I want to offer a discount.
- Hide products from display, so I can prevent customers from viewing and buying them without deleting their database entry.
- View and edit customer orders so I can deal with customer support queries and solve mistakes.
- View, create, edit and delete blog posts from within the website itself.

# Features

The first thing that a new user's eye will be drawn to when they arrive at the site is the header and main nav bar, featured on every page of the site. The header includes the shop's logo which links back to the home page, a search bar allowing users to look up book titles, authors or genres and 4 buttons on the nav bar leading to the main sections of the site: the shop, the blog, the user options, and the shopping cart.

The package has been broken up into six distinct apps, the features of each of which I've detailed below.

## Home

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/home.PNG" width="50%" height="50%"/>

The home app is the simplest, but it was my starting point upon which I built the rest of the project. It renders the index.html template, which displays a photograph by Horst Friedrichs of the Shakespeare & Co bookshop in Paris and invites the user to browse the shop or the blog, the two main sections of the website.

## Shop

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/shop.PNG" width="50%" height="50%"/>

Selling books is the main purpose of the website, so the shop app is the most important. From here the user can see the complete collection of books available from the database, find what they're looking for with the powerful search bar and view each book's product_detail page to add it to their cart.

Some features of the shop app include:

- Data models for each book as well as 5 genres, which are included as foreign keys of the book objects.
- A search function in the all_products view which allows the user to enter in a title, author name or genre, or any combination of the three, as search criteria and for the set of books displayed to the user to adapt to this criteria. For example, entering "Truman Capote crime" into the search bar will display both books by Capote in the database as well as every book in the crime genre.

## Cart

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/cart.PNG" width="50%" height="50%"/>

What use is a shop if you can't buy anything? The cart app allows the user to add books to their cart from the book's product_detail page. The cart link in the nav bar then updates in real time with the session's current total. From the cart page itself the user can remove books from the cart or edit the quantity they wish to purchase.

## Checkout

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/checkout.PNG" width="60%" height="60%"/>

The checkout app includes the Order and OrderLineItem data models allowing the website to track purchases made and, in a real world scenario, fulfill those orders. The checkout also features Stripe integration which can be seen in the card element at the bottom of the checkout form. In order to test the checkout process, please use Stripe's test card numbers: 4242 4242 4242 4242 or 4000 0025 0000 3155 if you wish to test a payment that fails to authenticate. The expiry date, CVC and postcode for both cards are 04/24 242 424242 respectively.

Once the cart is checked out successfully, a new Order object is instantiated and saved to the database and the user is brought to the order success page showing them a summary of their order. If the user is logged in, this page can be accessed again later via their order history.

## Blog

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/blog.PNG" width="60%" height="60%"/>

The blog app features the Post data model, which includes full CRUD functionality, only accessible by the admin superuser account. 

Individual blog posts are displayed as a list in the blog.html order in descending order from the newest. From here users can click on a post's title to view it in detail and read the full post and the admin superuser can acess the Add Post button which leads to the form to create a new blog post. Each post has it's own page with a url dynamically created using a combination of the post's title and its creation time. From the blog_post page, the admin can also edit and delete the existing posts.

## User

The user app governs all the functions related to user accounts: logging in and out, registering new accounts and viewing the current account's order history.

The order_history function in the view filters all instances of the Order model to those whose user field matches the username of the currently logged in account and a for loop in the template displays a list of these orders. Each order number can be clicked on to return to that order's confirmation page if the user wishes to confirm any details of their order.

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/order_history.PNG" width="60%" height="60%"/>

## Improvements
There are a number of ideas for features I would have liked to include but couldn't for a variety of reasons not least of which was the time limit. I've listed some of these below.

- Add defensive programming during the checkout process to prevent edge cases where the user deliberately or accidentally navigates away from the checkout page before the payment has fully authenticated, resulting in the card being charged but no order object being created.
- Create a more in depth search function. I am quite proud of how the search function turned out but there are always improvement that can be made. For instance there are a few books with two authors in the database and it doesn't handle those well.
- Add pagination on the store, blog and order history pages would help make those pages easy to navigate as well as cut down on image hosting costs at scale.
- Create clearer visual confirmation that a book has been added to the user's cart. Right now the only confirmation is that the cart total amount in the nav bar increases but this is easy to miss. I would have liked to have used Bootstrap's toasts to provide a notification to confirm when the cart is updated.
- Provide a form for user's to change their password.
- Add more functionality associated with having a user account such as the ability to save delivery information to the account to make future orders easier and to comment on blog posts.
- Collect email addresses from the newsletter form and use a service like [Mailchimp](https://mailchimp.com/) to create a mailing list.

# Testing

## Manual testing

I have manually tested each feature of the site throughout development as well as a final pass after the code was completed. Full details of which can be found [here]().

## Validation

All Python code in the project has succesfully passed [PEP8 validation](http://pep8online.com/) without any errors that would affect the functioning of the code. Most files passed without any problems at all and those that didn't were mostly limited to "line too long" errors.

## Bugs fixed

One notable bug I fixed during development was in the search function, in the views of the shop app. An early version of the code was simply looking to see if the names of the genres were included in the search criteria string and adding all the books belonging to that genre to the query set if they were. This meant that searching "nonfiction", "non-fiction" or "non fiction" would return all the books in the non-fiction genre **as well** as all the books in the fiction genre as "fiction" is included in all of those strings.

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/genresearchbug.PNG" width="70%" height="760%"/>

## Known issues

Despite extensive testing there are a number of bugs and issues that persist in the code that I either couldn't, or didn't have the time to fix.
- Blog posts' urls are generated using the time they were created and their slug, which is derived from the post title. This means that if 2 posts with the same title are created in the same minute as each other they will have identical urls and neither can be accessed until 1 is deleted via the admin back end. Originally the url only used the date of creation meaning this was a much bigger problem. I opted to include the hour and minute of creation in the url and presume that a store owner is very unlikely to make 2 blog posts in the same minute, never mind 2 with the same title.
- Logged in users can still access the registration form and create a new account without logging out via the URL.
- The order history page is populated via the "user" field of the Order model. This is just a CharField populated by the username of the logged in user when the order is place. This means that if a user account is deleted, and then another created with the same username, the new account will "inherit" the order history of the old account. This would present serious data protection concerns in a real-world scenario.
- Submitting the search bar with empty criteria is the same as no criteria, but searching for " " returns a TypeError as the logic can't account for a non-conditional statement. This can probably be resolved with an if statement checking that the criteria isn't just whitespace and giving the user an error message if they try.
- If the quantity field on the product_detail page is empty and you click "Add to Cart" the site crashes and returns a ValueError as the add_to_cart function is expecting an int. Some custom form validation is needed to prevent unexpected values being submitted.
- Clicking update in the cart with a non-numeral character in the quantity field throws a ValueError as the update button is an anchor element, not a submit button. As above, more validation is needed on the minor forms throughout the site.

# Deployment

The project was deployed using Heroku with a PostgreSQL database and using Amazon Web Services to host static and media files.

### Steps for deployment
- Create a new Heroku app
- Install the Heroku Postgres Add-on
- Ensure Config Vars, such as DATABASE_URL and SECRET_KEY are configured correctly in setting.py
- Link the Heroku app to the Github repository
- Click deploy
- Set up a new AWS bucket and configure settings.py to use it as the static and media urls.

# Credits

## Acknowledgements

Spencer Barriball for his feedback and advice and recommending invaluable resources

David Malone and Colm Tang for their help and advice.

## Technology used
- [Django 4.0](https://docs.djangoproject.com/en/4.0/)
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- HTML
- CSS
- Javascript
- [PostgreSQL](https://www.postgresql.org/) - Database used to store data models
- [Gunicorn](https://gunicorn.org/)
- [Git](https://git-scm.com/) - Version control.
- [Github](https://github.com/) - Used to host repository and live site.
- [Gitpod IDE](https://gitpod.io/) - Development enviornment used to build site.

## Frameworks
- [Bootstrap](https://getbootstrap.com/) - CSS Framework used to format most of the elements in the site.
- [JQuery](https://jqueryui.com/) - Javascript library
- [Font Awesome](https://fontawesome.com/) - Resource for icons used throughout the site.
- [Django-allauth](https://www.intenct.nl/projects/django-allauth/)
- [Django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- [Django-humanize](https://docs.djangoproject.com/en/4.0/ref/contrib/humanize/)

## Third party services
- [Heroku](https://www.heroku.com/) - Cloud service hosting the deployed site.
- [Amazon Web Services](https://aws.amazon.com/) - Cloud service hosting static and media files.
- [Pep8 validator](http://pep8online.com/) - Used to validate code and check for errors.

## Resources

- [Django 3 By Example - Third Edition by Antonio Melé](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)
- [Django 4.0 Documentation](https://docs.djangoproject.com/en/4.0/)
- [W3Schools](https://www.w3schools.com/)
- [Stackoverflow.com](https://stackoverflow.com/)

## Image credits
- [Shakespeare & Co., Paris by Horst Friedrichs](https://horstfriedrichs.com/shelf-portraits)
- All book cover images are property of their respective publisher.