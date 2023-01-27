# Email Simulator

This task is about simulating an email message using a class called Email. The class has four variables: has_been_read, email_contents, is_spam and from_address. The constructor initializes the sender's email address, the contents, marks as unread and non-spam the email by default and appends the newly created email to the inbox list. Then it creates a function called mark_as_read that changes has_been_read to true, and a function called mark_as_spam that changes is_spam to true. It also creates a list called inbox to store all emails. And it creates several functions: add_email which takes in the contents and email address from the received email to make a new Email object, get_count which returns the number of messages in the store, get_email which returns the contents of an email in the list, get_unread_emails which returns a list of all the emails that haven't been read, get_spam_emails which returns a list of all the emails that have been marked as spam, and delete which deletes an email in the inbox.

## Requirements
- Python 3.x

## Usage
- Clone the repository
- Run `email.py`
