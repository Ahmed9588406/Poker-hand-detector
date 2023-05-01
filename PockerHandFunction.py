
"""
this function determine the answer tha shown in mt hands depends on the rules I attached
in the directory of this projects
"""
def Find_Pocker_Hand(hand):
    ranks = [] # represent the number in the card
    suits = [] # represent the symbol in the card
    possible_Ranks = []

    # looping throw the hand to make different rank from suits
    for card in hand:
        """
        test 1: in this if else statement an error happened
        when we ant to get the rank we get the first element but in the case 
        of 10 we only get the 1 instead of 10 so this if else fixes this error
        """
        if len(card) == 2:
            # Getting the rank
            rank = card[0]
            # Getting the suit
            suit = card[1]
            """
            we need to make the numbers that represent ranks to check of a royal flush
            """
        else:
            # Getting the rank
            rank = card[0:2]
            # Getting the suit
            suit = card[2]
        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11
        # testing 2
        #print(rank, suit)
        # Appending the results in there corresponding list
        ranks.append(int(rank)) # error 2 we make this type casting because we are assigning this to integer
        suits.append(suit)

    # print(ranks)
    sortedRanks = sorted(ranks)
    # Test 3 to print the ranks and the suits
    # print(ranks, suits)
    # print(sortedRanks)

    # Checking the Royal Flush and Straight Flush and Flush
    """
    it's a  flush if the suits of the all cards in the hand (5 cards) is the same 
    so we can take the appearance of just one and compare it with 5 
    """
    # And we can check if it's a Flush by this condition
    if suits.count(suits[0]) == 5:
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks \
                and 10 in sortedRanks:
            possible_Ranks.append(10)
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possible_Ranks.append(9)
        else:
            possible_Ranks.append(6)  # -- Flush
    # Straight Flush (10 11 12 13 14)
    """
    check the element before 11 and add one to it and see of there are equal to each other
    11 == 10+1 (True)it will go to the next element
    12 == 11+1  (True)
    if we replace the 10 element with say 7 then the equation will be 11 == 7+1 
    which is false so its not a straight flush
     So if all of them give us true then it's a Straight Flush
    """
    # as I mentioned above I will start from the element 1 not 0 because 0 has no previous element
    if all(sortedRanks[i] == sortedRanks[i-1] +1 for i in range(1, len(sortedRanks))):
        possible_Ranks.append(5)

    hand_unique_value = list(set(sortedRanks))
    """ Four of a kind (3, 3, 3, 3,5) ther all the same except one of the cards
     we will handel it with the set when we apply set it will be (3, 5)
     # 3 3 3 3 5--set--- 3 5 --- Four of a kind
     # 3 3 3 5 5--set--- 3 5 --- Full house
    """

    if len(hand_unique_value) == 2:
        for value in hand_unique_value:
            if sortedRanks.count(value) == 4: # Four of a kind
                possible_Ranks.append(8)
            if sortedRanks.count(value) == 3: # Full house
                possible_Ranks.append(7)
    """
    Three of a kind and Pair
    5 5 5 6 7 -- set-- 5 6 7 unique values =3 Three of a kind
    8 8 7 7 2 -- set-- 8 7 2 unique values =3 Two pair
    """
    if len(hand_unique_value) == 3:
        for value in hand_unique_value:
            if sortedRanks.count(value) == 3: #  Three of a kind
                possible_Ranks.append(4)
            if sortedRanks.count(value) == 2: # Two pair
                possible_Ranks.append(3)

    # Pair
    # 5 5 3 6 7 ---set---5 3 6 7 - unique values = 4 --Pair
    if len(hand_unique_value) == 4:
        possible_Ranks.append(2)



    if not possible_Ranks:
        possible_Ranks.append(1)
    # Testing print(possible_Ranks)

    pockerHandRank = {10:"Royal Flush", 9:"Straight Flush", 8:"Four of a Kind", 7:"Full House", 6:"Flush",
                      5:"Straight", 4:"Three of a kind", 3:"Two Pair", 2:"Pair", 1:"High Card"}
   # Testing 0 to see if the function works or not
    out_put = pockerHandRank[max(possible_Ranks)]
    print(hand, out_put)
    return out_put



if __name__ == "__main__":
    Find_Pocker_Hand(["KH", "AH", "QH", "JH", "10H"])  # Royal Flush
    Find_Pocker_Hand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    Find_Pocker_Hand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    Find_Pocker_Hand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    Find_Pocker_Hand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    Find_Pocker_Hand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    Find_Pocker_Hand(["10H", "10C", "10D", "2D", "2D"])  # Three of a Kind
    Find_Pocker_Hand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    Find_Pocker_Hand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    Find_Pocker_Hand(["KD", "5H", "2D", "10C", "JH"])  # High Card