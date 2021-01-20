# method 2: opening data file from the web
import urllib.request
import time

start = time.time()

try:
    url = 'https://cs.nyu.edu/~kapp/python/movie_reviews.txt'
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8').lower()
except:
    print ("Something went wrong!")
else:
    # isolate each line from the review file
    lines = data.split("\n")

    # set up an empty dictionary
    sentiment = {}

    # visit every line in the file
    for line in lines:

        # isolate the score (1st character on each line)
        review = int(line[0])

        # isolate the rest of the line
        rest = line[2:]

        # isolate each word
        words = rest.split(' ')

        # visit each word
        for w in words:

            # clean up each word by removing non-alphabetic characters
            clean = ""
            for c in w:
                if c.isalpha():
                    clean += c

            # is this a new word?  if so, add it to the dictionary
            if clean not in sentiment:
                sentiment[clean] = [review,1]

            # otherwise update the dictionary entry for this word
            else:
                sentiment[clean][0] += review
                sentiment[clean][1] += 1

    
    # PART 1
    part1_ui = input("Enter a word to test: ")

    # make user input set to lowercase
    part1_ui = part1_ui.lower()
    
    if part1_ui in sentiment:
        avg = sentiment[part1_ui][0]/sentiment[part1_ui][1]
        print ("'",part1_ui,"' appears ", sentiment[part1_ui][1], " times", sep="")
        print ("The average score for reviews containing the word '",part1_ui,"' is ", sentiment[part1_ui][0]/sentiment[part1_ui][1], sep="")
        if avg >= 2.1: # 2.1 because data leans more towards negative
            print ("This is a positive word")
        else:
            print ("This is a negative word")
    else:
        print ("'",part1_ui,"' appears ", 0, " times", sep="")
        print ("There is no average score for reviews containing the word '",part1_ui,"'",sep="")
        print ('Cannot determine if this word is positive or negative')
    
# PART 2

    # Function:   compute_sentiment  
    # Input:      a single phrase (str) in which the sentiment of will be analyzed
    # Processing: determines the average sentiment value
    # Output:     returns the sentiment value to the user
    def compute_sentiment(phrase):
        # make sure each word in phrase is not case sensitive
        phrase = phrase.lower()
        
        split_phrase = phrase.split(" ")
        
        # create loop to analyze each word
        total = []
        for w in range(len(split_phrase)):
            if split_phrase[w] in sentiment:
                # get average
                avg = sentiment[split_phrase[w]][0]/sentiment[split_phrase[w]][1]
                total.append(avg)  
                
        if len(total) > 0:
            # return total average
            return sum(total) / len(total)
        else:
            # if no words in the phrase exist in sentiment than return total avg of 2.0 = true neutral
            return 2.0

# PART 3
    
    finish = time.time()
    run_time = finish - start
    print("Initializing sentiment database\nSentiment database initialization complete\nTotal unique words analyzed:", len(sentiment), "\nAnalysis took", format(run_time, ",.2f"), "seconds to complete\n")

    # ask user to enter a phrase
    part2_ui = input("Enter a phrase to test: ")

    # call function
    avg_sentiment = compute_sentiment(part2_ui)
    
    # determine whether the phrase is positive or negative
    if avg_sentiment == 2.0:
        print("Average score for this phrase is:", avg_sentiment)
        print("This is a true neutral statement!")
    else:
        # output average score for the user phrase
        print("Average score for this phrase is:", avg_sentiment)
        
        if avg_sentiment >= 2.0:
            print("This is a POSITIVE phrase")
        else:
            print("This is a NEGATIVE phrase")
