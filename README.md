<img width="874" height="289" alt="Stylized Crow and Wind Log" src="https://github.com/user-attachments/assets/c0449bf8-edd1-42d4-b560-50dfe75e4581" />

---
# ZephyrAI - Multi-Model CLI AI Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A powerful, professional-grade command-line interface for interacting with multiple AI models simultaneously. ZephyrAI automates browser-based AI interactions using Playwright, providing a unified interface for DeepAI, Zhipu AI, and iAsk AI.

## 🚀 Features

- **Multi-Model Support**: Simultaneous access to multiple AI providers
- **Browser Automation**: Headless automation using Playwright
- **Real-time Streaming**: Live response streaming with typing effects
- **Comparison Mode**: Compare responses from different AI models side-by-side
- **Session Logging**: Automatic logging of all interactions with searchable history
- **Clipboard Integration**: Automatic copying of AI responses to clipboard
- **File Input Support**: Process questions from text files
- **Professional CLI**: Color-coded output with banner art and progress indicators

## 📋 Supported AI Models

| Model | Provider | Access | Features |
|-------|----------|---------|----------|
| **DeepAI** | DeepAI.org | Free | High-quality responses, streaming |
| **ZChat** | Zhipu AI | Free | Chinese-optimized, fast responses |
| **iAsk** | iAsk.ai | Free | Research-focused, detailed answers |

## 🛠 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Chromium browser (automatically installed by Playwright)

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/zephyrai.git
cd zephyrai

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Manual Installation

```bash
pip install playwright pyfiglet colorama pyperclip
playwright install chromium
```

## 📖 Usage

### Basic Usage

**Method 1: Interactive Mode**
```bash
# Interactive mode - choose model from menu
python3 main.py
```

**Method 2: Pipe Input (Non-Interactive)**
```bash
# Pipe question directly to specific model
echo "Your question here" | python3 main.py --deep
echo "What is machine learning?" | python3 main.py --zchat
echo "Explain quantum physics" | python3 main.py --iask
```

### Direct Model Access

```bash
# Direct model access with interactive input
python3 main.py --deep          # Use DeepAI model
python3 main.py --zchat         # Use Zhipu AI model  
python3 main.py --iask          # Use iAsk AI model
```

### Advanced Features

```bash
# Compare responses from all models
python3 main.py --compare "Your question here"

# Pipe to comparison mode
echo "Your question" | python3 main.py --compare

# Use question from file
python3 main.py --deep -f question.txt

# Pipe file content to model
cat question.txt | python3 main.py --zchat

# Search conversation history
python3 main.py --history "search keyword"
```

### Usage Examples

```bash
# Interactive session
python3 main.py
# Then choose model and enter questions interactively

# One-shot question with DeepAI
echo "Explain blockchain technology" | python3 main.py --deep

# Batch processing from file
cat questions.txt | python3 main.py --iask

# Compare all models on same question
echo "What are the benefits of AI?" | python3 main.py --compare
```

### Command Line Arguments

| Argument | Description |
|----------|-------------|
| `--deep` | Use DeepAI model |
| `--zchat` | Use Zhipu AI model |
| `--iask` | Use iAsk AI model |
| `--compare QUESTION` | Compare all models with the same question |
| `-f, --file PATH` | Read question from file |
| `--history KEYWORD` | Search past conversation logs |
| `--help` | Show help message |

## 🎯 Usage Patterns

### Interactive Session
```bash
python3 main.py
```
*Prompts for model selection and enters interactive Q&A mode*

### One-Time Query
```bash
echo "Your question" | python3 main.py --deep
```
*Ideal for scripting and automation*

### Model Comparison
```bash
echo "Compare AI models" | python3 main.py --compare
```
*Gets perspectives from all available AI models*

### File Processing
```bash
cat long_question.txt | python3 main.py --zchat
```
*Process lengthy questions from files*

## 🔧 Technical Details

### Architecture

```
ZephyrAI/
├── main.py              # Main CLI interface
├── ai_deep_chat.py      # DeepAI automation module
├── ai_z_chat.py         # Zhipu AI automation module  
├── ai_iask_chat.py      # iAsk AI automation module
└── ~/.zephyrai/logs/    # Conversation logs
```

### Key Components

- **Playwright Integration**: Robust browser automation with error handling
- **Response Streaming**: Real-time output with stability detection
- **Session Management**: Persistent browser sessions with smart element selection
- **Logging System**: Structured logging with timestamped files
- **Error Recovery**: Automatic retry mechanisms for failed interactions
- **Pipe Support**: Seamless stdin/stdout integration for Unix-style workflows

## 📊 Example Output

### Interactive Mode
```
======================================
Welcome to ZephyrAI – Multi-Model CLI Assistant
======================================

❓ Enter your question: Explain neural networks

⏳ Waiting for AI response...

=== DeepAI Response ===

Neural networks are computing systems inspired by the human brain...
They consist of interconnected nodes (neurons) organized in layers...

======================================
```

### Pipe Mode
```bash
echo "What is Python?" | python3 main.py --deep
```
```
======================================
Welcome to ZephyrAI – Multi-Model CLI Assistant
======================================

⏳ Waiting for AI response...

=== DeepAI Response ===

Python is a high-level programming language known for its simplicity...
======================================
```

## 🔒 Privacy & Security

- All conversations are stored locally in `~/.zephyrai/logs/`
- No data is transmitted to external servers except the AI providers
- Browser sessions are isolated and cleaned up properly
- Automatic clipboard clearing is recommended after sensitive operations

## 🐛 Troubleshooting

### Common Issues

**Browser not launching:**
```bash
# Reinstall Playwright browsers
playwright install chromium
```

**Module not found errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**Timeout errors:**
- Check internet connection
- Retry with longer timeouts in script configurations

**Pipe input not working:**
```bash
# Ensure proper quoting for complex questions
echo "What is AI?" | python3 main.py --deep
# Instead of:
echo What is AI? | python3 main.py --deep
```

### Debug Mode

Enable headful mode for debugging by modifying `headless=False` in the respective script files.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Playwright team for excellent browser automation tools
- PyFiglet for ASCII banner generation
- Colorama for cross-platform colored terminal text
- All AI providers for their free access tiers

## 📞 Support

For support and questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review existing issues for similar problems

---

**Disclaimer**: This tool is for educational and research purposes. Users are responsible for complying with the terms of service of each AI provider and applicable laws.
