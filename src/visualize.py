#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
#items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items:
 #   print(k,':',v)

items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)[:10]
items = items[::-1]

# plot bar chart
labels = [k for k, v in items]
values = [v for k, v in items]

plt.figure(figsize=(15, 5))
plt.bar(labels, values)
plt.title(args.key)
plt.xlabel('Key')
plt.ylabel('Percent' if args.percent else 'Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
input_name = os.path.basename(args.input_path)
plt.savefig('img/' + input_name + args.key + '.png')
print('Plot saved to img/' + input_name + args.key + '.png')
