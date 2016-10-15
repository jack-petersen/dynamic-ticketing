

# https://www.reddit.com/r/nfl/comments/wt1sr/list_of_nfl_teams_by_media_market_size/
# Our dictionaries:
mediaMarketDict = {'denver': 4727, 'seattle': 4565, 'carolina': 8152, 'kansascity': 2903, 'arizona':4438, 'newengland':9684, 'pittsburgh':4396, 'greenbay':4186, 'cincinnati':4666, 'minnesota':5073, 'nyjets':22421, 'buffalo':2990, 'houston':6452,
            'detroit':8032, 'washington': 5853, 'philadelphia': 8688, 'atlanta':6462, 'indianapolis': 3266, 'losangeles':3986, 'baltimore':4248, 'nygiants':22421, 'neworleans':2635, 'oakland':10645, 'dallas':8071, 'chicago':10606, 'miami':1439,
            'sandiego':2683, 'sanfrancisco':10645, 'tampabay':4417, 'cleveland':4794, 'jacksonville':3660, 'tennessee':2667}

stardict = {'denver': {'vonmiller':85, 'aqibtalib':66, 'demarcusware':64}, 'seattle': {'russellwilson':83, 'richardsherman':80, 'kamchancellor':68}, 'carolina': {'camnewton':100,'lukekuechly':93, 'gregolsen':62}, 'kansascity': {'justinhouston':74},
            'arizona':{'carsonpalmer':88, 'patrickpeterson':82, 'larryfitzgerald':73, 'tyrannmathieu':72},
            'newengland':{'tombrady': 99, 'robgronkowski':91}, 'pittsburgh':{'antoniobrown':97, 'benroethlisberger':79, 'leveonbell':59}, 'greenbay':{'aaronrodgers':94}, 'cincinnati':{'ajgreen':84, 'genoatkins':71, 'andydalton':65}, 'minnesota':{'adrianpeterson':95},
            'nyjets':{'darellerevis':76, 'brandonmarshall':75, 'muhammadwilkerson': 61}, 'buffalo':{'leseanmccoy':31}, 'houston':{'jjwatt':98, 'deandrehopkins':81},'detroit':{'ezekielansah':57},'washington': {'joshnorman':89}, 'philadelphia': {},
            'atlanta':{'juliojones':92}, 'indianapolis': {'andrewluck':8}, 'losangeles':{'aarondonald':86, 'toddgurley':78},
            'baltimore':{'marshalyanda':63}, 'nygiants':{'odellbeckhamjr':90}, 'neworleans':{'drewbrees':70}, 'oakland':{'khalilmack':87},
            'dallas':{'tyronsmith':58}, 'chicago':{'mattforte':10}, 'miami':{'suh':60}, 'sandiego':{'philiprivers':54}, 'sanfrancisco':{'navorrobowman':39}, 'tampabay':{'dougmartin':67}, 'cleveland':{'joethomas':77}, 'jacksonville':{'allenrobinson':69},
            'tennessee':{'delaniewalker':18}}

divisiondict = {'seattle': ['arizona', 'losangeles', 'sanfrancisco'], 'arizona': ['seattle', 'sanfrancisco', 'losangeles'], 'sanfrancisco': ['seattle', 'arizona', 'losangeles'], 'losangeles': ['arizona', 'seattle', 'sanfrancisco'],
                'minnesota': ['greenbay', 'detroit', 'chicago'], 'greenbay': ['minnesota', 'detroit', 'chicago'], 'detroit': ['greenbay', 'minnesota', 'chicago'], 'chicago': ['greenbay', 'detroit', 'minnesota'],
                'tampabay': ['carolina', 'neworleans', 'atlanta'], 'carolina': ['tampabay', 'neworleans', 'atlanta'], 'neworleans': ['carolina', 'tampabay', 'atlanta'], 'atlanta': ['carolina', 'neworleans', 'tampabay'],
                'philadelphia': ['washington', 'dallas', 'nygiants'], 'washington': ['philadelphia', 'dallas', 'nygiants'], 'dallas': ['washington', 'philadelphia', 'nygiants'], 'nygiants': ['washington', 'dallas', 'philadelphia'],
                'denver': ['sandiego', 'oakland', 'kansascity'], 'sandiego': ['denver', 'oakland', 'kansascity'], 'oakland': ['sandiego', 'denver', 'kansascity'], 'kansascity': ['sandiego', 'oakland', 'denver'],
                'pittsburgh': ['cincinnati', 'cleveland', 'baltimore'], 'cincinnati': ['pittsburgh', 'cleveland', 'baltimore'], 'cleveland': ['cincinnati', 'pittsburgh', 'baltimore'], 'baltimore': ['cincinnati', 'cleveland', 'pittsburgh'],
                'indianapolis': ['houston', 'tennessee', 'jacksonville'], 'houston': ['indianapolis', 'tennessee', 'jacksonville'], 'tennessee': ['houston', 'indianapolis', 'jacksonville'], 'jacksonville': ['houston', 'tennessee', 'indianapolis'],
                'miami': ['newengland', 'buffalo', 'nyjets'], 'newengland': ['miami', 'buffalo', 'nyjets'], 'buffalo': ['newengland', 'miami', 'nyjets'], 'nyjets': ['newengland', 'buffalo', 'miami']}

eloDict = {'denver': 1637, 'seattle': 1635, 'carolina': 1634, 'kansascity': 1621, 'arizona':1613, 'newengland':1605, 'pittsburgh':1591, 'greenbay':1582, 'cincinnati':1578, 'minnesota':1567, 'nyjets':1522, 'buffalo':1519, 'houston':1506,
            'detroit':1503, 'washington': 1496, 'philadelphia': 1488, 'atlanta':1486, 'indianapolis': 1484, 'losangeles':1479, 'baltimore':1475, 'nygiants':1469, 'neworleans':1464, 'oakland':1455, 'dallas':1446, 'chicago':1444, 'miami':1439,
            'sandiego':1438, 'sanfrancisco':1437, 'tampabay':1412, 'cleveland':1395, 'jacksonville':1389, 'tennessee':1349}

varWeightDict = {'elo': 0.35, 'market': 0.1, 'division': .15, 'stars':.4 }



def calcEloSkill(eloDict, ht, vt):
    # Input: dictionary with elo ratings, hometeam, visiting team
    # Output: a number that serves as the modifier
    elosum = 0
    for i in eloDict:
        elosum += eloDict[i]
    eloaverage = elosum / 32.0
    vtelodiff = eloDict[vt] / eloaverage

    return vtelodiff



def calcStarPower(stardict, ht, vt):
    # Input: A dictionary mapping Teams to their "stars" according to top 100 players in NFL, a home team, an away team
    # Output: A number serving as modifier

    # Method to the madness: Take top 40 NFL players, assign them to teams in dictionary. We will be comparing star power
    # to "average" amount of star power, so we have to give each team a "star", if they were part of the top 100 list.
    # Matt Forte is an exception, but we will let it slide because the bears are terrible.

    # Iteratre through dict: for each team, a sum of their star power
    totalstarsum =0
    starsum = {}
    for i in stardict:
        starsum[i] = 0
        for j in stardict[i]:
            starsum[i] += stardict[i][j]
            totalstarsum += stardict[i][j]
    averagestarsum = totalstarsum / 32.0
    starModifier = starsum[vt] * 1.0 / averagestarsum
    return starModifier




def calcMarketSize(mediaMarketDict, ht, vt):
    # Input: A dictionary with net worth of teams, a dictionary with "Market sizes" of each team
    # Output: A number serving as a modifier
    mediaMarketSum = 0
    for i in mediaMarketDict:
        mediaMarketSum += mediaMarketDict[i]


    mediaMarketAvg = mediaMarketSum / 32.0
    mediaMarketdiff = mediaMarketDict[vt] / mediaMarketAvg

    return mediaMarketdiff


def sameDivision(divisiondict, ht, vt):
    # Input: A double dictionary with each team mapped to the other teams in its division
    # Output: A number serving as a modifier

    # A ticket is more valuable if the visiting team is in a different division, as fans are willing to pay more to see
    # different players/teams.

    if vt in divisiondict[ht]:
        return 0.9
    else:
        return 1.1


def calcModifier(eloDict, mediaMarketDict, divisiondict, stardict, ht, vt, varweight):
    # Input: results from functions above, also a dictionary with how each of the functions should be weighted.
    # Output: a final modifier

    elo = calcEloSkill(eloDict, ht, vt)
    market = calcMarketSize(mediaMarketDict, ht, vt)
    division = sameDivision(divisiondict, ht, vt)
    stars = calcStarPower(stardict, ht, vt)

    finalweight = (varweight['elo'] * elo) + (varweight['market'] * market) + (varweight['division'] * division) + (varweight['stars'] * stars)
    return finalweight

print "mod =", calcModifier(eloDict, mediaMarketDict, divisiondict, stardict, 'jacksonville', 'indianapolis', varWeightDict)
