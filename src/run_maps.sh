#1/bin/bash

for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
	echo "Starting $file"
	nohup python3 map.py --input_path "$file" &
done
echo "All map.py started"
