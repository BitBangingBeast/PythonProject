import random
import os
clear=lambda:os.system('cls')
player={ "player_name":"",
    "deck":[],
    "count":[0,[],0],
  }
IA={ "player_name":"the House",
    "deck":[],
    "count":[0,[],0],
  }
deck=[2,3,4,5,6,7,8,9,10,"king","queen","jack","Ace"]

#functions


def hit(Player,Deck):
  return Player.append(random.choice(Deck))


def count(hand,total):
  count1=0
  min_value=0
  for card in range(len(hand)):
    
    if hand[card]== "king" or hand[card]=="queen" or hand[card]=="jack":
      count1+=10
    elif hand[card]=="Ace":
      min_value+=1
      total[1].append(hand[card])
    else:
      count1+=hand[card]
  total[0]=count1
  total[2]=count1+min_value
  
  return total
def count_IA_Ace(IA_count):
  how_much11=0
  for i in range(len(IA_count[1])):
    if IA_count[1][i] == "Ace":
      if (IA_count[0]+11):
        IA_count[0]+=11
        how_much11+=1
      else:
        IA_count[0]+=1
  while IA_count[0]>21 and how_much11!=0:
    IA_count[0]-=10
    how_much11-=1
  IA_count[1]=[]
  return IA_count


#main 


player["player_name"]=input("enter your name: ") 

for i in range(2):
  player["deck"].append(random.choice(deck))
  IA["deck"].append(random.choice(deck))
p_deck=player["deck"]
IA_deck=IA["deck"]
Count=count(player["deck"],player["count"])

print(f'{player["player_name"]} your card {p_deck} ')
print(f'{IA["player_name"]} his card {IA_deck[0]} ')

serve=input("do you want to be served yes or no?:  ")
you_lost=False
while serve == "yes" and you_lost==False :
  clear()
  player["deck"].append(random.choice(deck))
  p_deck=player["deck"]
  Count=count(player["deck"],player["count"])
  if Count[2]>21:
    you_lost=True
  print(f'your card {p_deck}')
  print(f'{IA["player_name"]} his card {IA_deck[0]} ')
  if you_lost==False:
    serve=input("do you want to be served again yes or no?:  ")
clear()
if you_lost:
  print(f'{player["player_name"]} you lost with this deck {player["deck"]} and a total count of {Count[2]}')
else:
  iA_count=count(IA["deck"],IA["count"])
  for i in range (len(Count[1])):
   Count[0]+=int(input(("you have an Ace what do you want to set it to 1 or 11?: ")))

  iA_count =count_IA_Ace(iA_count)
 
 
  if iA_count[0]>17:
    IA["deck"].append(random.choice(deck))
    iA_count=count(IA["deck"],IA["count"])
    iA_count =count_IA_Ace(iA_count)
    print(iA_count)

  if iA_count[0]==Count[0]:
    print(f'{player["player_name"]} you draw with {IA["player_name"]} and your deck was {player["deck"]} and his deck {IA["deck"]}' )
  elif iA_count[0]>Count[0]:
    print(f'{player["player_name"]} you lost to {IA["player_name"]} and your deck was {player["deck"]} and his deck {IA["deck"]} his total was {iA_count[0]} and your total {Count[0]}' )
  else:
      print(f'{player["player_name"]} you won on {IA["player_name"]} and your deck was {player["deck"]} and his deck {IA["deck"]} his total was {iA_count[0]} and your total {Count[0]}' )
