# Mistral 7B Web Chatbot

This is a simple Flask-based chatbot using the open-source Mistral 7B Instruct model.

## Setup

1. Clone or unzip the project folder.
2. Install dependencies:

   ```bash
   pip install flask transformers accelerate torch
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

## Notes
- This loads the Mistral 7B model (`mistralai/Mistral-7B-Instruct-v0.2`) from Hugging Face.
- You need a GPU with ~16GB+ VRAM for smooth performance, or it will fallback to CPU (much slower).
- The web interface is very basic HTML + JavaScript.

Enjoy chatting with your self-hosted Mistral 7B chatbot!
