import os
import gradio as gr
from groq import Groq

# Load API key
client = Groq(api_key="your_api_key")

SYSTEM_PROMPT = """
You are a Pakistani Agricultural and Water Management Decision Support Assistant.
Rules:
1. Respond in ENGLISH first.
2. Then respond in formal Pakistani Urdu.
3. Do NOT mix both languages in same paragraph.
4. Use Pakistani agricultural terminology.
5. Provide structured recommendations:
   - Problem
   - Recommended Actions
   - Technical Guidance
6. Do not fabricate statistics.
"""

def agricultural_advisory(message, history):

    if history is None:
        history = []


    # ✅ NEW: Gradio messages format expected
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # history now contains dicts like {"role":.., "content":..}
    for msg in history:
        # each element is a dict per online docs
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.5,
        )

        reply = response.choices[0].message.content

        # ✅ NEW: append dicts for messages format
        history.append({"role":"user","content":message})
        history.append({"role":"assistant","content":reply})

        return "", history

    except Exception as e:
        # In error case, append assistant role too
        history.append({"role":"assistant","content":f"Error: {str(e)}"})
        return "", history


with gr.Blocks(title="Pakistani Agricultural Advisory System") as demo:

    gr.Markdown("# 🌾 Pakistani Agricultural & Water Advisory System")
    gr.Markdown(
        "AI-powered decision support for farmers and irrigation planners in Pakistan."
    )

    # ✅ NEW: use messages format
    chatbot = gr.Chatbot(height=500)

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Enter your agricultural or irrigation query here...",
            scale=4,
        )
        submit_btn = gr.Button("Submit", scale=1)

    clear_btn = gr.Button("Clear Chat")

    submit_btn.click(
        agricultural_advisory,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot],
    )

    msg.submit(
        agricultural_advisory,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot],
    )


    # ✅ NEW: Clear sends empty list of messages
    clear_btn.click(lambda: ("", []), None, [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
