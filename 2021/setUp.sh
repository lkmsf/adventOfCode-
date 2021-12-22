#!/bin/bash

# sh ../setUp.sh day year (where day/year if not provided defautls to curr)
# needs to be run from the year directory
# add in session cookie into aoc_session.txt file at main scope 

# text data into file: pbpaste > test,in

open https://adventofcode.com/${year}/day/${day}

AOC_SESSION=$(<../aoc_session.txt)
day=${1:-$(TZ='America/New_York' date +%-d)}
year=${2:-$(date +%Y)}

mkdir day${day}
cd day${day}

# save the unique user input file
inputFileName=data.in
> ${inputFileName} # erase file
curl https://adventofcode.com/${year}/day/${day}/input --cookie session="${AOC_SESSION}" >> ${inputFileName}

touch test.in

# set up python file 
codeFileName=1.py
cp -n ../../template/template.py $codeFileName
# sed -i ""  "s/%%DAY%%/${day}/g" $codeFileName

open -a Visual\ Studio\ Code test.in
open -a Visual\ Studio\ Code $codeFileName
open -a Visual\ Studio\ Code ${inputFileName}


# save test data into file

# also be sure to convert "html entities" to what they should be (ex. -&gt;)
response=$(curl "https://adventofcode.com/${year}/day/${day}" | perl -MHTML::Entities -pe 'decode_entities($_);') 

testData=$(echo "$response" | pcregrep -M -o1 "For example.+</p>\n<pre><code>((\n|.)*?)</code></pre>")

#remove <emp> - tried to remove any tags but too many false positives
testData=$(echo "$testData" | sed -e 's/<\/*em>//g')

echo "$testData" >> test.in