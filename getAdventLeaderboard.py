import requests 
import json 
import sys 
import operator 
from datetime import datetime
import pytz
import os

TOTAL_PEOPLE = 27
SCORE_DATA = "aocLb.txt"
LD_NUM = 688160

def main(): 
    args = sys.argv[1:]
    if len(args) and args[0] == "help":  
        printDirs() 
        return 

    flags = {"users": [], "day": list(map(str, range(1, 26))), "year": str(datetime.now().year)} 


    i = 0 
    while(i < len(args)): 
        if "-" not in args[i]: 
            printDirs() 
        key = args[i][1:]
        if key in ["reload", "offset"]: 
            flags[key] = True 
            i += 1
        elif key in ["year"]: 
            if args[i + 1] != flags["year"]: 
                flags["year"] = args[i+1]
            i += 2
        else: 
            flags[key] = args[i + 1].split(",") 
            i += 2

    if os.path.exists(SCORE_DATA): 
        with open(SCORE_DATA) as f: 
            data = json.load(f) 
            if data["event"] != flags["year"]: 
                flags["reload"] = True 

    if "reload" in flags: 
        print("Redownloading Leaderboard info...") 
        redownloadFile(flags["year"]) 
        formatFile(flags["year"]) #in case change mind on how to store the data, we write to the file twice 
        print("Done!") 

    printData(flags) #flags["day"], flags["users"], flags["sortByTime"])

def printDirs():
    print("Flags: ")
    print("-reload") 
    print("-day _,_,.... (1-25)") 
    print("-year _ (if not default")
    print("-users _,_,_...")
    print("-sortByOffset (for star 2 - False means sort by (part 2 - part1)") 

def printData(flags): #days, users, sortByTime):
    days, users, sortByOffset = flags["day"], flags["users"], "offset" in flags
    with open(SCORE_DATA) as f: 
        data = json.load(f) 

    for day in days: 
        scores = data[day] 

        #print out 
        nameLen  = len(max(scores["1"].keys(), key = len, default = "")) + 2 
        timeLen = 20 

        print(f"Day {day}\n")
        for star in [1,2]: 
            print(f"Star {star}")

            scoresForStar = scores[str(star)]
            

            if star == 2:
                defaultOrder =  sorted(scoresForStar.items(), 
                        #somewhat janky way to sorted by time duration 
                        key = lambda a: ("z" if "day" in a[1][0] else "") + ("0" if len(a[1][0].split()[0]) == 1 else "") + a[1][0]) 
                if sortByOffset: 
                    order =  sorted(scoresForStar.items(), 
                            key = lambda a: ("z" if "day" in a[1][1] else "") + ("0" if len(a[1][1].split()[0]) == 1 else "") + a[1][1]) 
                else: 
                    order =  sorted(scoresForStar.items(), 
                            key = lambda a: ("z" if "day" in a[1][0] else "") + ("0" if len(a[1][0].split()[0]) == 1 else "") + a[1][0]) 
            else: 
                defaultOrder =  sorted(scoresForStar.items(), 
                        key = lambda a: ("z" if "day" in a[1] else "") + ("0" if len(a[1].split()[0]) == 1 else "") + a[1]) 
                order =  sorted(scoresForStar.items(), key = lambda a: ("z" if "day" in a[1] else "") + ("0" if len(a[1].split()[0]) == 1 else "") + a[1]) 
                #order =  sorted(scoresForStar.items(), key = lambda a: ("z" if "day" in a[1] else "") + a[1]) 
                #order =  sorted(scoresForStar.items(), key = lambda a: datetime.timedelta(a[1]))

            defaultOrder = {name[0]: i for i, name in enumerate(defaultOrder, 1)}

            for n, s in order: 
                i = defaultOrder[n]
                if users and n not in users: continue
                print(f"{i}".rjust(2), f"{n}".ljust(nameLen), f"{s if star == 1 else s[0]}".ljust(timeLen), end = "") 
                if star == 2: 
                    print(f" ({s[1]})".ljust(timeLen), end = "")
                print(f"(+{TOTAL_PEOPLE - i + 1})".rjust(8 + (2 - star) * timeLen), end = "") 
                print() 
            print()
    
    
def redownloadFile(year): 
    #download file 
    url = "https://adventofcode.com/" + year + "/leaderboard/private/view/" + LD_NUM + ".json" 

    with open("../cookies.txt") as f: 
        cookies = f.read().strip()
    cookies = [c.split("=") for c in cookies.split(";")]
    cookies = {key: val for key, val in cookies}

    r = requests.get(url, cookies = cookies)
    with open(SCORE_DATA, 'w') as f: 
        json.dump(r.json(), f)
    

def formatFile(year): 
    with open(SCORE_DATA) as f: 
        data = json.load(f) 
    memberData = data["members"]

    people = {} 
    for p in memberData.keys(): 
        name = memberData[p]["name"] 
        if not name: 
            name = "Anon#" + p 
        people[p] = name 

    scoresByDay = {}  
    for day in range(1, 26): 
        if day == 1: challengeStart = datetime(int(year), 11, 30, 21) #, tzinfo = pytz.timezone("US/Eastern")) 
        else: challengeStart = datetime(int(year), 12, day - 1, 21) #, tzinfo = pytz.timezone("US/Eastern")) 

        scoresByDay[day] = {1:{}, 2:{}}

        for n, name in people.items(): 
            curr = memberData[n]["completion_day_level"]

            if str(day) in curr: 
                score1 = curr[str(day)]["1"]["get_star_ts"]
                part1Finished = datetime.fromtimestamp(int(score1)) 

                scoresByDay[day][1][name] = str(part1Finished - challengeStart) 

                if "2" in curr[str(day)]: 
                    score2 = curr[str(day)]["2"]["get_star_ts"]
                    part2Finished = datetime.fromtimestamp(int(score2)) 
                    scoresByDay[day][2][name] = str(part2Finished - challengeStart), str(part2Finished - part1Finished) 

    scoresByDay["event"] = data["event"]
    with open(SCORE_DATA, 'w') as f: 
        json.dump(scoresByDay, f)

if __name__ == "__main__":
    main()
