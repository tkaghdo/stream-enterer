## 1. Git branches ##


cd ~
git clone /dataquest/user/git/chatbot
cd chatbot
git checkout -b more-speech

## 2. Switching branches ##


cd /home/dq/chatbot
git checkout more-speech
printf "\nprint('Kind of dull in here, right?')" >> bot.py
git add .
git commit -m "Added more output"

## 3. Pushing a branch to a remote ##


cd /home/dq/chatbot
git push origin more-speech

## 4. Merging branches ##


cd /home/dq/chatbot
git checkout master
git merge more-speech
git push origin master

## 5. Deleting branches ##


cd /home/dq/chatbot
git branch -d more-speech

## 6. Checking out branches from the remote ##


cd /home/dq
git clone /dataquest/user/git/chatbot chatbot2
cd chatbot2
git checkout -b happy-bot
printf "\nprint('Happiness level: 120')" >> bot.py
git add .
git commit -m "Made the bot 20% happier!"
git push origin happy-bot
cd ..
cd chatbot
git fetch
git checkout happy-bot
python bot.py

## 7. Finding differences across branches ##


cd /home/dq/chatbot
git --no-pager diff master happy-bot

## 8. Branch naming conventions ##


cd /home/dq/chatbot
git checkout -b feature/random-messages
printf "\nimport random\nmessages=['Hi', 'Hi.', 'How are you?', 'Today is a long day...']\nn=random.randint(1,len(messages))\nprint(messages[n])" >> bot.py
git add .
git commit -m "Added random messaging to the bot!"
git push origin feature/random-messages

## 9. Branch history ##


cd /home/dq/chatbot
git checkout feature/random-messages
git checkout -b feature/spam-messages