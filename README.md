# adventOfCode-
Advent of code solutions 

w/ set up script and submit script (current is in 2021 folder). 

While normally I prioritize code readability, this is not a good example of this. This is a lot of "what cool thing can I get python to do". 

The other fun part of this is that I'm learning how to make bash scripts and send requests with curl to automate some of the process. Someday I hope to be fast enough at solving these problems to have any of this make a practical difference :) - for now it's just for fun.

TODO: 
* Vscode settings 
  * better shortcut for running a python file
* setUp script 
  * Learn how to use cron and automate this!
  * maybe separate the create files and download input script logic? No reason not to make the other files before the time
* submit script
  * lets also shorten this name if we're doing it that way
* Far off
  * might be a fun exercise to scrape the aoc reddit for python solutions to see different approaches
    * also would be good to learn this
  * Automate also downloading the testing input 
    * it's generally one of the first things within <code> blocks but not always
    * so find the first "sufficently" large code block
    * then write to the testing file but make sure formatting is correct
  * Might be fun to write this up too! Good explanation of basic bash script stuff / process of automating a thing

Done: 

1/9 
* setUp script 
  * change names to remove day numbers since we put them in a folder anyways 
* submit script
  * lets change this to the copy/paste value with the day being the single argument -> no arguments!
  * can this automatically also create a "fancier" file when we submit part 2 correctly

1/1
  * set up run so that it runs with the file directory instead of workspace directory 
  * open the advent of code website first instead of waiting for input file

1/3 
* don't try and do both parts in the same file
  * setup creates a part 1 file
  * submit copies part 1 into a new part 2 file
* Remove the main/function logic in the template (just more to worry about)

Before: 
* created a template/setup/submit scripts