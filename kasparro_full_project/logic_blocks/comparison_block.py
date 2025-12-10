
def compare_products(A, B):
    shared = list(set(A["key_ingredients"]) & set(B["key_ingredients"]))
    only_A = list(set(A["key_ingredients"]) - set(B["key_ingredients"]))
    only_B = list(set(B["key_ingredients"]) - set(A["key_ingredients"]))

    return [
        {"point": "price", "A": A["price"], "B": B["price"]},
        {"point": "ingredients", "shared": shared, "only_A": only_A, "only_B": only_B}
    ]
