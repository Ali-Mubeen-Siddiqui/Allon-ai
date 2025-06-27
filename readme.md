Ran tool
Ran tool
Ran tool
Read file: ai/requirements.txt
Read file: ai/allon.py
Read file: ai/core.py
Read file: ai/voice_engine.py
Read file: ai/listener.py
Read file: ai/functions.py
Read file: ai/training_data/main.txt
Read file: ai/readme.md
Read file: ai/memory_data/memory.py
Read file: ai/main.py
Read file: ai/requirements.txt
Read file: ai/.gitignore
Read file: ai/notes/
Ran tool
Read file: notes/$_ud.txt
Here is a high-fidelity, comprehensive `README.md` draft for **Allon AI**. This README covers all features, setup, usage, and personalization tips, and highlights the use of `requirements.txt` for dependency management.

---

# Allon AI

**Allon AI** is a next-generation, voice-enabled, context-aware AI assistant designed to be your fast, friendly, and intelligent companion. Allon can remember, reason, execute system functions, and interact naturally—making it more than just a chatbot. It’s your personal AI friend, tutor, and productivity partner.

---

## 🚀 Features

### 🗣️ Voice Interaction
- **Talk to Allon**: Uses speech recognition for input and text-to-speech for responses.
- **Natural, friendly, and concise replies**: Allon is designed to sound like a real companion, not a robot.

### 🧠 Memory System
- **Short-term memory**: Remembers recent conversations for context.
- **Long-term memory**: Stores important information and user preferences across sessions.
- **Automatic memory management**: Short-term memory refreshes periodically for privacy and performance.

### 🛠️ Function Calling & Automation
- **Dynamic function execution**: Allon can open websites, write files, get the current time, execute system commands, and more.
- **Extensible**: Add your own functions easily in `functions.py` and the `tools/` directory.

### 🏷️ Tag-based Control
- Uses special tags in responses to:
  - Indicate if a function should be executed (`<function>true</function>`)
  - Specify if information should be stored in long-term memory (`<long>true</long>`)
  - Provide function call details in JSON (`<execute>{...}</execute>`)

### 🧩 Personalization
- Allon adapts to your style, remembers your preferences, and can be customized with your own training data and personality traits.

### 📚 Example Skills
- Programming help (Python, Java, etc.)
- Math, science, and logic
- Creative writing and storytelling
- Technical support and debugging
- Language translation
- Educational help
- Research and data analysis

---

## ⚡ Quick Start

### 1. **Clone the Repository**
```bash
git clone <your-repo-url>
cd AllonAi/ai
```

### 2. **Install Dependencies**
> **Important:** Use the provided `requirements.txt` to ensure all dependencies are installed.
```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment Variables**
- Create a `.env` file in the `ai/` directory.
- Add your OpenRouter/OpenAI API key:
  ```
  API_KEY=your_openrouter_api_key_here
  ```

### 4. **Personalize Allon (Recommended)**
- Edit `training_data/main.txt` to add your name, preferences, and any special instructions for Allon.
- The more you tell Allon about yourself, the better and more personal the responses!

### 5. **Run Allon**
```bash
python main.py
```
- Allon will greet you and start listening for your voice commands.

---

## 🧑‍💻 How It Works

- **Main Entry Point:** `main.py` launches Allon.
- **Core Logic:** `allon.py` and `core.py` manage the AI, memory, and function execution.
- **Voice Engine:** `voice_engine.py` handles text-to-speech.
- **Listener Engine:** `listener.py` handles speech-to-text.
- **Memory:** `memory_data/memory.py` manages short and long-term memory.
- **Functions:** `functions.py` and `tools/` provide Allon's abilities (open sites, write files, etc.).

---

## 🛡️ Tags & Functionality

Allon uses special tags in its responses to control behavior:

- `<function>true</function>`: Indicates a function should be executed.
- `<long>true</long>`: Save this information in long-term memory.
- `<execute>{...}</execute>`: JSON object specifying which functions to call and with what arguments.

**Example:**
```json
<function>true</function>
<long>false</long>
<execute>
{
  "0": {
    "function_name": "open_site",
    "arguments": {
      "site_url": "https://www.youtube.com"
    }
  }
}
</execute>
```

---

## 📝 Personalization Tips

- **Tell Allon about yourself!**  
  Edit `training_data/main.txt` and add your name, interests, and preferences.
- **Add custom functions:**  
  Extend Allon's abilities by adding new functions in `functions.py` and the `tools/` directory.
- **Set your preferred voice and rate:**  
  Edit `voice_engine.py` to change the default voice settings.

---

## 🧩 Extending Allon

- Add new skills by defining functions in `functions.py` and registering them in `funcs_table`.
- Create new tools in the `tools/` directory for advanced integrations.

---

## 🗂️ Project Structure

```
ai/
├── allon.py           # Main Allon class
├── core.py            # Core AI logic and memory
├── functions.py       # Function definitions and registry
├── listener.py        # Voice input engine
├── memory_data/       # Memory management files
├── notes/             # Example notes and essays
├── requirements.txt   # Python dependencies
├── training_data/     # Personalization and training data
├── voice_engine.py    # Voice output engine
├── main.py            # Entry point
└── .env               # Your API key (not in repo)
```

---

## 🛑 .gitignore

Sensitive and runtime files are ignored by default:
```
.env
__pycache__/
ai/memory_data/shortTerm.txt
ai/memory_data/longTerm.txt
```

---

## ❓ FAQ

**Q: Why should I personalize Allon?**  
A: The more Allon knows about you, the more helpful and personal it becomes!

**Q: What if I want to add new features?**  
A: Just add new functions in `functions.py` and register them in `funcs_table`. Allon is designed to be easily extensible.

**Q: Is my data private?**  
A: Allon stores memory locally. You control what goes into long-term memory.

---

## ❤️ Contributing

Pull requests and suggestions are welcome! Please open an issue or PR to discuss improvements or new features.

---

## 📢 Final Note

**Allon AI is your fast, friendly, and always-ready AI companion. Make it yours—personalize, extend, and enjoy!**

---

**Now, go ahead and tell Allon about yourself in `training_data/main.txt` for the best experience!**

---

Would you like this README written to your `ai/readme.md` file?