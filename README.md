---

# 🌾 Pakistani Agricultural & Water Advisory System

**AI-powered decision support tailored for farmers and irrigation planners in Pakistan.**

This application leverages **Gradio** and **Groq's LLaMA-3.3-70B-Versatile** model to provide expert, dual-language (English and formal Urdu) agricultural advice. It is designed to understand local Pakistani agricultural terminology and deliver structured, actionable recommendations for crop management and water conservation.

## ✨ Features

* **🌍 Bilingual Output:** Automatically generates responses in English first, followed by formal Pakistani Urdu, without mixing the two.
* **🚜 Localized Expertise:** Tuned to understand and utilize Pakistani agricultural terminology and practices.
* **📋 Structured Recommendations:** Breaks down advice into clear, actionable sections:
* Problem Identification
* Recommended Actions
* Technical Guidance


* **⚡ Modern Gradio UI:** Built using Gradio's updated `messages` format for robust, stateful chat interactions.

## 🛠 Prerequisites

Ensure you have Python installed along with the required libraries.

Install the dependencies using pip:

```bash
pip install gradio groq

```

## 🔑 Environment Setup

**Security Note:** Never hardcode your API key into the script.

This app requires a Groq API key to function. Set it as an environment variable before running the script.

**On Linux/macOS:**

```bash
export GROQ_API_KEY="your_new_api_key_here"

```

**On Windows (Command Prompt):**

```cmd
set GROQ_API_KEY=your_new_api_key_here

```

**On Windows (PowerShell):**

```powershell
$env:GROQ_API_KEY="your_new_api_key_here"

```

*(Make sure to update your `app.py` script to use `os.getenv("GROQ_API_KEY")` when initializing the Groq client!)*

## 🚀 How to Run

Once your dependencies are installed and your API key is secured, run the application:

```bash
python app.py

```

*(Replace `app.py` with the actual name of your Python file).*

A local web server will launch (typically at `http://127.0.0.1:7860`). Open this URL in your browser to start querying the Agricultural Advisory System.

## 🧠 Under the Hood

* **UI Framework:** Gradio (`gr.Blocks`, `gr.Chatbot`)
* **LLM Provider:** Groq
* **Model Used:** `llama-3.3-70b-versatile` (Chosen for high reasoning capabilities required for bilingual, structured logic)
* **Generation Parameters:** Temperature is set to `0.5` to ensure advice remains factual, grounded, and technically accurate without hallucinating statistics.
