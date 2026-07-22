class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def formatemail(email) :
            temp = email.split("+")
            return temp[0].replace("." , "")
        seen_emails = set()
        for email in emails :
            temp = email.split("@")
            local_name = temp[0]
            domain_name = temp[1]
            cleaned_email = formatemail(local_name) + "@" + domain_name
            seen_emails.add(cleaned_email)
        return len(seen_emails)