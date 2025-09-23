#!/usr/bin/env python3
"""
Zephyr AI Automation Tool (Playwright version)
"""

import time
import sys
import asyncio
from colorama import init, Fore, Style
import pyfiglet
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

init(autoreset=True)


class ZCHATAI:
    def __init__(self, headless=True):
        self.browser = None
        self.page = None
        self.headless = headless
        self.first_question = True   # ✅ Track if it's the first Q
        self.seen_ids = set()

    async def setup_driver(self):
        """Set up Playwright browser and open chat site once"""
        pw = await async_playwright().start()
        self.browser = await pw.chromium.launch(headless=self.headless)
        self.page = await self.browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        ))

        # Open chat site only once
        await self.page.goto("https://chat.z.ai/")
        await self.page.wait_for_timeout(5000)

        # Try to click auto-think once
        try:
            auto_think_button = await self.page.wait_for_selector(
                "//button[@data-autothink='true']", timeout=10000
            )
            await auto_think_button.click()
            await self.page.wait_for_timeout(2000)
        except PlaywrightTimeout:
            pass  # button not found, continue

    async def stream_response(self, question, timeout=120, check_interval=0.5):
        """Stream Codex AI response while it's generated"""
        start_time = time.time()
        printed_text = ""
    
        try:
            while time.time() - start_time < timeout:
                if self.first_question:
                    # ---------- FIRST QUESTION MODE ----------
                    ai_responses = await self.page.query_selector_all(
                        "//div[starts-with(@id,'message-') and not(contains(@class,'user-message'))]"
                    )
                    if ai_responses:
                        last = ai_responses[-1]
                        text_node = await last.query_selector(".chat-assistant")
                        latest_response = (await text_node.inner_text()).strip() if text_node else ""

                        if latest_response.startswith(question):
                            latest_response = latest_response[len(question):].strip()

                        if len(latest_response) > len(printed_text):
                            new_text = latest_response[len(printed_text):]
                            sys.stdout.write(new_text)
                            sys.stdout.flush()
                            printed_text = latest_response

                    # stop once loading dots gone
                    loading = await self.page.query_selector_all(
                        "//div[contains(@class, 'loading-container')]"
                    )
                    if not loading:
                        print()
                        self.first_question = False
                        return printed_text

                else:
                    # ---------- NEXT QUESTIONS MODE ----------
                    message_divs = await self.page.query_selector_all(
                        "//div[starts-with(@id,'message-') and not(contains(@class,'user-message'))]"
                    )

                    if message_divs:
                        latest_div = message_divs[-1]
                        latest_id = await latest_div.get_attribute("id")

                        # Always read text even if ID already seen (it may be updated)
                        text_node = await latest_div.query_selector(".chat-assistant")
                        latest_response = (await text_node.inner_text()).strip() if text_node else ""

                        if latest_response.startswith(question):
                            latest_response = latest_response[len(question):].strip()

                        if len(latest_response) > len(printed_text):
                            new_text = latest_response[len(printed_text):]
                            sys.stdout.write(new_text)
                            sys.stdout.flush()
                            printed_text = latest_response

                        # Mark as seen only when finished
                        loading = await self.page.query_selector_all(
                            "//div[contains(@class, 'loading-container')]"
                        )
                        if not loading:
                            print()
                            self.seen_ids.add(latest_id)
                            return printed_text


                await asyncio.sleep(check_interval)

            print("\n⚠️ Timeout while waiting for Codex AI response.")
            return printed_text

        except Exception as e:
            print(f"\n[Error streaming response: {e}]")
            return printed_text

    async def chat_with_codex(self, question):
        """Send question and return AI response without reloading site"""
        try:
            chat_input = await self.page.wait_for_selector("#chat-input", timeout=20000)
            await chat_input.fill(question)
            await chat_input.press("Enter")

            await self.page.wait_for_selector(
                "//div[contains(@class, 'message')]", timeout=30000
            )

            print(Fore.GREEN + "\n" + "=" * 60)
            print(Fore.YELLOW + "Codex AI Response:")
            print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)               
            await self.stream_response(question)
            print(Fore.GREEN + "=" * 60 + "\n")

            selectors = [
                "//div[contains(@class, 'message') and contains(@class, 'ai')]",
                "//div[contains(@class, 'response')]",
                "//div[contains(@class, 'bot')]",
                "//div[contains(@class, 'assistant')]",
                "//div[contains(@class, 'ai-message')]",
            ]

            response_text = ""
            for selector in selectors:
                elements = await self.page.query_selector_all(selector)
                for element in elements:
                    text = (await element.inner_text()).strip()
                    if text and len(text) > 20 and text != question:
                        response_text = text
                        break
                if response_text:
                    break

            return response_text or "[No response extracted]"
        except PlaywrightTimeout:
            return "[Timeout: Codex AI did not respond in time]"
        except Exception as e:
            return f"[Error: {e}]"

    async def close(self):
        """Close browser"""
        if self.browser:
            await self.browser.close()


def banner():
    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + "Welcome to Codex AI Automation CLI (Playwright)")
    print(Fore.YELLOW + "=" * 70)


def stream_print(text, delay=0.05):
    """Print text word by word like typing"""
    for word in text.split():
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        time.sleep(delay)
    print()


async def main():
    banner()

    bot = ZCHATAI(headless=True)
    await bot.setup_driver()

    print(Fore.MAGENTA + "\nType your questions below (type 'exit' to quit):\n")

    with open("codex_ai_log.txt", "a", encoding="utf-8") as log_file:
        while True:
            question = input(Fore.CYAN + "You: " + Style.RESET_ALL).strip()
            if question.lower() in ["exit", "quit"]:
                break

            response = await bot.chat_with_codex(question)

            log_file.write(f"Q: {question}\nA: {response}\n{'-'*60}\n")

    await bot.close()
    print(Fore.RED + "\n[+] Codex AI session ended. Goodbye!\n")


if __name__ == "__main__":
    asyncio.run(main())

