
class QuestionGeneratorAgent:
    def generate(self, product):
        return [
            {"question": f"What is {product['name']} and what does it do?", "category": "Informational"},
            {"question": f"What is the concentration in {product['name']}?", "category": "Informational"},
            {"question": f"How do I use {product['name']}?", "category": "Usage"},
            {"question": f"Can {product['name']} be used daily?", "category": "Usage"},
            {"question": f"Are there any side effects of {product['name']}?", "category": "Safety"},
            {"question": f"Is {product['name']} safe for sensitive skin?", "category": "Safety"},
            {"question": f"What are the benefits of using {product['name']}?", "category": "Benefits"},
            {"question": f"How much does {product['name']} cost?", "category": "Purchase"},
            {"question": f"How does {product['name']} compare to Product B?", "category": "Comparison"}
        ]
