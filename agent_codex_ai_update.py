#!/usr/bin/env python3
"""
Codex AI Automation Tool
Enhanced professional CLI version
"""

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# CLI design imports
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)


class CodexAIAutomation:
    def __init__(self, headless=False, chromedriver_path=None):
        """Initialize the automation tool"""
        self.driver = None
        self.headless = True
        self.chromedriver_path = chromedriver_path or "/usr/bin/chromedriver"
        self.setup_driver()

    def setup_driver(self):
        """Set up Chrome WebDriver"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        )

        try:
            if self.chromedriver_path:
                service = Service(executable_path=self.chromedriver_path)
                self.driver = webdriver.Chrome(service=service, options=chrome_options)
            else:
                self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(0)
        except Exception as e:
            print(Fore.RED + f"[!] Failed to setup driver: {e}")
            sys.exit(1)

    def stream_response(self, question, timeout=120, check_interval=0.5):
        """
        Stream Codex AI response in real-time while it's being generated.
        Stops when loading dots disappear.
        """
        start_time = time.time()
        printed_text = ""

        try:
            # Loop until loading-container disappears
            while time.time() - start_time < timeout:
                # Grab the latest AI message
                ai_responses = self.driver.find_elements(
                    By.XPATH,
                    "//div[contains(@class, 'message') and contains(@class, 'ai')] "
                    "| //div[contains(@class, 'response')] "
                    "| //div[contains(@class, 'bot')]"
                )
                if ai_responses:
                    latest_response = ai_responses[-1].text.strip()

                # Print only the new part
                    if latest_response.startswith(question):
                        latest_response = latest_response[len(question):].strip()
                    if len(latest_response) > len(printed_text):
                        new_text = latest_response[len(printed_text):]
                        sys.stdout.write(new_text)
                        sys.stdout.flush()
                        printed_text = latest_response

                # Check if loading dots are gone
                loading = self.driver.find_elements(
                    By.XPATH, "//div[contains(@class, 'loading-container')]"
                )
                if not loading:
                    print()  # newline after stream
                    return printed_text

                time.sleep(check_interval)

            print("\n⚠️ Timeout while waiting for Codex AI response.")
            return printed_text

        except Exception as e:
            print(f"\n[Error streaming response: {e}]")
            return printed_text


    def chat_with_codex(self, question):
        """Send question and return AI response"""
        try:
            self.driver.get("https://chat.z.ai/")
            time.sleep(5)

            auto_think_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-autothink='true']"))
            )
            auto_think_button.click()
            time.sleep(2)

            chat_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "chat-input"))
            )

            chat_input.clear()
            chat_input.send_keys(question)
            chat_input.send_keys(Keys.ENTER)

            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message')]"))
            )

            self.stream_response(question)

            selectors = [
                "//div[contains(@class, 'message') and contains(@class, 'ai')]",
                "//div[contains(@class, 'response')]",
                "//div[contains(@class, 'bot')]",
                "//div[contains(@class, 'assistant')]",
                "//div[contains(@class, 'ai-message')]",
            ]

            response_text = ""
            for selector in selectors:
                elements = self.driver.find_elements(By.XPATH, selector)
                for element in elements:
                    text = element.text.strip()
                    if text and len(text) > 20 and text != question:
                        response_text = text
                        break
                if response_text:
                    break

            return response_text or "[No response extracted]"
        except TimeoutException:
            return "[Timeout: Codex AI did not respond in time]"
        except Exception as e:
            return f"[Error: {e}]"

    def close(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()


def banner():
    ascii_banner = pyfiglet.figlet_format("Zephyr AI")
    print(Fore.CYAN + Style.BRIGHT + ascii_banner)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + "Welcome to Codex AI Automation CLI")
    print(Fore.YELLOW + "=" * 70)


def stream_print(text, delay=0.05):
        """Print text word by word like an AI is typing"""
        for word in text.split():
            sys.stdout.write(word + " ")
            sys.stdout.flush()
            time.sleep(delay)
        print()  # newline after finish

def main():
    banner()

    chromedriver_path = input(
        Fore.YELLOW + "Enter ChromeDriver path (default /usr/bin/chromedriver): "
    ).strip() or None

    bot = CodexAIAutomation(chromedriver_path=chromedriver_path)

    print(Fore.MAGENTA + "\nType your questions below (type 'exit' to quit):\n")

    with open("codex_ai_log.txt", "a", encoding="utf-8") as log_file:
        while True:
            question = input(Fore.CYAN + "You: " + Style.RESET_ALL).strip()
            if question.lower() in ["exit", "quit"]:
                break

            response = bot.chat_with_codex(question)

            print(Fore.GREEN + "\n" + "=" * 60)
            print(Fore.YELLOW + "Codex AI Response:")
            print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)
            stream_print(response, delay=0.07)  # tweak delay to make it slower/faster
            print(Fore.GREEN + "=" * 60 + "\n")

            log_file.write(f"Q: {question}\nA: {response}\n{'-'*60}\n")

    bot.close()
    print(Fore.RED + "\n[+] Codex AI session ended. Goodbye!\n")


if __name__ == "__main__":
    main()

