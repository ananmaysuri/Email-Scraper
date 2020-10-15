import imaplib
import email
from email.header import decode_header
import re
import pandas as pd

# account credentials
# before this go to https://myaccount.google.com/lesssecureapps?pli=1 and turn on "Allow less secure apps"
username ="enter your email here"
password ="enter your password here"

# set verbose to 0 if you don't want to display the subject and email id of all mails
VERBOSE = 1

# number of emails to check, starting from most recent
N = 7

def email_scraper(username, password):
    # create an IMAP4 class with SSL
    M = imaplib.IMAP4_SSL("imap.gmail.com") # here we used gmail server, change server for other mail service like outlook
    # authenticate
    M.login(username, password)

    status, messages = M.select("INBOX") # here we are selecting the INBOX section, can change the section to SPAM etc.
    # total number of emails
    messages = int(messages[0])
    l=[]
    EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    for i in range(messages, messages - N, -1):
        # fetch the email message by ID
        res, msg = M.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                # email sender
                from_ = msg.get("From")
                if VERBOSE:
                    print("Subject:", subject)
                    print(f"From:{from_}\n")
                # checking if subject contains the sub-string 'Thank you for applying'
                if 'Thank you for applying' in subject:
                    id = re.search(EMAIL_REGEX, from_)
                    l.append(id.group())
    print(f"Found {len(l)} Mails")
    df = pd.DataFrame(l, columns=["Email ID's"])
    print(df)
    # storing email ids in a csv file
    df.to_csv("ID's_file.csv")
    M.close()
    M.logout()

if __name__ == '__main__':
    email_scraper(username, password)