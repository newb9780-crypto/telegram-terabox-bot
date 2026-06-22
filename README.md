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

3. Set up a Python virtual environment (recommended)
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Set environment variables
BOT_TOKEN=your_telegram_bot_token
TERABOX_EMAIL=your_terabox_email
TERABOX_PASSWORD=your_terabox_password

export BOT_TOKEN="your_token"
export TERABOX_EMAIL="your_email"
export TERABOX_PASSWORD="your_password"

python bot.py
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
