#!/bin/bash
day=${1:-$(TZ='America/New_York' date +%-d)}
year=${2:-$(date +%Y)}

# also be sure to convert "html entities" to what they should be (ex. -&gt;)
response=$(curl "https://adventofcode.com/${year}/day/${day}" | perl -MHTML::Entities -pe 'decode_entities($_);') 

testData=$(echo "$response" | pcregrep -M -o1 "For example.+</p>\n<pre><code>((\n|.)*?)</code></pre>")

#remove <emp> - tried to remove any tags but too many false positives
testData=$(echo "$testData" | sed -e 's/<\/*em>//g')

echo "$testData" >> test.in


