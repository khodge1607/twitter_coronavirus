# Coronavirus twitter analysis

This project scanned all geotagged tweets (about 1.1 billion tweets), narrowed down to all tweets sent in 2020 to monitor for the spread of the coronavirus on social media. The instructions followed for this analysis can be found at <https://github.com/mikeizbicki/twitter_coronavirus>


## MapReduce Process
Used MapReduce to sort through tweets. We looked at ten hashtag in particular. That list can be found <hashtaglist>. The map step counted all the tweets featuring those hashtags based on their language and country. Code can be found at <src/map.py>. The reduce step combined each day of 2020's data together and can be found at </Reduce.py>. All the outputs of the mapping step are in the outputs folder, and outputs of the Reduce step are found in the combined.country and combined.lang files. 

## Visualizations


