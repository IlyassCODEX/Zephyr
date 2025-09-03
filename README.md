<img width="874" height="289" alt="Stylized Crow and Wind Log" src="https://github.com/user-attachments/assets/c0449bf8-edd1-42d4-b560-50dfe75e4581" />

---

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)   [![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)](https://playwright.dev/python/)   [![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)   [![Status](https://img.shields.io/badge/Status-Active-success.svg)]()  

Now you can **chat with AI directly from your terminal** – no API keys, no complex requests, no need to visit websites.  
Zephyr AI Automation CLI makes it effortless: just run the tool, type your questions, and watch the AI respond in real time, right inside your CLI.  
It allows you to ask questions and stream responses in real time, with a professional CLI interface and automatic logging.  

---

## ✨ Features
- 🚀 **Playwright-powered automation** – no APIs or keys required  
- 💬 **Interactive CLI** – ask questions and get answers directly in your terminal  
- 📝 **Real-time streaming** – responses appear progressively, like a real chat  
- 📂 **Automatic logging** – all Q&A sessions saved in `codex_ai_log.txt`  
- 🎨 **Professional CLI design** – clean layout with colors and typing effect  
- ⚡ **Headless or visible browser** – switch easily depending on your needs  


📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IlyassCODEX/zephyr.git
   cd zephyr
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:

   ```bash
   playwright install
   ```

---

## ▶️ Usage

Run the script:

```bash
python zephyr.py
```

You will see a banner and a prompt:

```
======================================================================
Welcome to Codex AI Automation CLI (Playwright)
======================================================================

Type your questions below (type 'exit' to quit):

You:
```

Example session:

```
You: what is the capital of France?

Codex AI Response:
----------------------------------------------------------------------
The capital of France is Paris.
----------------------------------------------------------------------
```

Exit anytime with:

```
exit
```

---

## ⚙️ Configuration

* **Headless mode** (default: `True`):
  To see the browser window, set in `zephyr.py`:

  ```python
  bot = ZCHATAI(headless=False)
  ```

* **Logs**:
  All conversations are saved automatically in `codex_ai_log.txt`.

---

## 📂 Project Structure

```
zephyr/
│
├── zephyr.py   # Main CLI script
├── requirements.txt      # Dependencies
└── codex_ai_log.txt      # Generated log file (runtime)
```

---

## 🛠 Requirements

* Python **3.8+**
* [Playwright](https://playwright.dev/python/)
* [Colorama](https://pypi.org/project/colorama/)
* [Pyfiglet](https://pypi.org/project/pyfiglet/)

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---

## 🙌 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📌 Disclaimer

This project is for **educational and research purposes only**.
