class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".net", ".org"]

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not any(domain.endswith(vd) for vd in valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

