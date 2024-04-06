import discord
from discord.ext import commands
import random
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

# Define your questions and answers
questions = [
    {
        "question": "Who was the victim?",
        "answer": "James Smith",
        "info": "James Smith was a wealthy businessman with many enemies."
    },
    {
        "question": "Where did the murder take place?",
        "answer": "Stanford Manor",
        "info": "Stanford Manor is an old mansion on the outskirts of town."
    },
    # Add more questions, answers, and info here
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def start(ctx):
    await ctx.send("Welcome to the Murder Mystery Game! I will ask you a series of questions. Answer them correctly to reveal information about the case Type 'exit' anytime to end the game.")
    await ask_question(ctx.channel, ctx.author)

async def ask_question(channel, author):
    questions_asked = 0

    for question in questions:
        await channel.send("```css\n{}\n```".format(question["question"]))  # Box around the question

        def check(msg):
            return msg.author == author and msg.channel == channel

        try:
            response = await client.wait_for('message', timeout=30, check=check)
        except asyncio.TimeoutError:
            await channel.send("Time's up! You failed to answer the question." )
        else:
            if response.content.lower() == 'exit':
                await channel.send("Game ended.")
                break
            elif response.content.strip().lower() == question["answer"].lower():
                await channel.send("✅ Correct! Here's some information about the case : `{}`".format(question["info"]))  # Correct emoji and text
            else:
                await channel.send("❌ Incorrect! moving on to the next question")  # Wrong emoji and text
            questions_asked += 1

        if questions_asked >= 10:
            await channel.send("You've reached the maximum number of questions (10). Game ended.")
            break

# Get the token from environment variables
token = os.getenv('TOKEN')
if token is None:
    print("Error: Bot token not found in environment variables.")
else:
    client.run(token)
