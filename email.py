# Sources used for new knowledge or refresh existing knowledge:
# How to return 2 values from a function and use them:
#     https://note.nkmk.me/en/python-function-return-multiple-values/
# Manipulating class object:
#     https://stackoverflow.com/questions/30313752/manipulating-items-of-array-of-class-objects-in-python
# Learnt about Class, objects, class variables, decorators and inheritance from this youtube playlist:
#     https://www.youtube.com/watch?v=v_Jp11xqCzg&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt

class Email(object):
    """A class that creates an email object.
    """
    inbox = []

    def __init__(self, from_address, contents):
        """The object generator. Requires two arguments: the sender's email address and
        the email contents.
        It is automatically marked as non-spam and unread

        Args:
            from_address (_type_): _description_
            contents (_type_): _description_
        """
        self.from_address = from_address
        self.contents = contents
        self.is_spam = False
        self.has_been_read = False
        self.inbox.append(self.__dict__)

    @classmethod
    def mark_as_read(cls, i):
        """A class method that takes the list index as input and 
        marks the object's parameter "has_been_read" to True

        Args:
            i (into): the object's index
        """
        cls.inbox[i]["has_been_read"] = True

    @classmethod
    def mark_as_spam(cls, i):
        """A class method that takes the list index as input and 
        marks the object's parameter "is_spam" to True

        Args:
            i (int): the object's index
        """
        cls.inbox[i]["is_spam"] = True

    @classmethod
    def get_count(cls):
        """A class method that returns the total number of objects
        in the inbox list

        Returns:
            int: the length of the inbox list
        """
        return len(cls.inbox)

    @staticmethod
    def add_email(from_address, contents):
        """A static method that creates a new Email object.

        Args:
            from_address (str): sender'e email address
            contents (str): email contents
        """
        Email(from_address, contents)

    @staticmethod
    def get_email(i):
        """A static method that returns an e-mail based on its object list index.

        Args:
            i (int): the inbox list index of the email

        Calls single_email_display function to display the email on the screen.
        """
        for index, email in enumerate(Email.inbox):
            if index == i:
                return Email.single_email_display(email)

    @staticmethod
    def display_all():
        """A static method that displays all the emails in the inbox list.
        It also displays the index of the email (ID).
        """
        for index, email in enumerate(Email.inbox):
            print(f"ID: {index}")
            for key in email:
                print(f"{key}: {email[key]}")
            print()

    @staticmethod
    def single_email_display(email):
        """A static method that returns an Email object in a easy to read manner

        Args:
            email (dict): the email object with the values set as its attributes

        Returns:
            str: each dict key and its corresponding value for the given email parameter
        """
        to_display = ''
        for key in email:
            to_display += f"{key}: {email[key]}\n"
        return to_display

    @staticmethod
    def get_unread_emails():
        """A static method that returns all the Email objects which have
        the key "has_been_read" set to False

        Returns:
            str: all Email objects and their indexes that have not been read
        """
        to_display = ''
        for index, email in enumerate(Email.inbox):
            if not email["has_been_read"]:
                to_display += f"ID: {index}\n"
                for key in email:
                    to_display += f"{key}: {email[key]}\n"
                to_display += "\n"
        return to_display

    @staticmethod
    def get_spam_emails():
        """A static method that returns all the Email objects which have
        the key "is_spam" set to True

        Returns:
            str: all Email objects and their indexes that have been marked as spam
        """
        to_display = ''
        for index, email in enumerate(Email.inbox):
            if email["is_spam"]:
                to_display += f"ID: {index}\n"
                for key in email:
                    to_display += f"{key}: {email[key]}\n"
                to_display += "\n"
        return to_display

    @staticmethod
    def err_is_num_in_range(num, options):
        """A static method that error checks if a given "num" could be casted 
        as an int and if it is in the options

        Args:
            num (str): user input
            options (list or string): a set of items or a string where the check is performed

        Returns:
            Not a number: if "num" can not be casted to int
            Not an option: if "num" is not in the "options"
            True (bool): if "num" can be casted as int and is in "options"
        """
        try:
            x = int(num)
        except:
            print("Not a number")
            if num not in options:
                print("Not an option")
            else:
                return True

    @staticmethod
    def send_report():
        """A static method that displays a report of the objects in inbox.
        """
        spam_count = 0
        unread_count = 0
        total_count = Email.get_count()
        # getting total value for 'spam_count and 'unread_count'
        for mail in Email.inbox:
            if mail["is_spam"]:
                spam_count += 1
            if not mail["has_been_read"]:
                unread_count += 1
        # displaying an appropriate message if the inbox hasn't got any emails
        if total_count == 0:
            print("There are no emails in your inbox.")
        # saving an appropriate user-friendly message if spam and unread count are higher than 0
        if unread_count > 0 and spam_count > 0:
            to_print = (f"""Total unread emails - {unread_count}. Breakdown:
{Email.get_unread_emails()}

Total spam emails - {spam_count}. Breakdown:
{Email.get_spam_emails()}
Total number of emails - {total_count}.""")
        # saving an appropriate user-friendly message if unread is 0 and spam is higher than 0
        elif unread_count == 0 and spam_count > 0:
            to_print = (f"""Total unread emails - {unread_count}.Total spam emails - {spam_count}. Breakdown:
{Email.get_spam_emails()}
Total number of emails - {total_count}.""")
        # saving an appropriate user-friendly message if unread is higher than 0 and spam is 0
        elif unread_count > 0 and spam_count == 0:
            to_print = (f"""Total unread emails - {unread_count}. Breakdown:
{Email.get_unread_emails()}Total spam emails - {spam_count}.
Total number of emails - {total_count}.""")
        # saving an appropriate user-friendly message if unread and spam are both 0
        elif unread_count == 0 and spam_count == 0:
            to_print = (f"""Total unread emails - {unread_count}. Breakdown:
{Email.get_spam_emails()}Total spam emails - {spam_count}. Breakdown:
{Email.get_spam_emails()}
Total number of emails - {total_count}.""")
        else:
            print("unexpected error")
        print(to_print)

    @staticmethod
    def delete(i):
        """A static method to delete one email at a given index.

        Args:
            i (int): the index in "inbox" of the email to be deleted
        Returns:
            it will display a list of emails left after deletion
        """
        for index, email in enumerate(Email.inbox):
            if index == i:
                del Email.inbox[index]
                print("Email successfully deleted.")
        Email.display_all()

    @staticmethod
    def request_email_dets():
        """A static method that requests the user to input email details

        Returns:
            str: the user inputs: sender's email address and the email address contents
        """
        sender = input("What is the sender's email address? ")
        contents = input("What are the email contents? ")
        return sender, contents


user_choice = ''
while user_choice != "quit":
    # getting user input on what action to take
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        # displaying an appropriate message if there are no emails in the inbox and
        # asking the user if an email should be added
        if Email.get_count() == 0:
            print("There are no emails in your inbox.")
            while True:
                choice = input("Would you like to add an email? (y/n)").lower()
                if choice == "y":
                    details = Email.request_email_dets()
                    Email.add_email(details[0], details[1])
                elif choice == "n":
                    break
                # otherwise, displaying an error message
                else:
                    print("Incorrect input. Please try again")
        else:
            # if there is at least one email in the inbox,
            # will ask the user to chose from the following options:
            # read, add, delete an email or return to the main menu and
            # doing user input error checking for each step
            # calling the appropriate object methods at each step
            print(f"Your current inbox is: \n")
            Email.display_all()
            while True:
                choice = input("""Type:
1 - to read an email
2 - to add an email
3 - to delete an email
0 - to return to main menu""").lower()
                if not choice.isdigit():
                    print("Your input is not a number. Please try again.")
                elif int(choice) not in [1, 2, 3, 0]:
                    print("Your input is not in the list of options. Please try again")
                else:
                    if choice == "1":
                        while True:
                            choice = input("Type in the ID of the email that you'd like to read: ")
                            if not choice.isdigit():
                                print("You have not entered a number. Please try again")
                            elif int(choice) > Email.get_count() - 1:
                                print("ID typed doesn't exist. Please try again")
                            else:
                                if Email.inbox[int(choice)]["has_been_read"]:
                                    print("Email has already been read.")
                                else:
                                    Email.mark_as_read(int(choice))
                                    print(Email.get_email(int(choice)))
                                    while True:
                                        choice = input("Would you like to read another e-mail? (y/n) ").lower()
                                        if choice == "y":
                                            choice = input("Type in the ID of the email that you'd like to read: ")
                                            if not choice.isdigit():
                                                print("You have not entered a number. Please try again")
                                            elif int(choice) > Email.get_count() - 1:
                                                print("ID typed doesn't exist. Please try again")
                                            else:
                                                if Email.inbox[int(choice)]["has_been_read"]:
                                                    print("Email has already been read.")
                                                else:
                                                    Email.mark_as_read(int(choice))
                                                    print(Email.get_email(int(choice)))
                                        elif choice == "n":
                                            break
                                        else:
                                            print("Invalid input")
                            break
                        break

                    elif choice == "2":
                        details = Email.request_email_dets()
                        Email.add_email(details[0], details[1])
                        print("Email added successfully")
                        while True:
                            user_input = input("Would you like to add another email? (y/n)").lower()
                            if user_input == "y":
                                details = Email.request_email_dets()
                                Email.add_email(details[0], details[1])
                                print("Email added successfully")
                            elif user_input == "n":
                                break
                            else:
                                print("Invalid input. Please try again")
                    elif choice == "3":
                        print(f"Your current inbox is: \n")
                        Email.display_all()
                        while True:
                            choice = input("Type in the ID of the email that you'd like to delete: ")
                            if not choice.isdigit():
                                print("You have not entered a number. Please try again")
                            elif int(choice) > Email.get_count() - 1:
                                print("ID typed doesn't exist. Please try again")
                            else:
                                Email.delete(int(choice))
                                while True:
                                    choice = input("Would you like to delete another email? (y/n)").lower()
                                    if Email.get_count() == 0:
                                        print("There are no emails in the inbox.")
                                        break
                                    elif choice == "y":
                                        choice = input("Type in the ID of the email that you'd like to delete: ")
                                        if not choice.isdigit():
                                            print("You have not entered a number. Please try again")
                                        elif int(choice) > Email.get_count() - 1:
                                            print("ID typed doesn't exist. Please try again")
                                        else:
                                            Email.delete(int(choice))
                                    elif choice == "n":
                                        break
                                    else:
                                        print("Invalid input. Please try again")
                            break
                        break
                    elif choice == "0":
                        break
                    else:
                        print("Fatal error")
    # checking if an email should be marked as spam then
    # error checking the user input and if there are no errors,
    # marking email as spam and displaying it
    elif user_choice == "mark spam":

        while True:
            Email.display_all()
            # requesting user choice input
            choice = input("Type in the ID of the email that you'd like to mark as spam: ")
            if not choice.isdigit():
                print("You have not entered a number. Please try again")
            elif int(choice) > Email.get_count() - 1:
                print("ID typed doesn't exist. Please try again")
            else:
                if Email.inbox[int(choice)]["is_spam"]:
                    print("Email already marked spam.")
                else:
                    Email.mark_as_spam(int(choice))
                    print(Email.single_email_display(Email.inbox[int(choice)]))
                while True:
                    choice = input("Would you like to update another email as spam? (y/n) ").lower()
                    if choice == "y":
                        choice = input("Type in the ID of the email that you'd like to mark as spam: ")
                        if not choice.isdigit():
                            print("You have not entered a number. Please try again")
                        elif int(choice) > Email.get_count() - 1:
                            print("ID typed doesn't exist. Please try again")
                        else:
                            if Email.inbox[int(choice)]["is_spam"]:
                                print("Email already marked spam.")
                            else:
                                Email.mark_as_spam(int(choice))
                                print(Email.single_email_display(Email.inbox[int(choice)]))
                            break
                    elif choice == "n":
                        break
                    else: print("Incorrect input")
            break
    # checking if the user selected "send" and
    # calling the appropriate object method to prepare an inbox report to
    # be displayed for sending 
    elif user_choice == "send":
        Email.send_report()
    # P.S. I wasn't sure if "send" should be used to send an email or what the functionality should be so,
    # I chose to simulate a "send report" like on those G-Suite Dashboards where it shows you how many emails
    # you sent, how many are in your dashboard etc.
    # if needed, this can be easily added to the inbox list or to simulate a "send email" functionality that
    # can add an email to inbox
    
    # exiting the algorithm if the user selected "quit"
    elif user_choice == "quit":
        print("Goodbye")
    # displaying error message as the user input is not in the options list
    else:
        print("Oops - incorrect input")
