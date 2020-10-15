# Email-Scraper

This project was made with PyCharm IDE in Python 3.7 Virtualenv.

## Steps to Execute:-
1. Open this Project with PyCharm.
2. In the terminal enter the following command to install dependencies "pip install -r requirements.txt".
3. In the main.py, do the following changes:-
- If using Gmail, go to https://myaccount.google.com/lesssecureapps?pli=1 with your account signed in and turn on "Allow less secure apps".
- Enter your Email ID and Password.
- Set VERBOSE to 0 if you don't want to display the subject and email id of all mails. (Optional)
- Set N to the number of Email's to check, starting from most recent.
- If not using Gmail, change the server to any of the servers given in the link : https://www.systoolsgroup.com/imap/
- You can change section of Email's, just replace "INBOX" by "SPAM" etc.
4. Run main.py.
5. Dataframe of Email's will be displayed in the terminal and also exported into CSV file.
