class EmailVerifier:
    def __init__(self, domains=None):
        # Initialize with a list of domains if provided, otherwise use a default list
        if domains is None:
            domains = ["mymail.pomona.edu"]
        self.domains = domains

    def verify_email(self, email):
        """
        Verify if the provided email ends with any of the expected domains.

        Args:
            email (str): The email address to verify.

        Returns:
            bool: True if the email ends with any of the specified domains, False otherwise.
        """
        # Check if the email ends with any of the domains in the list
        print("is this valid or not")
        return any(email.endswith(domain) for domain in self.domains)





#____________________________EXAMPLE USAGE____________________________________________________________________________________________________________________#
# Example usage of the EmailVerifier class
if __name__ == "__main__":
    # List of domains to verify against
    domains = ["mymail.pomona.edu", "student.claremont.edu", "alumni.pomona.edu", "faculty.pomona.edu", "staff.pomona.edu"]
    verifier = EmailVerifier(domains)
    test_emails = ["user@mymail.pomona.edu", "visitor@anotherdomain.com", "professor@faculty.pomona.edu"]

    for email in test_emails:
        result = verifier.verify_email(email)
        print(f"Does the email '{email}' end with one of the specified domains? {result}")


#__________________________________________________________________________________________________________________________________________________#