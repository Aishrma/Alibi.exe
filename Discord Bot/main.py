import discord
import os
from discord.ext import commands
import random
import asyncio
from dotenv import load_dotenv
from questions import questions_list
from storylines import title, description_victim, description_crime_scene, items, autopsy_report, forensic_report, backstories, alibis, description_alibis, witnesses, distance, answer, solution, suspects
from href_crimescenes import images_list
from href_sync import sync_list
from href_title import title_list
from jumbled_words import jumbled_list

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Required for message content
intents.reactions = True  # Required for adding reactions
client = commands.Bot(command_prefix="!", intents=intents)

questions = questions_list
jumbled = jumbled_list

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def start(ctx):
    await ctx.send('''Hey! Welcome to the world of puzzles! Choose the type of puzzle you want to solve today by entering the corresponding number:''')
    await ctx.send("1. Murder Mystery")
    await ctx.send("2. Scramble")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        user_msg = await client.wait_for('message', check=check, timeout=30)
        choice = int(user_msg.content)

        if choice == 1:
            await murder_mystery(ctx)
        elif choice == 2:
            await scramble(ctx)
        else:
            await ctx.send("Invalid choice. Please enter either '1' or '2'.")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to respond. Please try again.")

async def murder_mystery(ctx):
    await ctx.send('''Welcome detective! Alibi has got some cases for you to solve. Put your thinking hats on and once you are ready, enter the number corresponding to the mystery you want to solve today''')

    await ctx.send("1. The Enigma of the Midnight Manor", file=discord.File(sync_list[0]))
    await ctx.send("2. Shadows in the Gallery", file=discord.File(sync_list[1]))
    await ctx.send("3. The Enigma at Hawthorn Manor", file=discord.File(sync_list[2]))
    await ctx.send("4. Shadows of Deception", file=discord.File(sync_list[3]))
    await ctx.send("5. Echoes of Betrayal", file=discord.File(sync_list[4]))
    await ctx.send("6. Whispers in the Shadows", file=discord.File(sync_list[5]))
    await ctx.send("7. Silent Whispers", file=discord.File(sync_list[6]))
    await ctx.send("8. Midnight Masquerade", file=discord.File(sync_list[7]))
    await ctx.send("9. A Brush with Death", file=discord.File(sync_list[8]))
    await ctx.send("10. Midnight Murmurs at Ravenwood Hall", file=discord.File(sync_list[9]))

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        user_msg = await client.wait_for('message', check=check, timeout=30)
        i = int(user_msg.content) - 1

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to respond. Please try again.")

    await ctx.send('''You will be provided with a set of questions. Answering each of them will reveal new information pertaining to the case. Incorrectly answering a question will lead to you losing out on the information corresponding to that question. You have only 50 seconds to answer each question. Type 'exit' anytime to end the game.''')
    await ask_question1(ctx.channel, ctx.author, ctx, i)

async def ask_question1(channel, author, ctx, i):
    questions_asked = 1

    shuffled_questions = questions
    random.shuffle(shuffled_questions)

    await ctx.send("The game starts now!", file=discord.File(title_list[i]))

    for question in shuffled_questions:
        try:
            message = await channel.send("```css\n{}\n```".format(question["question"]))
            
            for emoji in ["🇦", "🇧", "🇨", "🇩","❌"]:
                await message.add_reaction(emoji)

            reaction, user = await client.wait_for(
                "reaction_add", timeout=50, check=lambda r, u: u == ctx.author and r.emoji in ["🇦", "🇧", "🇨", "🇩","❌"]
            )
            if(reaction.emoji == "🇦"):
                selected_answer = "A"
            elif(reaction.emoji == "🇧"):
                selected_answer = "B"
            elif(reaction.emoji == "🇨"):
                selected_answer = "C"
            elif(reaction.emoji == "🇩"):
                selected_answer = "D"
            elif(reaction.emoji == "❌"):
                selected_answer = "❌"
        except asyncio.TimeoutError:
            await message.edit(content="Time's up! You failed to answer the question.")
        else:
            correct_answer = question["answer"].upper()
            if selected_answer == "❌":
                await channel.send("Game ended.")
                break
            elif selected_answer == correct_answer:
                if(questions_asked == 1):
                    info_message = await channel.send("✅ Correct! Here's some information about the victim  : {}".format(description_victim[i]))
                elif(questions_asked == 2):
                    info_message = await channel.send("✅ Correct! Here's the description of the crime scene: {}".format(description_crime_scene[i]) , file=discord.File(images_list[i])) #crime scene image
                elif(questions_asked == 3):
                    info_message = await channel.send("✅ Correct! The crime scene investigation has drawn attention to these four items  : {}".format(items[i]) ) #items  
                elif(questions_asked == 4):
                    info_message = await channel.send("✅ Correct! Examination of the body of the victim has given the following results : {}".format(autopsy_report[i]))
                elif(questions_asked == 5):
                    info_message = await channel.send("✅ Correct! Here's the forensic evidence cololected from the crime scene : {}".format(forensic_report[i]))
                elif(questions_asked == 6):
                    info_message = await channel.send("✅ Correct! We have four individuals under scrutiny : {}".format(backstories[i]))
                elif(questions_asked == 7):
                    info_message = await channel.send("✅ Correct! However the suspects claim to have the following alibis : {}".format(alibis[i]))
                elif(questions_asked == 8):
                    info_message = await channel.send("✅ Correct! here is a description of the places mentioned in the alibis {}".format(description_alibis[i]))
                elif(questions_asked == 9):
                    info_message = await channel.send("✅ Correct! Any good detective searches for witnesses here are the witnesses at the places where the suspects told they were at : {}".format(witnesses[i]))
                elif(questions_asked == 10):
                    info_message = await channel.send("✅ Correct! hmm, there is always a possibily that the killer could have travelled between these places. Here is the distance between those places and the crime scene  : {}".format(distance[i]))
                await info_message.add_reaction('✅')
                reaction , user = await client.wait_for('reaction_add', check =lambda r, u: r.message == info_message and u == author and str(r.emoji) == '✅')
            else:
                await channel.send("❌ Incorrect! Moving on to the next question")
        
        questions_asked += 1
        if questions_asked == 10:
            q = "It's now time to put your little grey cells to work and solve the case! Who do you think the murderer is:\n" + suspects[i]
            q1 = await channel.send("```css\n{}\n```".format(q))
            await final_answer(ctx.channel, ctx.author, ctx, q1, i)
            break

async def final_answer(channel, author, ctx, q1, i):
    try:
        for emoji in ["🇦", "🇧", "🇨", "🇩"]:
            await q1.add_reaction(emoji)

        reaction, user = await client.wait_for(
            "reaction_add", timeout=50, check=lambda r, u: u == ctx.author and r.emoji in ["🇦", "🇧", "🇨", "🇩"]
        )
        if(reaction.emoji == "🇦"):
            selected_answer = "A"
        elif(reaction.emoji == "🇧"):
            selected_answer = "B"
        elif(reaction.emoji == "🇨"):
            selected_answer = "C"
        elif(reaction.emoji == "🇩"):
            selected_answer = "D"

        correct_answer = answer[i]
            
    except asyncio.TimeoutError:
        await channel.send("Time's up! You failed to answer the question.")
    else:
        if correct_answer == selected_answer:
            await channel.send("✅ Congratulations!!")
        else:
            await channel.send("❌ Incorrect!")
    await channel.send(solution[i])


async def scramble(ctx):
    await ctx.send('''Welcome!''')

    await ctx.send('''You will be provided with a set of questions.
    Remember you have only 50 seconds to answer each question. 
    Type 'exit' anytime to end the game.''')
    await ask_question(ctx.channel, ctx.author, ctx)

async def ask_question(channel, author, ctx):
    questions_asked = 1

    shuffled_questions = jumbled
    random.shuffle(shuffled_questions)

    await ctx.send("The game starts now!")

    for question in shuffled_questions:
        message = await channel.send("```css\n{}\n```".format(question["question"]))

        def check(message):
            return message.author == author and message.channel == channel
        try:
            selected_answer = await client.wait_for("message", check=check, timeout=50)
            selected_answer = selected_answer.content.upper()

        except asyncio.TimeoutError:
            await message.edit(content="Time's up! You failed to answer the question.")
        else:
            correct_answer = question["answer"].upper()
            if selected_answer.upper() == "EXIT":
                await channel.send("Game ended.")
                break
            elif selected_answer == correct_answer:
                await channel.send("✅ Correct!")
            else:
                await channel.send("❌ Incorrect!")
        
        questions_asked += 1
        if questions_asked == 10:
            await channel.send("Congratulations! You have completed the game.")
            break


client.run(os.getenv('TOKEN'))
