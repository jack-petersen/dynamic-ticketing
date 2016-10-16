

# https://www.reddit.com/r/nfl/comments/wt1sr/list_of_nfl_teams_by_media_market_size/
# Our dictionaries:
mediaMarketDict = {'denver': 4727, 'seattle': 4565, 'carolina': 8152, 'kansascity': 2903, 'arizona':4438, 'newengland':9684, 'pittsburgh':4396, 'greenbay':4186, 'cincinnati':4666, 'minnesota':5073, 'nyjets':22421, 'buffalo':2990, 'houston':6452,
            'detroit':8032, 'washington': 5853, 'philadelphia': 8688, 'atlanta':6462, 'indianapolis': 3266, 'losangeles':3986, 'baltimore':4248, 'nygiants':22421, 'neworleans':2635, 'oakland':10645, 'dallas':8071, 'chicago':10606, 'miami':1439,
            'sandiego':2683, 'sanfrancisco':10645, 'tampabay':4417, 'cleveland':4794, 'jacksonville':3660, 'tennessee':2667}

stardict = {'denver': {'vonmiller':85, 'aqibtalib':66, 'demarcusware':64, 'chrisharrisjr':48, 'demaryiusthomas':38, 'tjward':32, 'emmanuelsanders':26}, 'seattle': {'russellwilson':83, 'richardsherman':80, 'kamchancellor':68, 'michaelbennett':41,
            'earlthomas':34, 'dougbaldwin':28}, 'carolina': {'camnewton':100,'lukekuechly':93, 'gregolsen':62, 'thomasdavis':46, 'kawannshort':42, 'ryankalil':21, 'johnathanstewart':14},
            'kansascity': {'justinhouston':74, 'ericberry':45, 'marcuspeters':35, 'carlosdunlap':30, 'jamaalcharles':25, 'derrickjohnson':20, 'alexsmith':19, 'tambahall':16, 'traviskelce':9, 'jeremymaclin':8},
            'arizona':{'carsonpalmer':88, 'patrickpeterson':82, 'larryfitzgerald':73, 'tyrannmathieu':72, 'chandlerjones':52, 'calaiscampbell':29},
            'newengland':{'tombrady': 99, 'robgronkowski':91, 'julianedelman':13}, 'pittsburgh':{'antoniobrown':97, 'benroethlisberger':79, 'leveonbell':59, 'cameronheyward':12}, 'greenbay':{'aaronrodgers':94, 'claymatthews':57, 'mikedaniels':5},
            'cincinnati':{'ajgreen':84, 'genoatkins':71, 'andydalton':65, 'tylereifert':56, 'andrewwhitworth':33}, 'minnesota':{'adrianpeterson':95, 'harrisonsmith':27, 'linvaljoseph':24},
            'nyjets':{'darellerevis':76, 'brandonmarshall':75, 'muhammadwilkerson': 61}, 'buffalo':{'leseanmccoy':31, 'sammywatkins':4, 'richieincognito':3}, 'houston':{'jjwatt':98, 'deandrehopkins':81},'detroit':{'ezekielansah':57},
            'washington': {'joshnorman':89, 'trentwilliams':55, 'jordanreed':23, 'kirkcousins':15}, 'philadelphia': {'fletchercox':51},
            'atlanta':{'juliojones':92, 'devontafreeman':50}, 'indianapolis': {'andrewluck':8}, 'losangeles':{'aarondonald':86, 'toddgurley':78},
            'baltimore':{'marshalyanda':63}, 'nygiants':{'odellbeckhamjr':90, 'elimanning':53}, 'neworleans':{'drewbrees':70, 'cameronjordan':1}, 'oakland':{'khalilmack':87, 'reggienelson':40, 'derekcarr':1},
            'dallas':{'tyronsmith':58, 'dezbryant':49}, 'chicago':{'mattforte':10}, 'miami':{'suh':60, 'reshadjones':36, 'jarvislandry':2}, 'sandiego':{'philiprivers':54}, 'sanfrancisco':{'navorrobowman':39},
            'tampabay':{'dougmartin':67, 'lavontedavid':47, 'geraldmccoy':37}, 'cleveland':{'joethomas':77, 'garybarnidge':6}, 'jacksonville':{'allenrobinson':69, 'blakebortles':44, 'chrisivory':22, 'telvinsmith':17, 'allenhurns':11},
            'tennessee':{'delaniewalker':18}}

jerseydict = {'denver': {'vonmiller':20}, 'seattle': {'russellwilson':19, '12thman':16}, 'carolina': {'camnewton':12, 'lukekuechly':3}, 'kansascity': {}, 'arizona':{},
              'newengland':{'tombrady':23, 'robgronkowski':17, 'julianedelman':9}, 'pittsburgh':{'antoniobrown':22, 'benroethlisberger':10}, 'greenbay':{'aaronrodgers':14}, 'cincinnati':{}, 'minnesota':{}, 'nyjets':{}, 'buffalo':{}, 'houston':{},
              'detroit':{}, 'washington': {}, 'philadelphia': {'carsonwentz':21}, 'atlanta':{}, 'indianapolis': {}, 'losangeles':{'toddgurley':1}, 'baltimore':{}, 'nygiants':{'odellbeckhamjr':25, 'elimanning':5},
              'neworleans':{'drewbrees':8}, 'oakland':{'derekcarr':7, 'khalilmack':4}, 'dallas':{'ezekielelliot':18, 'dezbryant':15, 'dakprescott':13, 'jasonwitten':11}, 'chicago':{}, 'miami':{'jarvislandry':2},
              'sandiego':{}, 'sanfrancisco':{'colinkaepernick':24, 'navorrobowman':6}, 'tampabay':{}, 'cleveland':{}, 'jacksonville':{}, 'tennessee':{}}

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

varWeightDict = {'elo': 0.35, 'market': 0.15, 'division': .1, 'stars':.4 }



def calcEloSkill(eloDict, ht, vt):
    # Input: dictionary with elo ratings, hometeam, visiting team
    # Output: a number that serves as the modifier
    elosum = 0
    for i in eloDict:
        elosum += eloDict[i]
    eloaverage = elosum / 32.0
    vtelodiff = eloDict[vt] / eloaverage

    return vtelodiff



def calcStarPower(stardict, jerseydict, ht, vt):
    # Input: A dictionary mapping Teams to their "stars" according to top 100 players in NFL, a home team, an away team
    # Output: A number serving as modifier

    # Method to the madness: Take top 40 NFL players, assign them to teams in dictionary. We will be comparing star power
    # to "average" amount of star power, so we have to give each team a "star", if they were part of the top 100 list.
    # Matt Forte is an exception, but we will let it slide because the bears are terrible.

    # Iteratre through dict: for each team, a sum of their star power
    # The first part of star power
    totalstarsum =0
    starsum = {}
    for i in stardict:
        starsum[i] = 0
        for j in stardict[i]:
            starsum[i] += stardict[i][j]
            totalstarsum += stardict[i][j]
    averagestarsum = totalstarsum / 32.0
    starModifier = starsum[vt] * 1.0 / averagestarsum

    # The second part of star power
    jerseystarsum = {}
    totaljerseysum = 0
    for i in jerseydict:
        jerseystarsum[i] = 0
        for j in jerseydict[i]:
            jerseystarsum[i] += jerseydict[i][j]
            totaljerseysum+= jerseydict[i][j]
    averagejerseysum = totaljerseysum / 32.0
    jerseyModifier = jerseystarsum[vt] * 1.0 / averagejerseysum


    newStarModifier = (jerseyModifier * 0.5) + (starModifier *0.5)

    return newStarModifier


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
