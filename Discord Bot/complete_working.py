import discord
from discord.ext import commands
import random
import asyncio
from final_lists import questions_list
from listsv2 import title, description_victim, description_crime_scene, items, autopsy_report, forensic_report, backstories, alibis, description_alibis, witnesses, distance, answer, solution, suspects


intents = discord.Intents.default()
intents.message_content = True  # Required for message content
intents.reactions = True  # Required for adding reactions
client = commands.Bot(command_prefix="!", intents=intents)

questions = questions_list

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def start(ctx):
    await ctx.send('''Welcome detective! Alibi has got some cases for you to solve. Put your thinking hats on and once you are ready, enter the number corresponding to the mystery you want to solve today''')

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        user_msg = await client.wait_for('message', check=check, timeout=30)
        global i
        i = int(user_msg.content) - 1

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to respond. Please try again.")

    await ctx.send('''You will be provided with a set of questions answering each of them will reveal new information pertaining to the case. Incorrectly answering a question will lead to you losing out on the information corresponding to that question.
    Remember you have only 50 seconds to answer each question. 
    Type 'exit' anytime to end the game.''')
    await ask_question(ctx.channel, ctx.author, ctx)

async def ask_question(channel, author, ctx):
    questions_asked = 1

    shuffled_questions = questions
    random.shuffle(shuffled_questions)


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
            correct_answer = question["answer"].upper() # Get correct answer's emoji
            if selected_answer == "❌":
                await channel.send("Game ended.")
                break
            elif selected_answer == correct_answer:
                if(questions_asked == 1):
                    info_message = await channel.send("✅ Correct! Here's some information about the victim  : {}".format(description_victim[i]))
                elif(questions_asked == 2):
                    info_message = await channel.send("✅ Correct! Here's the description of the crime scene: {}".format(description_crime_scene[i]))
                elif(questions_asked == 3):
                    info_message = await channel.send("✅ Correct! The crime scene investigation has drawn attention to these four items  : {}".format(items[i]) )
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
                #await info_message.remove_reaction('✅', user)
            else:
                await channel.send("❌ Incorrect! moving on to the next question")  # Wrong emoji and text
        
        questions_asked += 1
        if questions_asked == 10:
            q = "It's now time to put your little grey cells to work and solve the case! Who do u think the murderer is: " +"\n" +suspects[i]
            q1 = await channel.send("```css\n{}\n``` ".format(q))
            await final_answer(ctx.channel, ctx.author, ctx,q1)
            break

async def final_answer(channel, author, ctx,q1):
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
        await channel.send("Time's up! You failed to answer the question." )
    else:
        if correct_answer == selected_answer : 
            await channel.send("✅ Congratulations!!")
        else:
            await channel.send("❌ Incorrect!")
    await channel.send(solution[i])

def check_reaction_and_author(message, author, emoji):
    def check(reaction,user):
        return user == author and str(reaction.emoji) == emoji
    return check

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
client.run('BOT_TOKEN')
