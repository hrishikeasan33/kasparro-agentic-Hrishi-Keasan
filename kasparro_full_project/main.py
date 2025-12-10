
from agents.data_parser import DataParserAgent
from agents.question_generator import QuestionGeneratorAgent
from agents.template_engine import TemplateEngine
from agents.page_assembler import PageAssemblerAgent

from logic_blocks.benefits_block import extract_benefits
from logic_blocks.usage_block import extract_usage
from logic_blocks.safety_block import extract_safety
from logic_blocks.summary_block import generate_summary
from logic_blocks.comparison_block import compare_products

import json

def main():
    productA = DataParserAgent("data/product.json").load_product()

    # Create dummy product B
    productB = {
        "name": "LumaRadiance Vitamin C Serum",
        "concentration": "12% Vitamin C",
        "skin_type": ["Dry", "Combination"],
        "key_ingredients": ["Vitamin C", "Vitamin E"],
        "benefits": ["Brightening", "Hydration"],
        "how_to_use": "Apply 2 drops morning and night",
        "side_effects": "May cause dryness",
        "price": "₹799"
    }

    qg = QuestionGeneratorAgent()
    questions = qg.generate(productA)

    blocks = {
        "benefits": extract_benefits(productA),
        "usage": extract_usage(productA),
        "safety": extract_safety(productA),
        "summary": generate_summary(productA),
        "comparison_points": compare_products(productA, productB)
    }

    engine = TemplateEngine("templates")
    assembler = PageAssemblerAgent(engine, "output")

    faq, prod, comp = assembler.assemble(productA, productB, questions, blocks)

    print("Pipeline completed.")

if __name__ == "__main__":
    main()
