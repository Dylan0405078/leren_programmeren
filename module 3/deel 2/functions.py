import time
import math
from termcolor import colored
from data import *

##################### O03 #####################

def copper2silver(amount: int) -> float:
    return amount / 10

def silver2gold(amount: int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:
    return round(silver2gold(copper2silver(amount)), 2)


def platinum2gold(amount: int) -> float:
    return amount * 25

def getPersonCashInGold(personCash: dict) -> float:
    total_gold = 0
    if "copper" in personCash:
        total_gold += copper2gold(personCash["copper"])
    if "silver" in personCash:
        total_gold += silver2gold(personCash["silver"])
    if "gold" in personCash:
        total_gold += personCash["gold"]
    if "platinum" in personCash:
        total_gold += platinum2gold(personCash["platinum"])
    return total_gold

##################### O05 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    total_cost_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
    total_cost_gold = copper2gold(total_cost_copper)
    return total_cost_gold

##################### O06 #####################

def getFromListByKeyIs(lst: list, key: str, value: any) -> list:
    result = []
    for item in lst:
        if key in item and item[key] == value:
            result.append(item)
    return result

def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(people: list, friends: list) -> list:
    adventuring_people = getAdventuringPeople(people)
    share_with_friends = getShareWithFriends(friends)
    adventuring_friends = []
    for person in adventuring_people:
        if person in share_with_friends:
            adventuring_friends.append(person)
    return adventuring_friends

##################### O07 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    horse_cost = horses * 5 * 11
    tent_cost = tents * 3 * 7 * 11
    return copper2gold(horse_cost * JOURNEY_IN_DAYS + tent_cost)

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    item_texts = [f"{item['amount']}{item['unit']} {item['name']}" for item in items]
    if len(item_texts) > 1:
        return ', '.join(item_texts[:-1]) + ' & ' + item_texts[-1]
    else:
        return item_texts[0]

def getItemsValueInGold(items: list) -> float:
    total_cost_gold = 0
    for item in items:
        if item['price']['type'] == 'gold':
            total_cost_gold += item['price']['amount'] * item['amount']
        elif item['price']['type'] == 'silver':
            total_cost_gold += silver2gold(item['price']['amount'] * item['amount'])
        elif item['price']['type'] == 'copper':
            total_cost_gold += copper2gold(item['price']['amount'] * item['amount'])
    return round(total_cost_gold, 2)

##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total_gold = 0.0
    for person in people:
        if 'cash' in person and 'gold' in person['cash']:  
            total_gold += person['cash']['gold']
    return total_gold

##################### O10 #####################

def getInterestingInvestors(investors: list) -> list:
    interesting_investors = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            interesting_investors.append(investor)
    return interesting_investors

def getAdventuringInvestors(investors: list) -> list:
    adventuring_investors = []
    for investor in investors:
        if investor.get('interesting') and investor.get('adventuring'):
            adventuring_investors.append(investor)
    return adventuring_investors

def getTotalInvestorsCosts(investors, gearList):
    total_cost = 0.0
    
    for gear in gearList:
        total_cost += gear['amount'] * gear['price']['amount']
    
    for investor in investors:
        if investor['adventuring']:
            total_cost *= (1 + investor['profitReturn'] / 100)

            
    
    return round(total_cost, 2)

    




##################### O11 #####################

from data import COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT
def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    max_nights_human = leftoverGold // COST_INN_HUMAN_SILVER_PER_NIGHT
    max_nights_horse = leftoverGold // COST_INN_HORSE_COPPER_PER_NIGHT
    return int(min(max_nights_human, max_nights_horse) // (people + horses))

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    return float(nightsInInn * (COST_INN_HUMAN_SILVER_PER_NIGHT * people + COST_INN_HORSE_COPPER_PER_NIGHT * horses))

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()