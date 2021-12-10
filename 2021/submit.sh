#!/bin/bash

AOC_SESSION=$(<../aoc_session.txt)
day=$(TZ='America/New_York' date +%-d)
year=$(date +%Y)

cd day${day}

part=1
if [ -f "2.py" ]; then
    part=2
fi
answer=`pbpaste`

echo "Submitting part ${part} answer: ${answer}"

#response=$(curl -d "level=${part}&answer=${answer}" -X POST "https://adventofcode.com/${year}/day/${day}/answer" --cookie session="${AOC_SESSION}" | grep "article")
response=$(cat ../testing | grep "article")

echo $response

if [ $(echo $response | grep "That's the right answer" | wc -l) -gt 0 ];
then 
    if [ ${part} -eq 1 ]; then
        # part 1
        open https://adventofcode.com/${year}/day/${day}
        cp -n 1.py 2.py
        open -a Visual\ Studio\ Code 2.py
    else
        #part 2
        open https://adventofcode.com/2021/leaderboard/self
        cp -n 2.py fancier.py
        open -a Visual\ Studio\ Code fancier.py
    fi
fi

