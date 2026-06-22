✅ Step 1: Sahi README.md (Copy-Paste Ready)
Bas is poore box ko copy karke apni README.md mein paste kar de. Isme saare headings, code blocks, tables bilkul set hain.

markdown
# 📦 telegram-terabox-bot

A Telegram bot that connects directly to your **TeraBox cloud account** to upload, list, download, delete and manage files automatically — all from inside Telegram!

> ⚙️ Built with Python · Uses reverse‑engineered TeraBox APIs · Works 24/7 on **Render.com**

---

## ✨ Features

- 🔐 **Login** to TeraBox using your email and password (no API token required)
- 📤 **Upload** any file (photo, video, document) directly from Telegram to your TeraBox
- 📂 **List** all files in your root folder with file IDs and sizes
- 📥 **Download** any file from TeraBox to Telegram using its file ID
- 📁 **Create** new folders in your TeraBox
- 🗑️ **Delete** unwanted files
- 🔄 **Automatic session** handling – no need to log in again
- ☁️ **Deploy for free** on Render.com with a single click

---

## 🧾 Prerequisites

Before you start, make sure you have:

1. A **TeraBox account** (free or premium) with email and password – **no 2‑Factor Authentication** enabled.
2. A **Telegram Bot Token** – obtain one from [@BotFather](https://t.me/botfather) on Telegram.
3. (Optional) A **GitHub account** to host your code for deployment.

---

## 🛠️ Setup Locally (for testing)

### 1. Clone or create the project folder
```bash
mkdir telegram-terabox-bot
cd telegram-terabox-bot
2. Create the required files
You need the following files in the root directory:

bot.py – main bot logic

terabox_api.py – TeraBox API client

requirements.txt – Python dependencies

Procfile – for Render deployment

(All code is provided in the repository – just copy and paste.)

3. Set up a Python virtual environment (recommended)
bash
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
4. Install dependencies
bash
pip install -r requirements.txt
5. Set environment variables
Create a .env file in the project root and fill in your credentials:

env
BOT_TOKEN=your_telegram_bot_token
TERABOX_EMAIL=your_terabox_email
TERABOX_PASSWORD=your_terabox_password
Alternatively, export them in your terminal:

bash
export BOT_TOKEN="your_token"
export TERABOX_EMAIL="your_email"
export TERABOX_PASSWORD="your_password"
6. Run the bot
bash
python bot.py
You should see ✅ Bot is running! in the console. Now open Telegram, find your bot, and send /start.

🌐 Deploy on Render.com (Free & Easy)
Render allows you to host your bot 24/7 for free. Follow these steps:

1. Push your code to GitHub
Create a public or private repository on GitHub and push all your files (except .env).

2. Log in to Render
Go to render.com and sign in with your GitHub account.

3. Create a new Web Service
Click the New + button and select Web Service.

Connect your GitHub repository.

4. Configure the service
Fill in the following details:

Field	Value
Name	Choose any (e.g., terabox-bot)
Environment	Python 3
Build Command	pip install -r requirements.txt
Start Command	python bot.py
Plan	Free (or choose any)
5. Add Environment Variables
In the same page, scroll down to Environment Variables and add these three:

Key	Value
BOT_TOKEN	Your Telegram bot token
TERABOX_EMAIL	Your TeraBox email
TERABOX_PASSWORD	Your TeraBox password
6. Deploy
Click Create Web Service. Render will automatically build and deploy your bot.

Once the build finishes (you’ll see a green checkmark), your bot is live and will respond to commands on Telegram.

🔔 Note: On the free plan, Render will spin down the service after 15 minutes of inactivity, but it wakes up automatically when a new message arrives. Your bot will never miss a message!

🤖 Bot Commands
After deployment, send these commands to your bot in Telegram:

Command	Description
/start	Show welcome message with available commands
/help	Detailed usage instructions
/list	List all files (up to 50) in your root directory with IDs and sizes
/upload	(Optional) Reply to a file with /upload to upload (but you can just send the file directly)
/download <file_id>	Download a file using its ID (get it from /list)
/mkdir <folder_name>	Create a new folder in your root directory
/delete <file_id>	Delete the file with the given ID
💡 Easiest way to upload
Just send any file (photo, video, document) – the bot will automatically upload it to your TeraBox root folder. No command needed!

🔑 How to Get a Telegram Bot Token
Open Telegram and search for @BotFather.

Send /newbot and follow the instructions:

Choose a display name for your bot.

Choose a username ending with bot (e.g., MyTeraBoxBot).

Once created, BotFather will give you a token like 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz.

Copy that token – you’ll use it as the BOT_TOKEN environment variable.

🔧 Environment Variables Summary
Variable	Description	Required?
BOT_TOKEN	Your Telegram bot token from BotFather	Yes
TERABOX_EMAIL	Email address used for TeraBox login	Yes
TERABOX_PASSWORD	Password for your TeraBox account	Yes
Never share these values – always keep them as environment variables, never hard‑coded in your code.

🐛 Troubleshooting
Problem	Possible Solution
Login failed	Check your email/password. Disable 2FA on your TeraBox account.
List files fails	The API might have changed – restart the bot. Ensure your internet connection is stable.
Upload fails	File size > Telegram limit (2GB). Also check your TeraBox free space.
Bot doesn't respond	Verify the service is running on Render. Check the logs for any error messages.
jsToken missing	The bot auto‑refreshes it. If it persists, restart the bot.
📁 File Structure
text
telegram-terabox-bot/
├── bot.py                # Main Telegram bot logic
├── terabox_api.py        # TeraBox API client (login, upload, list, download, delete, mkdir)
├── requirements.txt      # Python dependencies
├── Procfile              # Render start command (worker: python bot.py)
└── README.md             # This file
⚠️ Important Notes
This bot uses unofficial, reverse‑engineered TeraBox APIs. TeraBox may change their endpoints at any time, which could temporarily break the bot. We will try to keep the code updated.

2‑Factor Authentication (2FA) is not supported. Please disable it on your TeraBox account if enabled.

Rate limits: Avoid sending too many requests per minute, or your account/IP may be temporarily blocked.

Large files: Uploading files over 100 MB may take longer and could time out on slow connections.

🤝 Contributing
Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.

📄 License
This project is open‑source and available under the MIT License.

🙏 Acknowledgements
Built with ❤️ using:

python-telegram-bot

Requests

Enjoy seamless TeraBox management from your Telegram! 🚀

text

---

## ✅ Step 2: Poori Project ZIP Banane Ka Tarika (Manual)

Main tujhe **har file ka content** de raha hoon. Tu in sabko **ek folder mein** save kar, aur fir **ZIP** bana le.

### 📁 Folder Structure:
telegram-terabox-bot/
├── bot.py
├── terabox_api.py
├── requirements.txt
├── Procfile
└── README.md

text

---

### 1. `bot.py`
```python
import logging
import os
import asyncio
from typing import Optional

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

from terabox_api import TeraBoxClient

# ============= CONFIGURATION =============
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TERABOX_EMAIL = os.getenv("TERABOX_EMAIL")
TERABOX_PASSWORD = os.getenv("TERABOX_PASSWORD")

if not all([BOT_TOKEN, TERABOX_EMAIL, TERABOX_PASSWORD]):
    logger.error("Missing environment variables! Please set BOT_TOKEN, TERABOX_EMAIL, TERABOX_PASSWORD")
    exit(1)

# Initialize TeraBox Client
try:
    terabox = TeraBoxClient(TERABOX_EMAIL, TERABOX_PASSWORD)
    logger.info("✅ TeraBox client initialized successfully")
except Exception as e:
    logger.error(f"❌ Failed to initialize TeraBox client: {e}")
    exit(1)

# ============= BOT HANDLERS =============

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message with available commands"""
    welcome_text = """
🚀 **Welcome to TeraBox Bot!**

I can help you manage your TeraBox files directly from Telegram.

**Available Commands:**
/start - Show this message
/list - List files in your TeraBox
/upload - Upload a file (reply to a file with /upload)
/download - Download a file (use /download <file_id>)
/mkdir - Create a new folder (use /mkdir <folder_name>)
/delete - Delete a file (use /delete <file_id>)
/help - Show detailed help

**How to use:**
• Send any file to upload it to TeraBox
• Use /list to see your files
• Use /download <file_id> to download a file
"""
    await update.message.reply_text(welcome_text, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show detailed help"""
    help_text = """
📖 **Detailed Help**

**Upload Files:**
Just send any file (photo, video, document) and it will be automatically uploaded to TeraBox.

**List Files:**
Use /list to see all files in your root directory.

**Download Files:**
Use /download <file_id> - You can get file_id from /list command.

**Create Folder:**
Use /mkdir <folder_name> to create a new folder.

**Delete File:**
Use /delete <file_id> to delete a file.

**File IDs:**
When you use /list, you'll see each file with its ID in parentheses.
Example: `myfile.jpg (ID: 123456789)`
"""
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def list_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List files from TeraBox"""
    try:
        await update.message.reply_text("📂 Fetching your files...")
        
        files = terabox.list_files(limit=50)
        
        if not files:
            await update.message.reply_text("📭 No files found in your TeraBox.")
            return
        
        # Format the response
        reply = "📁 **Your Files:**\n\n"
        for item in files:
            icon = "📁" if item.get("isdir") == 1 else "📄"
            name = item.get("name", "Unknown")
            file_id = item.get("fs_id", "N/A")
            size = item.get("size", 0)
            
            # Format size
            if size > 1024 * 1024 * 1024:
                size_str = f"{size / (1024*1024*1024):.2f} GB"
            elif size > 1024 * 1024:
                size_str = f"{size / (1024*1024):.2f} MB"
            elif size > 1024:
                size_str = f"{size / 1024:.2f} KB"
            else:
                size_str = f"{size} B"
            
            reply += f"{icon} `{name}`\n"
            reply += f"   📎 ID: `{file_id}` | 📦 Size: {size_str}\n\n"
        
        # Split long messages
        if len(reply) > 4000:
            parts = [reply[i:i+4000] for i in range(0, len(reply), 4000)]
            for part in parts:
                await update.message.reply_text(part, parse_mode="Markdown")
        else:
            await update.message.reply_text(reply, parse_mode="Markdown")
            
    except Exception as e:
        logger.error(f"List error: {e}")
        await update.message.reply_text(f"❌ Error: {str(e)}")


async def download_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Download a file from TeraBox"""
    try:
        if not context.args:
            await update.message.reply_text(
                "❌ Please provide a file ID.\n"
                "Usage: `/download <file_id>`\n"
                "Get file IDs from /list command.",
                parse_mode="Markdown"
            )
            return
        
        file_id = context.args[0]
        await update.message.reply_text(f"⬇️ Downloading file (ID: {file_id})...")
        
        file_content = terabox.download_file(file_id)
        
        # Try to get filename from list
        files = terabox.list_files(limit=100)
        filename = "downloaded_file"
        for f in files:
            if str(f.get("fs_id")) == str(file_id):
                filename = f.get("name", "downloaded_file")
                break
        
        await update.message.reply_document(
            document=file_content,
            filename=filename,
            caption=f"✅ Downloaded from TeraBox\nFile ID: {file_id}"
        )
        
    except Exception as e:
        logger.error(f"Download error: {e}")
        await update.message.reply_text(f"❌ Download failed: {str(e)}
