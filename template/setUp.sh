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
open -a Visual\ Studio\ Code ${inputFileName}

if [[! -f "test${day}.in"]]; then
    touch test${day}.in
    open -a Visual\ Studio\ Code test${inputFileName}

# set up python file 
codeFileName=day${day}.py
if [[! -f "$codeFileName"]]; then
    touch $codeFileName
    cat ../template/template.py >> $codeFileName

    sed -i ""  "s/%%FILE_NAME_HERE%%/${inputFileName}/g" $codeFileName
fi

open -a Visual\ Studio\ Code $codeFileName