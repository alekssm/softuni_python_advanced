from email_val_errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError, InvalidDomainNameError

valid_domains = ["com", "bg", "org", "net"]

while True:
    email = input()
    if email == "End":
        break

    email_parts = email.split("@")
    if len(email_parts) < 2:
        raise MustContainAtSymbolError("Email must contain @")

    if not len(email_parts) == 2:
        raise MustContainAtSymbolError("Email must contain only one @")

    name, domain_all = email_parts
    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_parts = domain_all.split(".")
    if len(domain_parts) < 2 or not all([len(x) > 1 for x in domain_parts[0:len(domain_parts) - 1]]):
        raise InvalidDomainNameError("Invalid domain name")

    domain = domain_parts[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
