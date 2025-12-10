# ⚡ Kasparro Applied AI – Agentic Content System  
### Built by **Hrishikeasan N. P**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AI-MultiAgent-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>
</p>

---

## 🚀 Project Overview

This system is a fully modular **multi-agent AI content generation pipeline** developed for the  
**Kasparro Applied AI Engineer Challenge**.

It generates:

- ✔ Product Page  
- ✔ FAQ Page  
- ✔ Product Comparison Page  
- ✔ JSON structured outputs  
- ✔ Premium Streamlit UI for visualization  

The solution is built using AI agents, template-driven generation, logic blocks, and a clean UI dashboard.

---

## 🧠 **System Features**

### 🔹 Multi-Agent Architecture  
- **FAQ Agent**  
- **Product Page Agent**  
- **Comparison Agent**

Each agent independently generates a specific content block.

### 🔹 Modular Logic Blocks  
Reusable units for prompt creation, JSON parsing, validation, and formatting.

### 🔹 Template-Based Output  
Ensures consistent product descriptions, FAQs, and comparison layouts.

### 🔹 Streamlit Visualization  
A premium UI with:
- Tabs  
- Expandable FAQs  
- Gradient cards  
- Ingredient comparison  
- Price verdict section  

---

## 📸 **Screenshots**

### 🖼 FAQ Page  
![FAQ Page]<img width="1849" height="812" alt="image" src="https://github.com/user-attachments/assets/b0c8676d-cd91-48bf-bbf0-97ac91601a30" />


---

### 🖼 Comparison Page – Top Section  
![Comparison Top]<img width="1863" height="862" alt="image" src="https://github.com/user-attachments/assets/3fc8f882-585e-43a8-8acb-52f6a6f09358" />


---

### 🖼 Comparison Page – Mid Section  
<img width="1821" height="797" alt="image" src="https://github.com/user-attachments/assets/3d9cb696-689a-4c6e-831b-39ce4474bc77" />


---

### 🖼 Comparison Page – Final Price Verdict  
<img width="1845" height="469" alt="image" src="https://github.com/user-attachments/assets/496696ed-8eba-4935-b2f7-01d333ad079f" />


---

## 📂 **Folder Structure**
project/
│
├── agents/ # Multi-agent logic for FAQ, Product, Comparison
├── data/ # Input product data and prompt assets
├── logic_blocks/ # Modular logic units (prompting, validation, parsing)
├── output/ # Generated JSON files (faq.json, product_page.json, comparison_page.json)
├── templates/ # Reusable templates for structured generation
│
├── app.py # Streamlit UI for interactive visualization
├── main.py # Main pipeline orchestrator



---

🔧 Installation
Prerequisites

Python 3.8 or higher
pip (Python package installer)
Git (for cloning the repository)

Local Setup

Clone the repository

bashgit clone https://github.com/yourusername/multi-agent-content-generator.git
cd multi-agent-content-generator

Create a virtual environment (recommended)

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashpip install -r requirements.txt

Set up environment variables

bashcp .env.example .env
# Edit .env and add your API keys
🚀 Usage
Running the Agent Pipeline
Execute the main agent pipeline:
bashpython main.py
Launch the Streamlit UI
Start the interactive web interface:
bashstreamlit run app.py
The application will open in your default browser at http://localhost:8501
Command Line Options
bash# Run with specific configuration
python main.py --config config.yaml

# Run with custom output directory
python main.py --output ./outputs

# Run in verbose mode
python main.py --verbose
🌐 Deployment
Google Colab Deployment
Deploy the application quickly on Google Colab with public access:
bash# Install LocalTunnel
!npm install -g localtunnel

# Run Streamlit in the background
!streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &

# Create public tunnel
!lt --port 8501
After running these commands, you'll receive a public URL to access your application.

