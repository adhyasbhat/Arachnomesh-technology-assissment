# Given n email addresses of different domains, please send an email to the first address(in alphabetical order) of each domain. Please assume a function sendmail() to send the emails.
# (note: give general solution).
# Input Array = ['ghi@hotmail.com', 'def@yahoo.com', 'ghi@gmail.com', 'abc@channelier.com', 'abc@hotmail.com', 'def@hotmail.com', 'abc@gmail.com', 'abc@yahoo.com', 'def@channelier.com','jkl@hotmail.com', 'ghi@yahoo.com', 'def@gmail.com'].

# Expected Output - Below is the  order of address in which sendmail function is going to send mail.
#                                 abc@channelier.com
#                                 abc@yahoo.com
#                                 abc@gmail.com
#                                 abc@hotmail.com


def send_emails(emails):
    domains_dict = {}
    for email in emails:
        domain = email.split('@')[1]
        if domain in domains_dict:
            continue
        else:
            domains_dict[domain] = email
    sorted_domains = sorted(domains_dict.keys())
    sent_emails = []
    for domain in sorted_domains:
        email = domains_dict[domain]
        sendmail(email)
        sent_emails.append(email)
    return sent_emails
emails = ['ghi@hotmail.com', 'def@yahoo.com', 'ghi@gmail.com', 'abc@channelier.com', 'abc@hotmail.com', 'def@hotmail.com', 'abc@gmail.com', 'abc@yahoo.com', 'def@channelier.com','jkl@hotmail.com', 'ghi@yahoo.com', 'def@gmail.com']
send_emails(emails)
