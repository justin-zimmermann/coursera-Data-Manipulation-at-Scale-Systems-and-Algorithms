import sys
import json
import string


def lines(file, scores):
    new_terms = {}
    new_terms_counts = {}
    for line in file:
        #line = line.encode('utf-8')
        line_dict = json.loads(line)
        if "text" not in line_dict.keys():
            pass
        else:
            line_sentiment = []
            words = line_dict["text"].encode('utf-8').translate(None, string.punctuation).split()
            for word in words:
                if word in scores.keys():
                    line_sentiment.append(scores[word])
                else:
                    line_sentiment.append(0.)
            for i, word in enumerate(words):
                if line_sentiment[i] == 0.:
                    if i == len(words) - 1:
                        inferred_sentiment = float(sum(line_sentiment)) / float(len(line_sentiment)) +\
                                             1. * line_sentiment[i - 1]
                    elif i == 0:
                        inferred_sentiment = float(sum(line_sentiment)) / float(len(line_sentiment)) +\
                                             1. * line_sentiment[i + 1]
                    else:
                        inferred_sentiment = float(sum(line_sentiment)) / float(len(line_sentiment)) +\
                                             0.5 * line_sentiment[i - 1] + \
                                             0.5 * line_sentiment[i + 1]
                    if inferred_sentiment != 0.:
                        if word in new_terms.keys():
                            new_terms[word] += inferred_sentiment
                            new_terms_counts[word] += 1.
                        else:
                            new_terms[word] = inferred_sentiment
                            new_terms_counts[word] = 1.
    for term in new_terms.keys():
        new_terms[term] = new_terms[term] / new_terms_counts[term]
        sys.stdout.write("%s %.3f\n" % (term, new_terms[term]))


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
