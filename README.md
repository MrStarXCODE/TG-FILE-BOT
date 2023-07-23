
# BASIC TELEGRAM FILE STORAGE BOT

This bot receives files of any type (documents, images, audio, video) from users, stores them in a private Telegram channel, and retrieves them upon request. Each stored file is associated with a unique identifier that is used to retrieve the file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

### Requirements
- Python
- `python-telegram-bot==13.6` library

Install the necessary library using:

```bash
pip install python-telegram-bot==13.6
```

## Usage

After installing the necessary package, set up your bot token and channel ID, then you can run the bot:

```bash
python main.py
```

Once the bot is running:
1. Send it a file of any type. The bot will store the file and provide you with a unique identifier for that file.
2. To retrieve a file, simply send the unique identifier to the bot.

## Support

If you find any issues or have suggestions for improvements, please file an issue in the GitHub issue tracker.

## Author

$Kek - MrStarXCODE - 22-07-2023
## License

This project is for personal use. Please do not distribute or use this code for commercial purposes without consent.

