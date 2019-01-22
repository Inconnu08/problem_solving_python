import re


def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    for i, email in enumerate(emails):
        pre_email, su_email = email.split('@')
        pre_email = pre_email.replace('.', '')
        emails[i] = re.sub("[+].*[@]", "", pre_email + '@') + su_email

    return len(set(emails))


print(numUniqueEmails(["test.email+alex@leetcode.com",
                       "test.e.mail+bob.cathy@leetcode.com",
                       "testemail+david@lee.tcode.com"]))
