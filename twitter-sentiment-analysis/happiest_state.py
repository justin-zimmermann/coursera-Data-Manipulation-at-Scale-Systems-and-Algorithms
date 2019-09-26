import sys
import json


def lines(file, scores):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    state_sentiment = dict()
    state_count = dict()
    for line in file:
        #line = line.encode('utf-8')
        line_dict = json.loads(line)
        if "text" not in line_dict.keys():
            pass
        else:
            line_sentiment = 0
            words = line_dict["text"].encode('utf-8').split()
            for word in words:
                if word in scores.keys():
                    line_sentiment += scores[word]
            got_state = False
            if "user" in line_dict.keys():
                if "location" in line_dict['user'].keys():
                    for abb in states.keys():
                        if abb in line_dict['user']['location'].encode('utf-8') or \
                                states[abb] in line_dict['user']['location'].encode('utf-8'):
                            got_state = True
                            if abb in state_sentiment.keys():
                                state_sentiment[abb] += line_sentiment
                                state_count[abb] += 1
                            else:
                                state_sentiment[abb] = line_sentiment
                                state_count[abb] = 1
                            break
            if got_state == False:
                if "place" in line_dict.keys():
                    if type(line_dict['place']) == dict:
                        if line_dict['place']['country_code'] == "US":
                            for abb in states.keys():
                                if abb in line_dict['user']['location'].encode('utf-8'):
                                    got_state = True
                                    if abb in state_sentiment.keys():
                                        state_sentiment[abb] += line_sentiment
                                        state_count[abb] += 1
                                    else:
                                        state_sentiment[abb] = line_sentiment
                                        state_count[abb] = 1
                                    break
    happiest_state = "None"
    happiest_value = -10.
    for state in state_sentiment.keys():
        state_sentiment[state] = float(state_sentiment[state]) / float(state_count[state])
        if state_sentiment[state] > happiest_value:
            happiest_state = state
            happiest_value = state_sentiment[state]
    sys.stdout.write("%s" % happiest_state)
    #debugging / interesting info
    #for state in state_sentiment.keys():
     #   sys.stdout.write("%s, %.4f, %d\n" % (state, state_sentiment[state], state_count[state]))
    #note: can produce US color map of states according to how happy they are


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