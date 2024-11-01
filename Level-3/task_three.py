"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""



def generate_invoice(receipt_string: str) -> str:

    separate_items_invoice = receipt_string.split("\n")
    print(separate_items_invoice)
    total_vat = 0
    price_no_vat = 0
    for items_invoice in separate_items_invoice:
        new_item = items_invoice.split("£")
        price_no_vat += float(new_item[1])
        total_vat += float(new_item[1]) * 0.2
    rounded_vat = round(total_vat, 2)
    
    lines = receipt_string.strip().split('\n')
    new_receipt_text = '\n'.join(lines[:-1])
    return f"VAT RECEIPT \n\n" + new_receipt_text + f"\nTotal: £{price_no_vat:.2f}Total inc VAT: £{rounded_vat:.2f}"
    




            


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
