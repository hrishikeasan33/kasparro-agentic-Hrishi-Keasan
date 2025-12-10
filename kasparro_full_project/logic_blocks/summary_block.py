
def generate_summary(product):
    return f"{product['name']} is a {product['concentration']} serum with {', '.join(product['key_ingredients'])}."
