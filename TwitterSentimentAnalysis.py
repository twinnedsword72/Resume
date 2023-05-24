"""
Author: Ishaan Singh
Purpose: This program uses sentiment analysis to determine whether tweets are positive, negative, or neutral.
Algorithm: Open files containing positive and negative words in which are then compared to the tweets where
the program counts the number of matches for both positive and negative. If number of positive words is greater than
negative words then the tweet is positive and vice versa. If number of positive words is equal to number of negative
words then the tweet is neutral.
"""
#Opens files containing tweets, positive words, negative words for reading
tweetsWords = open('Trump.txt', 'r')
posWords = open('positive.txt', 'r')
negWords = open('negative.txt', 'r')
stopWords = open('stopwords.txt', 'r')
x = tweetsWords.read()
y = x.splitlines()
#Initialize variables
aa = posWords.read()
bb = aa.splitlines()
cc = negWords.read()
dd = cc.splitlines()
ee = stopWords.read()
ff = ee.splitlines()
#Loop goes through each line finding the number of positive and negative words
for line in y:
 tweetContent=line
 numOfPos=0
 numOfNeg=0
 numOfStop = 0
 numOfOther = 0
 for line in bb:
  singleTweet=line
  if singleTweet in tweetContent:
        numOfPos+=1

 for line in dd:
  singleTweet2 = line
  if singleTweet2 in tweetContent:
                numOfNeg += 1

 for line in ee:
        singleTweet3 = line
        if singleTweet3 in tweetContent:
            numOfStop += 1
        else:
            numOfOther += 1
 #If number of positive words is greater than number of negative words then tweet is positive and vice versa.
 #Otherwise, if they are both equal, then the tweet is neutral
 totalCount = numOfPos+numOfNeg+numOfStop+numOfOther
 wordCountRatio = totalCount/151593
 if(numOfPos>numOfNeg):
     print("General sentiment appears to be positive\n")
     print('Positive word count is:',numOfPos)
     print('Negative word count:',numOfNeg)
     print('Stop word count is: ', numOfStop)
     print('Other word count is: ', numOfOther)
     print("Ratio for positive to negative word count is ", numOfPos/numOfNeg)
     print("The ratio of pos/neg/stop/other to total word count is,", wordCountRatio)
 elif(numOfNeg>numOfPos):
     print("General sentiment appears to be negative\n")
     print('Positive word count is:',numOfPos)
     print('Negative word count is:',numOfNeg)
     print('Stop word count is: ', numOfStop)
     print('Other word count is: ', numOfOther)
     print("Ratio for positive to negative word count is ", numOfPos/numOfNeg)
     print("The ratio of pos/neg/stop/other to total word count is", wordCountRatio)
 else:
     print("Sentiment is neutral\n")
