## 1. Git remotes ##

~$ git clone /dataquest/user/git/chatbot

## 2. Making changes to cloned repositories ##

~/chatbot$ git --no-pager diff $HASH2 $HASH

## 3. The master branch ##

~/chatbot$ git branch

## 4. Pushing changes to the remote ##

~/chatbot$ git push origin master

## 5. Viewing individual commits ##

~/chatbot$ git show

## 6. Commits and the working directory ##

~/chatbot$ git diff b486 8c2c

## 7. Switching to a specific commit ##

~/chatbot$ git reset --hard 8c2c

## 8. Pulling from a remote repo ##

~/chatbot$ git pull origin master

## 9. Referring to the most recent commit ##

~/chatbot$ git reset --hard HEAD~1