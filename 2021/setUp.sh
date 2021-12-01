#!/bin/bash

# sh ../setUp.sh day year (where day/year if not provided defautls to curr)
# needs to be run from the year directory
# add in session cookie into aoc_session.txt file at main scope 

AOC_SESSION=$(<../aoc_session.txt)
day=${1:-$(TZ='America/New_York' date +%-d)}
year=${2:-$(date +%Y)}

# save the unique user input file
inputFileName=${day}.in
> ${inputFileName} # erase file
curl https://adventofcode.com/${year}/day/${day}/input --cookie session="${AOC_SESSION}" >> ${inputFileName}

if [ ! -f "test${day}.in" ] 
then
    touch test${day}.in
fi

# set up python file 
codeFileName=day${day}.py
if [ ! -f "$codeFileName" ] 
then
    touch $codeFileName
    cat ../template/template.py >> $codeFileName
fi

sed -i ""  "s/%%DAY%%/${day}/g" $codeFileName
sed -i ""  "s/%%YEAR%%/${year}/g" $codeFileName
sed -i ""  "s/%%AOC_SESSION%%/${AOC_SESSION}/g" $codeFileName

open -a Visual\ Studio\ Code test${inputFileName}
open -a Visual\ Studio\ Code $codeFileName
open -a Visual\ Studio\ Code ${inputFileName}