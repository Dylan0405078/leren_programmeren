import time
from math import ceil, floor

from termcolor import colored
from data import *

##################### O03 #####################

def copper2silver(amount: int) -> float:
    return round((amount / 9), 2)

def silver2gold(amount: int) -> float:
    return round((amount / 4), 2)

def copper2gold(amount: int) -> float:
    return round(silver2gold(copper2silver(amount)), 2)

def platinum2gold(amount: int) -> int:
    return 20 * amount

def getPersonCashInGold(personCash: dict) -> float:
    gold = 0
    for cur, amount in personCash.items():
        if cur == 'platinum':
            gold += platinum2gold(amount)
        elif cur == 'gold':
            gold += amount
        elif cur == 'silver':
            gold += silver2gold(amount)
        elif cur == 'copper':
            gold += copper2gold(amount)
    return gold

##################### O05 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    return copper2gold((people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS)

##################### O06 #####################

def getFromListByKeyIs(lijst: list, key: str, value: any) -> list:
    return [item for item in lijst if key in item and item[key] == value]

def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends: list) -> list:
    return getFromListByKeyIs(getFromListByKeyIs(friends, 'adventuring', True), 'shareWith', True)

##################### O07 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return ceil(people / 3)

def getNumberOfTentsNeeded(people: int) -> int:
    return ceil(people / 4)

def getTotalRentalCost(horses: int, tents: int) -> float:
    kosten_gold = silver2gold(horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)
    kosten_gold += tents * COST_TENT_GOLD_PER_WEEK * ceil(JOURNEY_IN_DAYS / 7)
    return kosten_gold

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    item_line = ''
    aantal_items = len(items)
    separator = ', '
    for i, item in enumerate(items):
        if aantal_items > 1 and i == aantal_items - 2:
            separator = ' & '
        item_line += f"{item['amount']}{item['unit']} {item['name']}" + separator
    return item_line[:-2].strip()

def toPersonCash(kosten: dict) -> dict:
    person_cash_dict = dict()
    amount = 0
    for k, v in kosten.items():
        if k == 'amount':
            amount = v
        if k == 'type':
            person_cash_dict.update({v: amount})
            amount = 0
    return person_cash_dict

def getItemsValueInGold(items: list) -> float:
    return round(sum(map(lambda item: round(getPersonCashInGold(toPersonCash(item['price'])) * item['amount'], 2), items)), 2)

##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    return sum(map(lambda person: getPersonCashInGold(person['cash']), people))

##################### O10 #####################

def getInterestingInvestors(investors: list) -> list:
    return list(filter(lambda a: a['profitReturn'] <= 15, investors))

def getAdventuringInvestors(investors: list) -> list:
    return list(filter(lambda investor: investor['adventuring'], getInterestingInvestors(investors)))

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    aantal_mee = len(getAdventuringInvestors(investors))
    bedrag = COST_TENT_GOLD_PER_WEEK * ceil(JOURNEY_IN_DAYS / 6) * aantal_mee  # tentkosten
    bedrag += silver2gold(COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS * aantal_mee)  # paarden kosten
    bedrag += copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS * aantal_mee)  # eten
    bedrag += copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS * aantal_mee)  # eten paarden
    bedrag += getItemsValueInGold(gear) * aantal_mee  
    return round(bedrag, 2)

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    return floor(leftoverGold / getJourneyInnCostsInGold(1, people, horses))

def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    bedrag = silver2gold(nightsInInn * people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    bedrag += copper2gold(nightsInInn * horses * COST_INN_HORSE_COPPER_PER_NIGHT)
    return round(bedrag, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    return list(map(lambda investor: round(profitGold * investor['profitReturn'] / 100, 2), getInterestingInvestors(investors)))

def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    return round(max((profitGold - sum(investorsCuts)), 0) / fellowship, 2)

##################### O14 #####################

def getEarnings(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    #info ophalen
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    gold_profit = getAdventurerCut(profitGold, investorsCuts, len(adventuringFriends) + len(adventuringInvestors) + 1)

    adventurerProfit = gold_profit + 10 * len(adventuringFriends)

    # verdeel de uitkomsten
    for person in people:
        start_gold = getPersonCashInGold(person['cash'])

        end_gold = start_gold
        if person == mainCharacter:
            end_gold += adventurerProfit
        elif person in adventuringFriends:
            end_gold += gold_profit - 10
        elif person in interestingInvestors:
            end_gold += investorsCuts[interestingInvestors.index(person)]
            if person in adventuringInvestors:
                end_gold += gold_profit

        earnings.append({
            'name'   : person['name'],
            'start'  : round(start_gold, 2),
            'end'    : round(end_gold, 2)
        })

    return earnings

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