# AlexonePersonalBotV1

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Private-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](README.md)

> **⚠️ Disclaimer**: This is a selfbot for personal use. Using selfbots may violate Discord's Terms of Service. Use at your own risk.

## 📋 Index

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [Troubleshooting](#troubleshooting)
- [Support](#support)

## 📖 Description

AlexonePersonalBotV1 is a custom Discord selfbot that offers a variety of features to enhance your Discord experience. The bot includes custom commands, advanced functions, and tools for personal use.

## 🔧 Prerequisites

Before starting, make sure you have:

- **Python 3.8+** installed on your system
- **Personal Discord Token** (User Token)
- **Required API Keys** (specified in the configuration file)
- Stable internet connection

## 🚀 Installation

### Step 1: Clone or download the project
```bash
git clone [repository-url]
cd AlexonePersonalBotV1
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure the bot
1. Open the `CONFIG.txt` file
2. Enter all required information following the comments in the file
3. Save the changes

## ⚙️ Configuration

The `CONFIG.txt` file contains all necessary settings:

```txt
// Your personal token if you don't know how to get it, ask me in dm.
TOKEN=

[MAINTENANCE] // Our SelfBot has OpenAI integrated for autoreply, pls put yours here. ( example. sk-xxxxxxxxxxxxxxxxxxxx )
[MAINTENANCE] // OPENAI_API_KEY=

// Your Personal Paypal Email or a link (Recommended Email to bypass antilink bots).
PAYPAL_EMAIL=

# Other configurations...
```

> **🔒 Security**: Never share your Discord token or API keys with anyone!

## 🎮 Usage

### Starting the Bot

Run one of the following commands in the terminal:

```bash
# Windows
py main.py

# Linux/Mac
python3 main.py
```

### First Start

1. Start the bot following the instructions above
2. Check the terminal for any errors
3. Once started, type `.help` in Discord to see all available commands

## 📝 Available Commands

| Command  | Description                    |
|----------|--------------------------------|
| `.help`  | Shows all available commands   |
| `.afk`   | Sets your status to afk        |
| `.info`  | Information about the bot      |

> For the complete list of commands, use `.help` after starting the bot.

## 🔧 Troubleshooting

### Common Issues

**❌ Error: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**❌ Error: Invalid Token**
- Check that the token in `CONFIG.txt` is correct
- Make sure you haven’t included extra spaces

**❌ Bot not responding**
- Check your internet connection
- Make sure the token is still valid
- Restart the bot

### Error Logs

The terminal will show all errors and problems. If you encounter persistent errors:

1. Copy the full error message
2. Check the [Support](#support) section
3. Contact the developer if necessary

## 📞 Support

If you have problems or questions:

- **Developer**: @alex1dev
- **Discord DM**: `alex1dev`
- **License issues**: Contact via DM

> **📧 Before contacting**: Make sure you have followed all installation and configuration steps.

## 📄 License

This software is distributed under a private license. Use is limited to authorized buyers.

---

**Thank you for your purchase!** 🎉

*Made with ❤️ by @alex1dev*