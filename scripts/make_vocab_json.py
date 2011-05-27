# ~/geo2/web/twitter_geo_viz/scripts % python make_vocab_json.py < ~/vocab > ../vocab.json 

import sys,json

vocab_lines = sys.stdin.readlines()
word_and_counts = [line.split() for line in vocab_lines]

word2id = {}
for word,c in word_and_counts:
  word2id[word] = len(word2id) + 1

word2id_str = json.dumps(word2id)
print word2id_str
