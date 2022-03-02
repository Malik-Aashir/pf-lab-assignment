import random
cards = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards_each = 3
player1Card =[]
player2Card =[]
for card in range(cards_each):
    c1 = random.choice(list(cards.values()))
    c2 = random.choice(list(cards.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))