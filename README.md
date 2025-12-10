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
<img width="788" height="662" alt="image" src="https://github.com/user-attachments/assets/7a3c82c8-bc65-4be8-be71-730a2e5a5c1f" />


---

## ▶️ How to Run Locally

### 🔧 Installation

#### **Prerequisites**
- Python 3.8+
- pip
- Git

---

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/multi-agent-content-generator.git
cd multi-agent-content-generator
```

---

### **2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
```

**Activate the environment:**

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

---

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### **4. (Optional) Set Up Environment Variables**
```bash
cp .env.example .env
```
Edit `.env` and add API keys if required.

---

## 🚀 Usage

### **1. Run the Agent Pipeline**
```bash
python main.py
```

### **2. Launch the Streamlit UI**
```bash
streamlit run app.py
```

App will be available at:
```
http://localhost:8501
```

---

## 🌐 Deployment (Google Colab)

```bash
!npm install -g localtunnel
!streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
!lt --port 8501
```

You will get a public URL:
```
https://<random-name>.loca.lt
```

---

## 🧪 Technologies Used
- Python  
- Streamlit  
- Multi-Agent AI Architecture  
- JSON-based content generation  
- Custom templates  
- LocalTunnel  

---

## 👨‍💻 Author
**Hrishikeasan N.P**  
Applied AI Engineer • Multi-Agent Architect • NLP Developer
