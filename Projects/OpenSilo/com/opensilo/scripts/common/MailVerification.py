__author__ = 'sandeeps'


#!/usr/bin/env python
#
# Very basic example of using Python and IMAP to iterate over emails in a
# gmail folder/label.  This code is released into the public domain.
#
# RKI July 2013
# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
#
from com.opensilo import opensilo
import sys
import imaplib
import getpass
import email
import email.header
import datetime
import re


EMAIL_ACCOUNT = opensilo.emailid
password = opensilo.password

def process_mailbox(M,opensilo_email_found):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "UnSeen")
    if rv != 'OK':
        print "No messages found!"
        return
    if not data[0].split():
        opensilo_email_found = False
        return "No Email found!",opensilo_email_found
    else:
        opensilo_email_found = True
        print (str(data[0].split()) + ' unseen emails found!')
        for num in data[0].split():
            print 'Processing '+ num + ' email......'
            rv1, data1 = M.fetch(num, '(RFC822)')
            if rv1 != 'OK':
                print "ERROR getting message", num
                return

            msg = email.message_from_string(data1[0][1])
            decode = email.header.decode_header(msg['Subject'])[0]
            subject = unicode(decode[0])
            if subject == 'Welcome To OpenSilo!':
                print 'Message %s: %s' % (num, subject)
                print 'Raw Date:', msg['Date']
                # Now convert to local date-time
                date_tuple = email.utils.parsedate_tz(msg['Date'])
                if date_tuple:
                    local_date = datetime.datetime.fromtimestamp(
                        email.utils.mktime_tz(date_tuple))
                    print "Local Date:", \
                        local_date.strftime("%a, %d %b %Y %H:%M:%S")
                print('-------------------------------------------------------------')
                #print msg
                #print('-------------------------------------------------------------')
                auth_token = re.findall("token=3D\W*(.*?)\" target", str(msg), re.DOTALL | re.MULTILINE)[0]
                activation_URL = opensilo.opensiloURL+'?token='+str(re.sub(r"=+","",auth_token))
    return activation_URL, opensilo_email_found

def get_activationURL():

    M = imaplib.IMAP4_SSL('imap.gmail.com')
    opensilo_email_found = False


    try:
        rv, data = M.login(EMAIL_ACCOUNT,password )
    except imaplib.IMAP4.error:
        print "LOGIN FAILED!!! "
        sys.exit(1)

    rv, mailboxes = M.list()

    while opensilo_email_found == False:
        rv, data = M.select('INBOX')
        if rv == 'OK':
            print "Processing mailbox...\n"
            activation_link, opensilo_email_found = process_mailbox(M,opensilo_email_found)
            print activation_link
        else:
            print "ERROR: Unable to open mailbox ", rv

    if opensilo_email_found == True:
        M.close()
    M.logout()
    return activation_link

#get_activationURL()

