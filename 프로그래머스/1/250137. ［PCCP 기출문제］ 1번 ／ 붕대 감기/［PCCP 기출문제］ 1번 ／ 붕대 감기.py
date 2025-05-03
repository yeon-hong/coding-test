def solution(bandage, health, attacks):
    time = 1
    counter = 0
    max_health = health
    end_time = attacks[-1][0]
    for i in range(end_time):  
        hit, health = attack(time, health, attacks)
        if hit:
            counter = 0
            if health <= 0:
                return -1
        else:
            counter += 1
            health += bandage[1]
        if counter == bandage[0]:
            health += bandage[2]
            counter = 0
        health = max_health_check(max_health, health)
        time += 1
                    
    return health
                    
def max_health_check(max_health, health):
    if health > max_health:
            health = max_health
    return health

def attack(time, health, attacks):
    for row in attacks:
        if time == row[0]:
            health -= row[1]
            return True, health 
    return False, health 