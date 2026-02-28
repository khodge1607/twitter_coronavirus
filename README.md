# Coronavirus twitter analysis

This project scanned all geotagged tweets (about 1.1 billion tweets), narrowed down to all tweets sent in 2020 to monitor for the spread of the coronavirus on social media. The instructions followed for this analysis can be found at <https://github.com/mikeizbicki/twitter_coronavirus>


## MapReduce Process
Used MapReduce to sort through tweets. I looked at 17 [hashtags](hashtags) in particular. That list can be found <hashtaglist>. The map step counted all the tweets featuring those hashtags based on their language and country. Code can be found [here](src/map.py). The reduce step combined each day of 2020's data together and can be found [here](src/reduce.py). All the outputs of the mapping step are in the outputs folder, and outputs of the Reduce step are found in the [combined.country](src/combined.country) and [combined.lang](src/combined.land) files. 

## Alternative MapReduce
The reduce process was then modified to take a list of hashtags as inputs, and then track each hashtag's count for each day of the year. This process can be found [here](src/alternative_reduce_v2.py). 

## Visualizations

Shows top 10 countries where tweets with "#coronavirus" originated from. 
<img src="img/%23coronavirus.png">

Shows top 10 countries where tweets with "#코로나바이러스" originated from. 
<img src="img/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png">

Shows top ten langauges of tweets with "#coronavirus". 
<img src="img/combined.lang%23coronavirus.png">

Shows top 10 langauges of tweets with "#코로나바이러스". 
<img src="img/combined.lang%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png">

Shows how #coronavirus" and "sick" changed in their usage across 2020. 
<img src="img/%5B%23sick%2C%20%23coronavirus%5DFrequency%20Over%202020.png">

