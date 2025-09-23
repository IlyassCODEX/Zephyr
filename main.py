#!/usr/bin/env python3
import argparse
import pyfiglet
import asyncio
import os
import subprocess
import sys
import shutil
import datetime
import pyperclip

from colorama import Fore, Style, init
init(autoreset=True)

LOG_DIR = os.path.expanduser("~/.zephyrai/logs")
os.makedirs(LOG_DIR, exist_ok=True)

SCRIPTS = {
    "deep": "ai_deep_chat.py",
    "zchat": "ai_z_chat.py",
    "iask": "ai_iask_chat.py",
}

def banner():
    ascii_banner = pyfiglet.figlet_format("Zephyr AI")
    print(Fore.CYAN + Style.BRIGHT + ascii_banner)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + " Welcome to ZephyrAI – Multi-Model CLI Assistant")
    print(Fore.YELLOW + "=" * 70)

def log_response(model, question, answer):
    """Save Q&A to a timestamped log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{timestamp}.log")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{model.upper()}] Q: {question}\nA: {answer}\n{'-'*60}\n")

def run_script(script, input_text=None):
    """Run a script as subprocess with optional stdin piping."""
    try:
        if input_text:
            result = subprocess.run(
                [sys.executable, script],
                input=input_text.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            output = result.stdout.decode("utf-8", errors="ignore")
            return output
        else:
            subprocess.run([sys.executable, script])
            return None
    except Exception as e:
        return f"⚠️ Error running {script}: {e}"

def choose_model():
    """Interactive selector when no flag is passed."""
    print(Fore.CYAN + "\nChoose an AI model:")
    for i, (key, script) in enumerate(SCRIPTS.items(), 1):
        print(f" {i}) {key} → {script}")
    choice = input(Fore.YELLOW + "\nEnter number: ").strip()
    try:
        idx = int(choice) - 1
        return list(SCRIPTS.keys())[idx]
    except:
        print(Fore.RED + "❌ Invalid choice")
        sys.exit(1)

def compare_models(question):
    """Run the same question on all models and show results side by side."""
    print(Fore.MAGENTA + "\n🔎 Comparing responses across all models...\n")
    for key, script in SCRIPTS.items():
        print(Fore.GREEN + f"\n=== {key.upper()} ===\n")
        output = run_script(os.path.join(os.path.dirname(__file__), script), input_text=question)
        if output:
            print(output.strip())
            pyperclip.copy(output.strip())  # copy last response to clipboard
            log_response(key, question, output.strip())
        print(Fore.YELLOW + "\n" + "="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="ZephyrAI – Unified AI CLI Assistant"
    )
    parser.add_argument("--deep", action="store_true", help="Run DeepAI model")
    parser.add_argument("--zchat", action="store_true", help="Run Zhipu AI model")
    parser.add_argument("--iask", action="store_true", help="Run iAsk AI model")
    parser.add_argument("--compare", metavar="QUESTION", help="Ask all models the same question")
    parser.add_argument("-f", "--file", metavar="PATH", help="Use file input as question")
    parser.add_argument("--history", metavar="KEYWORD", help="Search past logs")

    args = parser.parse_args()
    banner()

    base_dir = os.path.dirname(os.path.abspath(__file__))

    # --- History Search ---
    if args.history:
        print(Fore.MAGENTA + f"\n📜 Searching logs for '{args.history}'...\n")
        for log_file in os.listdir(LOG_DIR):
            path = os.path.join(LOG_DIR, log_file)
            with open(path, encoding="utf-8") as f:
                content = f.read()
                if args.history.lower() in content.lower():
                    print(Fore.GREEN + f"\n--- {log_file} ---\n")
                    print(content)
        return

    # --- Compare Mode ---
    if args.compare:
        compare_models(args.compare)
        return

    # --- File Input ---
    input_text = None
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            input_text = f.read()

    # --- Model Selection ---
    model = None
    for key in SCRIPTS:
        if getattr(args, key):
            model = key
            break

    if not model:
        model = choose_model()

    script_path = os.path.join(base_dir, SCRIPTS[model])
    output = run_script(script_path, input_text=input_text)

    if output:
        print(Fore.GREEN + "\n=== AI Response ===\n")
        print(output.strip())
        pyperclip.copy(output.strip())  # auto-copy
        log_response(model, input_text or "[stdin]", output.strip())

if __name__ == "__main__":
    main()
