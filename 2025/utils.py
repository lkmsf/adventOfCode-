

def clean_ranges(ranges, debug = False): 
    ranges.sort()

    cleaned_ranges = []
    ignore_ranges = []

    for i, (a,b) in enumerate(ranges): 
        if debug: print(f"looking at ({a}, {b})") 
        
        if (a,b) in ignore_ranges: 
            continue
            
        for c,d in ranges[i+1:]:
            # a b c d
            if c > b:
                # list is sorted 
                break
            # c d a b
            if d < a: 
                continue

            if c <= a:
                # c a d b
                if d <= b:
                    a = d+1

                # c a  b d
                if d > b:
                    a = -1
                    break

            elif c > a:
                #  a c d b 
                if d <= b:
                    ignore_ranges.append((c,d)) 		

                #  a c  b d
                if d > b:
                    b = c-1

            if debug: print(f" 	from {c}, {d}, ->  ({a}, {b})") 

        
        if debug: print(f" Changed to ({a}, {b})") 
        if a != -1:
            cleaned_ranges.append((a,b)) 

    return cleaned_ranges