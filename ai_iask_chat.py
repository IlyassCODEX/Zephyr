import asyncio
import time
import random
from playwright.async_api import async_playwright
import pyfiglet
from colorama import init, Fore, Style


def banner():
    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + "Welcome to Enhanced AI Automation CLI (Playwright)")
    print(Fore.YELLOW + "=" * 70)
    print(Fore.WHITE + "")


async def main():
    
    banner()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://iask.ai/", wait_until="domcontentloaded")
        await asyncio.sleep(random.uniform(2, 4))

        # Find the input field once
        input_selectors = [
            "#q-compact",
            "textarea[name='q']",
            "textarea[placeholder*='Ask']",
        ]

        print("✅ Ready! Type your question (or 'exit' to quit).")

        while True:
            question = input("\n❓ Enter your question: ")
            if question.lower() in ["exit", "quit", "q"]:
                print("👋 Exiting...")
                break

            # Re-select the textarea each time (it gets replaced after every ask)
            try:
                chat_input = None
                for selector in input_selectors:
                    try:
                        chat_input = await page.wait_for_selector(selector, timeout=5000)
                        if chat_input:
                            break
                    except:
                        continue

                if not chat_input:
                    print("❌ Could not find input field")
                    await browser.close()
                    return
        
                await chat_input.click()
                await chat_input.fill(question)
                await asyncio.sleep(random.uniform(0.5, 1.5))
                await page.keyboard.press("Enter")
            except Exception as e:
                print(f"⚠️ Could not find input field: {e}")
                continue

            # Wait for the response in the output
            try:
                time.sleep(12)
                await page.wait_for_selector("#output #text", timeout=60000)
                response = await page.inner_text("#output #text")
                print("\n=== iAsk.ai Response ===\n")
                print(response.strip())
                print("\n=========================\n")
            except Exception as e:
                print(f"⚠️ Failed to get response: {e}")

        # keep browser open after exit if needed
        print("Browser will stay open. Close it manually when done.")
        await asyncio.sleep(9999)  # keeps session alive

if __name__ == "__main__":
    asyncio.run(main())
