
import json

class PageAssemblerAgent:
    def __init__(self, engine, out):
        self.engine = engine
        self.out = out

    def generate_answer(self, q, p, blocks):
        cat = q["category"]
        ques = q["question"]

        if cat == "Usage": return blocks["usage"]
        if cat == "Safety": return p["side_effects"]
        if cat == "Benefits": return ", ".join(p["benefits"])
        if cat == "Purchase": return f"The price is {p['price']}."
        if cat == "Comparison":
            return "Both products share Vitamin C but differ in remaining ingredients."

        if "Vitamin C" in ques:
            return "Vitamin C brightens skin and fades pigmentation."

        if "Hyaluronic Acid" in ques:
            return "Hyaluronic Acid hydrates and plumps skin."

        return blocks["summary"]

    def assemble(self, product, productB, questions, blocks):
        # FAQ
        faq_t = self.engine.load_template("faq_template.json")
        faq_t["product_name"] = product["name"]
        faq_t["faqs"] = []

        for q in questions:
            faq_t["faqs"].append({
                "question": q["question"],
                "category": q["category"],
                "answer": self.generate_answer(q, product, blocks)
            })

        json.dump(faq_t, open(f"{self.out}/faq.json","w"), indent=2)

        # PRODUCT PAGE
        prod_t = self.engine.load_template("product_template.json")
        prod_out = self.engine.fill_product(prod_t, product, blocks)
        json.dump(prod_out, open(f"{self.out}/product_page.json","w"), indent=2)

        # COMPARISON
        comp_t = self.engine.load_template("comparison_template.json")
        comp_out = self.engine.fill_comparison(comp_t, product, productB, blocks["comparison_points"])
        json.dump(comp_out, open(f"{self.out}/comparison_page.json","w"), indent=2)

        return faq_t, prod_out, comp_out
