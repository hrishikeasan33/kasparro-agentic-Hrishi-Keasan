
import json

class TemplateEngine:
    def __init__(self, template_dir):
        self.dir = template_dir

    def load_template(self, name):
        return json.load(open(f"{self.dir}/{name}"))

    def fill_product(self, t, p, blocks):
        t["product_name"] = p["name"]
        t["ingredients"] = p["key_ingredients"]
        t["usage"] = blocks["usage"]
        t["benefits"] = p["benefits"]
        t["price"] = p["price"]
        t["summary"] = blocks["summary"]
        t["safety"] = p["side_effects"]
        return t

    def fill_comparison(self, t, A, B, points):
        t["product_A"] = A
        t["product_B"] = B
        t["comparison_points"] = points
        return t
