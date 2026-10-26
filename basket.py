from itertools import combinations
from collections import Counter
def analyse(baskets, minimum_support=0.2):
    baskets=[set(b) for b in baskets]
    if not baskets: return []
    n=len(baskets); singles=Counter(x for b in baskets for x in b)
    pairs=Counter(p for b in baskets for p in combinations(sorted(b),2)); rules=[]
    for (a,b),count in pairs.items():
        if count/n < minimum_support: continue
        for left,right in ((a,b),(b,a)):
            confidence=count/singles[left]
            rules.append({'if':left,'then':right,'support':count/n,'confidence':confidence,'lift':confidence/(singles[right]/n)})
    return rules
if __name__=='__main__':
    import json
    print(json.dumps(analyse([['milk','bread'],['bread','eggs'],['milk','bread','eggs'],['milk']]),indent=2))
