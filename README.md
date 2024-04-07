# Track
Arcade Discord Bot

# Contributors

1.  Kavya Gupta
2.  Subikshaa Sakthivel
3.  Aishwarya Sharma

# Problem Statement
Detective games are popular forms of entertainment that challenge players' deductive reasoning skills. However, organizing and hosting such games in a physical setting can be time-consuming and resource-intensive. To address this, we've built a Discord bot project centered around a discord arcade theme, introducing a single-player mystery game within the Discord environment. While not aimed at addressing societal issues, the project integrates a mystery game and some mini games to encourage prolonged engagement with the platform. Our mini-games offer a thrilling mix of code-breaking challenges and brain teasers. Half of which involve using real-world encryption methods to decipher secret messages, while the others test your vocabulary and thinking skills.


# Goal
Our goal is to provide Discord users with a fun and engaging gaming experience within the Discord arcade environment. We aim to stimulate problem-solving skills through a variety of cipher decryption questions and puzzles, delivering an interactive storytelling experience where players become detectives, piecing together clues to solve compelling murder mysteries.

# Features
* Case Selection: Users initially choose from a variety of mystery cases to solve.
* Interactive Gameplay: The bot presents users with a series of riddles and puzzles, guiding them through the investigation process.
* Clue System: Correctly answering questions reveals new information and clues, helping users progress in the investigation.
* Time to comprehend clues: There is no time limit for understanding and analysing the clues, the players can move forward to the next question in accordance to their grasping ability by positively reacting to the tick emoji in the reaction box.
* Time Limit: Users have a limited time of 50 seconds to answer each question, adding suspense and urgency to the gameplay.
* Final Guess: After gathering all the clues, users can make a final guess on the identity of the culprit.
* Open to exit: Furthermore, there's an option to exit the game at any time by positively reacting to the cross emoji in the reaction box.
* Displaying progress: In our game of hangman after every input that the user gives their progress in the game in displayed.

* CSS Styling: We've incorporated CSS styling to enhance the presentation of text.
* Use of images emojis: We've integrated images and emojis throughout the interface to make the game more engaging.
* Message Reactions: Users can express their responses to riddles using message reactions.

# Tech Stack
* Frontend
  * css
* Languages
  * python
* Libraries/Framework
  * random
  * asyncio
  * os
  * discord.py
  * discord.ext
* Dependency management
  * dotenv
* Tools
  * vs code
  * github
  * canva
* Backend
  * server_website

# How to run
## To set up the bot in yourlocal machine, follow these instructions:
Set up environment variables by creating a `.env` file in the project directory and adding your Discord bot token.<br/>
Run the bot by executing the `main.py` file using the command
```
python3 main.py
```
## To run the bot in the discord server, follow these instructions:
```
!start
```
This will prompt the user to select their desired game.
Enter the number of your choice and continue with the game.
1. Murder Mystery -
   * Once you choose Murder mystery you will be provided with the option to choose from 10 mysteries. Type in the desired number.
   * You will now have to select a reaction from the options based on the answer you wish to give
   * clicking on the cross will exit from the game
2. Scramble -
   * once you choose scramble you will be asked to descramble the given words using the hints
   * type in the right answer 
3. Hangman -
   * once you choose hangman you will be given the number of letters in the word.
   * for guessing a letter type in 
```
!guess (your guess)
```
   * typing in  
```
exit
```
will end the game <br/>

4. Morse -
  * After choosing it questions will be displayed type the respective answers
  * typing in  
```
exit
```
will end the game  <br/>
5. Caesar Cipher -
* After choosing it questions will be displayed type the respective answers
*  typing in  
```
exit
```
will end the game 

# Deployment
The discord bot is deployed on Github and Discord.

# Applications
* Entertainment: The bot provides users with a fun and interactive way to spend time with friends or community members.
* Education: The detective game format can be adapted for educational purposes, such as teaching critical thinking and problem-solving skills.
* Community Building: Hosting detective game events on Discord can help foster a sense of community and engagement among server members.

# Further improvements
We would like to add the following features to our bot:
* Player Profiles: Implement player profiles to track progress, achievements, and leaderboard rankings.
* Multiplayer Mode: Introduce multiplayer functionality to allow multiple users to collaborate or compete in solving cases together.

# Demo video

