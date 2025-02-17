import re


def find_customer(some_string):
    customer = re.findall(r"%([A-Z][a-z]+)%", input_line)
    return False if not customer else customer[0]


def find_product(some_string):
    product = re.findall(r"<(\w+)>", input_line)
    return False if not product else product[0]


def find_count(some_string):
    count = re.findall(r"\|(\d+)\|", input_line)
    return False if not count else int(count[0])


def find_price(some_string):
    price = re.findall(r"([0-9]+\.?[0-9]+)[$]", input_line)
    return False if not price else float(price[0])


input_line = input()
income = 0

while input_line != "end of shift":

    if find_customer(input_line) and find_product(input_line) and find_count(input_line) and find_price(input_line):
        total_price = find_count(input_line) * find_price(input_line)
        print(f"{find_customer(input_line)}: {find_product(input_line)} - {total_price:.2f}")
        income += total_price

    input_line = input()

print(f"Total income: {income:.2f}")

