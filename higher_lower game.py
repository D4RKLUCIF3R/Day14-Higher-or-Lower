from game_data import data
import art
import random 



def comp_play(i,j):
    a = data[i]['follower_count']
    b = data[j]['follower_count']
   
    
    if a >= b:
        choice = "a" 
    else:
        choice = "b"
    return choice

def compare(i,j):
    text = " "
    text1 = " "
    for key in data[i]:
        if key != "follower_count":
            if key != "country":
                text += f"{data[i][key]}, "
            else:
                text+= f"{data[i][key]}"
                
    for key in data[j]:
        if key != "follower_count":
            if key != "country":
                text1 += f"{data[j][key]}, "
            else:
                text1 += f"{data[j][key]}"
    print(art.logo)
    print(text)
    print(art.vs)
    print(text1)



lost = False
i = random.randint(0,len(data)-1)
j = random.randint(0,len(data)-1)
score = 0

while(lost != True and i!=j):
    
   
    compare(i,j)
    c_choice = comp_play(i,j)
    u_choice = input("Who has more followers? 'A' or 'B' :").lower() #user choice
    
    if c_choice == u_choice:
        i = random.randint(0,len(data)-1)
        j = random.randint(0,len(data)-1)
        print(i,j)
        score+=1 
        print(f"You are right! Score is {score}")
    else:
        print(f"You lost! Final Score is {score}")
        lost = True
    
    
