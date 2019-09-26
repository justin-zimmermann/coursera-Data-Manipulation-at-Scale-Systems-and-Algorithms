import sys
import json
import string

def lines(file):
    total_counts = 0
    terms_counts = {}
    for line in file:
        line_dict = json.loads(line)
        if "text" not in line_dict.keys():
            pass
        else:
            words = line_dict["text"].encode('utf-8').translate(None, string.punctuation).split()
            total_counts += len(words)
            for word in words:
                if word in terms_counts.keys():
                    terms_counts[word] += 1
                else:
                    terms_counts[word] = 1
    for term in terms_counts.keys():
        terms_counts[term] = float(terms_counts[term]) / float(total_counts)
        sys.stdout.write("%s %.5f\n" % (term, terms_counts[term]))

def main():
    tweet_file = open(sys.argv[1])
    lines(tweet_file)

if __name__ == '__main__':
    main()