import sys
import json


def lines(file, scores):
    for line in file:
        #line = line.encode('utf-8')
        line_dict = json.loads(line)
        if "text" not in line_dict.keys():
            sys.stdout.write("0\n")
        else:
            line_sentiment = 0
            words = line_dict["text"].encode('utf-8').split()
            for word in words:
                if word in scores.keys():
                    line_sentiment += scores[word]
            sys.stdout.write("%d\n" % line_sentiment)


def build_sentiment_dict(file):
    scores = {}
    for line in file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = build_sentiment_dict(sentiment_file)
    lines(tweet_file, scores)

if __name__ == '__main__':
    main()
