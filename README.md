# Aiogram 3 Bot Template

## 📚 Description
This is a fully-featured Telegram bot template built with **aiogram 3.x** (currently 3.7). It includes an admin panel, payment integration, database support, and modular architecture for scalable development.

## 🚀 Features
- **Admin Panel**: Manage users, announcements, and administrative tasks.
- **Payment Integration**: Support for YooKassa transactions.
- **Reminder System**: Schedule and manage automated reminders.
- **User Profiles**: Store and manage user data in a structured database.
- **State Management**: Easily manage bot states using FSM.
- **Environment Configuration**: Securely manage configurations with `.env` files.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mlt-melt/aiogram3BotTemplate.git
   cd aiogram3BotTemplate
   ```

2. Install dependencies:
   ```bash
   pip install -r storage/requirements.txt
   ```

3. Create a `.env` file in `storage/` and add your telegram bot and yookassa tokens and other configurations.

4. Fill a `config.py` file in `storage/` with your telegram bot url and admins ids list.

5. Start the bot:
   ```bash
   python bot.py
   ```

## 📄 Configuration
Settings are managed in the `.env` and `storage/config.py` files.

### Example `.env` file:
```
BOT_TOKEN=tg_bot_token
YOOKASSA_SHOP_ID=your_shop_id
YOOKASSA_SECRET_TOKEN=your_secret_token
```

## 💻 Usage
- Start the bot using `python bot.py`
- Access admin panel commands with `/admin`
- Customize bot handlers and commands in `handlers/`

## 🧠 Technologies
- **Python**
- **Aiogram 3.x**
- **SQLite**
- **YooKassa API**

## 📊 Database
- The bot uses an SQLite database (`db.db`) for user and session data.

## 👤 Author
**Melt**  
[GitHub Profile](https://github.com/mlt-melt)

## 📜 License
This project is licensed under the MIT License.
