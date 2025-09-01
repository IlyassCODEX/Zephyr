<img width="874" height="289" alt="Stylized Crow and Wind Log" src="https://github.com/user-attachments/assets/c0449bf8-edd1-42d4-b560-50dfe75e4581" />

A powerful AI in a CLI automation tool that interacts with Codex AI through the Z.ai chat interface, providing real-time response streaming and professional-grade automation capabilities.

Example of usage :
<img width="960" height="476" alt="ASAS" src="https://github.com/user-attachments/assets/49e27c2f-a394-49c2-8667-09bccf0b3d0c" />


Features

    🤖 Automated AI Interactions: Seamlessly communicate with Codex AI

    ⚡ Real-time Response Streaming: Watch responses generate in real-time

    🎨 Professional CLI Interface: Beautiful terminal interface with colors and animations

    📝 Session Logging: Automatically save all conversations to a log file

    🔧 Configurable Settings: Customize ChromeDriver path and streaming speed

    🕶️ Headless Mode: Run automation in the background without GUI

Installation

    Python 3.7+

    Chrome browser installed

    ChromeDriver (compatible with your Chrome version)

Step-by-Step Installation

    Clone the repository
    bash
    git clone https://github.com/IlyassCODEX/Zephyr.git
    cd Zephyr

Install required dependencies

    pip install -r requirements.txt

    Install ChromeDriver

        Download from: https://chromedriver.chromium.org/

        Place in /usr/bin/chromedriver or specify path during execution


Usage
Basic Usage

    Run the tool:
    bash

    python agent_codex_ai_update.py

    Enter ChromeDriver path when prompted (or press Enter for default)

    Start chatting with Codex AI by typing your questions

    Type 'exit' or 'quit' to end the session

Advanced Configuration

Modify these variables in the code for customization:

    headless: Set to True for headless operation

    timeout: Adjust response timeout (default: 120 seconds)

    check_interval: Change streaming check interval (default: 0.5 seconds)

    stream_delay: Modify typing animation speed (default: 0.07 seconds)

Troubleshooting
Common Issues

    ChromeDriver not found

        Ensure ChromeDriver is installed and path is correct

        Download compatible version from https://chromedriver.chromium.org/

    Browser detection

        The tool uses a standard user agent, but websites may still detect automation

        Consider adding more stealth options if needed

    Element not found errors

        The website structure may have changed

        Check and update XPATH selectors if necessary

Debug Mode

To enable debugging, add these options to the Chrome setup:
python

chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

License

This project is licensed under the MIT License - see the LICENSE file for details.
Disclaimer

This tool is for educational and research purposes only. Ensure you comply with the terms of service of any websites you interact with using this automation tool.
Support

If you encounter any issues or have questions:

    Check the troubleshooting section above

    Open an issue on GitHub

    Provide detailed information about your environment and the error

Note: This tool may require maintenance as website structures change over time. Regularly check for updates to ensure compatibility.
