# SSProject

Step 1: <br>
Run getNewReleases.py to get a text file called "newMusicFriday.txt" that contains all of the tracks and their authors fetched from the Spotify playlist "New Music Friday". newMusicFriday.txt format = Track"Authors(1, 2, 3 etc) <br><br>

Step 2: <br>
Run generalTweets.py to fetch tweets from Twitter based on the keywords (NEED TO FIGURE OUT) and fills out a text file for each song (tweets1.txt, tweets2.txt etc) containing the general tweets (could be relevant or irrelevant). All of these files will be in the directory dir_gen. <br><br>

Step 3: <br>
Run regexTweets.py to open each file in dir_gen (dir_gen/tweets1.txt etc) containing the general tweets for each song and and runs a regex on each tweet and saves only the relevant tweets in text files called rxtweets1.txt, rxtweets2.txt etc. All of these files will be in the directory dir_regex. <br><br>

Step 4: <br>
Run sentiment.py to determine the sentiment of each tweet contained in the files of the dir_regex directory (dir_regex/rxtweets1.txt etc) and make a prediction on the song (maybe output a number from 1 to 5 of what we think the popularity will be so that it's easier later on to compare to ground truths) <br><br>

Step 5: <br>
Obtain ground truths from the Spotify popularity feature. Fetch back each song contained in the newMusicFriday.txt about 2 weeks after it was collected and get its popularity number. <br> <br>

Step 6: <br>
Based on ground truths and predicted results create some type of regression to show the correctness of our evaluation.
