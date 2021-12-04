#!/bin/bash

AOC_SESSION=$(<../aoc_session.txt)
day=$(TZ='America/New_York' date +%-d)
year=$(date +%Y)
echo ${year}

echo "Submitting part $1 answer: $2"

response=$(curl -d "level=$1&answer=$2" -X POST "https://adventofcode.com/${year}/day/${day}/answer" --cookie session="${AOC_SESSION}" | grep "article")
#response=$(cat testing | grep "article")

echo $response

if [ $(echo $response | grep "That's the right answer" | wc -l) -gt 0 ];
then 
    open https://adventofcode.com/${year}/day/${day}

    # Open up new file
    newFile=day${day}_part2.py
    oldFile=day${day}_part1.py
    cp -n $oldFile $newFile
    open -a Visual\ Studio\ Code $newFile

fi

