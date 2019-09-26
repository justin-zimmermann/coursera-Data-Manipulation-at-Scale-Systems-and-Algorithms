import sys
import json
import operator


def lines(file):
    hashtag_count = dict()
    for line in file:
        line_dict = json.loads(line)
        if "text" not in line_dict.keys():
            pass
        else:
            if type(line_dict['entities']['hashtags']) == list:
                for hashtag in line_dict['entities']['hashtags']:
                    if hashtag['text'] in hashtag_count.keys():
                        hashtag_count[hashtag['text']] += 1
                    else:
                        hashtag_count[hashtag['text']] = 1
    ordered_list = sorted(hashtag_count.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        sys.stdout.write("%s %d\n" % (ordered_list[i][0].encode('utf-8'), ordered_list[i][1]))


def main():
    tweet_file = open(sys.argv[1])
    lines(tweet_file)

if __name__ == '__main__':
    main()