#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_hashtags', nargs='+', required=True)
args = parser.parse_args()

import os
import json
import glob
import matplotlib.pyplot as plt
from collections import defaultdict

# dictionary where each hashtag maps to a list of daily counts
# e.g. {'#python': [0, 5, 3, ...], '#covid': [10, 2, 8, ...]}
hashtag_counts = defaultdict(list)

# get all lang files sorted by date so x-axis is in order
input_files = sorted(glob.glob('outputs/geoTwitter20-*.zip.lang'))

for path in input_files:
    with open(path) as f:
        tmp = json.load(f)
    for hashtag in args.input_hashtags:
        # if the hashtag appears that day, sum its counts, otherwise 0
        if hashtag in tmp:
            hashtag_counts[hashtag].append(sum(tmp[hashtag].values()))
        else:
            hashtag_counts[hashtag].append(0)

# plot
days = range(1, len(input_files) + 1)
for hashtag in args.input_hashtags:
    plt.plot(days, hashtag_counts[hashtag], label=hashtag)

plt.xlabel('Days Since January 1, 2020')
plt.ylabel('Number of Tweets')
plt.legend()
title_var =  str(args.input_hashtags).replace('\'', '') + 'Frequency Over 2020'
plt.title(title_var)
plt.savefig(f'../img/{title_var}.png')
print(f"Plot saved to img/{title_var}.png")
