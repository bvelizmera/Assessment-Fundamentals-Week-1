"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""



def generate_invoice(receipt_string: str) -> str:
    lines = receipt_string.strip().split('\n')
    new_receipt_text = '\n'.join(lines[:-1])

    separate_items_invoice = new_receipt_text.split("\n")
    total_vat = 0
    price_no_vat = 0
    for items_invoice in separate_items_invoice:
        new_item = items_invoice.split("£")
        price_no_vat += (float(new_item[1]))
        total_vat += float(new_item[1]) * 0.2
    rounded_vat = round(total_vat, 2)

    total_new_price = price_no_vat + rounded_vat
    

    return f"VAT RECEIPT \n\n" + new_receipt_text + f"\n\nTotal: £{price_no_vat:.2f}\nVAT: £{total_vat:.2f}\nTotal inc VAT: £{total_new_price:.2f}"
    




            


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
