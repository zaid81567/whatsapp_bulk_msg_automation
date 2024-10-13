Here's a sample `README.md` for your GitHub repository:

---

# WhatsApp Web Automation with Selenium

This project automates the process of sending messages (with attachments) to a list of WhatsApp contacts using **Selenium WebDriver**. It automates opening a chat, sending a pre-defined message, and attaching an image for each contact in the list.

## Features

- Send messages to multiple phone numbers via WhatsApp Web.
- Attach an image along with the message.
- Automatically handles non-existent WhatsApp numbers.
- Logs skipped numbers for later review.
- Execution time logging for performance tracking.

## Requirements

- Python 3.x
- Google Chrome browser
- [Selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/) for ChromeDriver
- [pyperclip](https://pypi.org/project/pyperclip/) for clipboard operations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/whatsapp-automation.git
   cd whatsapp-automation
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have **Google Chrome** installed.

4. The script uses **ChromeDriver**, which will be managed automatically by `webdriver-manager`.

## Setup

1. **Create External Files:**
   - Place the following files in the `other/` directory:
     - `numbers.txt`: List of phone numbers (one per line) with country code (e.g., `919876543210` for India).
     - `message.txt`: The message you want to send.
     - `img_path.txt`: Path to the image you want to send as an attachment.
   
   Example structure:
   ```
   other/
   ├── numbers.txt
   ├── message.txt
   └── img_path.txt
   ```

2. **File Format:**
   - `numbers.txt`: Each phone number should be on a new line.
   - `message.txt`: Write your message in this file.
   - `img_path.txt`: Full file path to the image you want to send.

## Usage

1. Open WhatsApp Web in a browser and log in.
   
2. Run the script:
   ```bash
   python main.py
   ```

3. The script will wait for you to log in to WhatsApp Web (30 seconds by default). After that, it will start sending messages and images to the phone numbers listed in `numbers.txt`.

4. The script will skip any numbers that are not registered on WhatsApp and log them in `skipped_nums.txt`.

## Code Overview

- **wait_for_element**: A helper function for explicit waits on elements.
- **saveSkippedNumber**: Saves skipped numbers to `skipped_nums.txt` for review.
- **Main Process**: 
  - Reads phone numbers, message, and image path.
  - Opens WhatsApp Web.
  - Sends the message and image to each contact.
  - Logs execution time and skipped numbers.

## Known Issues

- Using `time.sleep()` might slow down the script; replace it with more precise waits if necessary.
- Excessive use of this script may violate WhatsApp's terms of service. Use responsibly.

## Disclaimer

This project is for educational purposes only. The use of automation on WhatsApp may violate their [Terms of Service](https://www.whatsapp.com/legal/). Use at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adapt it further based on your specific requirements.