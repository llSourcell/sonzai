# TeleMafia LLM NPC Demo

A  demo of an LLM-powered NPC agent that lives in TeleMafia’s chat and reacts to on-chain player actions with witty/roasting comments in real time.

## Features
- Listens for on-chain player actions
- Generates real-time LLM-powered reactions
- Posts reactions in a Telegram group chat

## Setup
1. Clone this repo
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set your API keys as environment variables:
    - `OPENAI_API_KEY` (for LLM)
    - `TELEGRAM_BOT_TOKEN` (for Telegram bot)
4. Run the bot:
    ```bash
    python main.py
    ```

## Customization
- Swap OpenAI for another LLM provider if desired.

