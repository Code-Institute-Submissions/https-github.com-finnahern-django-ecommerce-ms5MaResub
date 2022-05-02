# Milestone 5 resubmission

This is the Readme document for the updated version of this project. The original, unchanged Readme is [here](https://github.com/finnahern/django-ecommerce-ms5/blob/main/README.md).

The issues with the original submission that needed to be addressed in this version were the following:
- The order confirmation page referred to a confirmation email that did not exist.
- SEO mechanisms such as the robots.txt and sitemap.xml files as well as meta tags in the html documents were absent.
- A custom 404 page was absent.
- The login and registration pages were accessible to logged in users.
- There was no mockup Facebook page for the store.
- The newsletter form was only a dummy, nothing was done with the email addreesses submitted.

### Confirmation email

After investigating how to send [automated emails](https://docs.djangoproject.com/en/4.0/topics/email/) [using Django](https://www.sitepoint.com/django-send-email/), I decided that given my limited time frame this was too complex to implement and that, since automated emails are not required per criteria 1.2, the fix was simply to remove the reference to the non-existent email on the order confirmation page. Adding this functionality would be something I'd like to include in any future revisions to the project.

### SEO

IN order to improve SEO and add useful context for search engines to find the site I added a robots.txt file and generated a sitemap.xml file using [xml-sitemaps.com](https://www.xml-sitemaps.com/). I also added meta tags to the base html template.

### Custom 404 page

The original version of the site did not include a custom error 404 page. This was simple to add by including a 404 handler in the project level urls.py file and a function to render the custom template in views.py in the home app. The template features an error message to the user and a button to go back to the previous page in their browser history. The advantage of a custom 404 page is that the user still has access to the navbar from the base template. 

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/404.PNG" width="50%" height="50%"/>

### Login and registration access

In order to prevent users who were already logged in from accessing the login or registration pages I added a check to each of the views for those pages to see if the current user is authenticated and if so, redirect them back to the shop page.

### Mockup Facebook page

A screenshot of the mocked up Facebook page for the site is included in the doc_resources directory

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/facebook.PNG" width="50%" height="50%"/>

### Newsletter form

In order to actually do something with the email addresses provided by the newsletter form I signed up for a Mailchimp account and used their API to store the subissions as a mailing list.

This was achieved by storing the API key and mail list ID provided by Mailchimp as enviornment variables and implementing a subscribe function to views.py in the user app which is called when the form is submitted along with the email field as an argument. The function then submits the given email address to Mailchimp to add to the mailing list. 

I found a very useful [guide](https://www.pythonstacks.com/blog/post/integrating-mailchimp-django/) on how to integrate the API. As you can see in the below screenshot, the dummy email addresses I submitted using the form are saved correctly to the mailing list.

<img src="https://raw.githubusercontent.com/finnahern/django-ecommerce-ms5/main/doc_resources/screenshots/Mailchimp.PNG" width="50%" height="50%"/>