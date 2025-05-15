import os
import asyncio
import os
import asyncio
import random
import openai

# Patch event loop for notebook/IDE compatibility
try:
    import nest_asyncio
    nest_asyncio.apply()
except ImportError:
    pass

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Mock player actions (in place of real on-chain events)
ACTIONS = [
    ("Alice", "voted to kill", "Bob"),
    ("Charlie", "healed", "Alice"),
    ("Bob", "accused", "Charlie"),
    ("Alice", "betrayed", "Charlie"),
]

async def mock_onchain_actions():
    while True:
        await asyncio.sleep(random.randint(3, 7))
        yield random.choice(ACTIONS)

async def roast_message(player, action, target):
    prompt = f"In TeleMafia, {player} just {action} {target}. Roast them in a witty, playful way (1-2 sentences, fun, not mean)."
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a witty, playful mafia game NPC who roasts players."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

async def terminal_npc_demo():
    print("\n=== TeleMafia LLM NPC Terminal Demo ===\n")
    print("Watch as the NPC reacts to player actions in real time!\n")
    async for player, action, target in mock_onchain_actions():
        print(f"Player Action: {player} {action} {target}")
        roast = await roast_message(player, action, target)
        print(f"NPC Roast: {roast}\n{'-'*50}")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import asyncio
    asyncio.run(terminal_npc_demo())
