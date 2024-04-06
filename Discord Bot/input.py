import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# Create a Discord client with command functionality
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('Login complete.')

@bot.command()
async def start_dob_conversation(ctx):
    # Prompt the user to enter their date of birth
    await ctx.send("Please enter your date of birth (YYYY-MM-DD):")

    def check(message):
        # Check if the message is from the same user and channel
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Wait for the user's response
        dob_message = await bot.wait_for('message', check=check, timeout=30)

        # Save the user's date of birth into a variable
        user_dob = dob_message.content

        # Print the user's date of birth
        print("User's Date of Birth:", user_dob)

        # Send a confirmation message
        await ctx.send(f"Your date of birth '{user_dob}' has been saved successfully.")
    
    except asyncio.TimeoutError:
        # If the user takes too long to respond
        await ctx.send("Sorry, you took too long to respond. Please try again.")

# Run the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))
