#1.Add me to the queue
def add_me_to_the_queue(express_queue,normal_queue,ticket_type,person_name):
    if ticket_type==1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue
#2.Where are my friends?
def find_my_friend(queue,friend_name):
    return queue.index(friend_name)
#3.Can I please join them?
def add_me_with_my_friends(queue,index,person_name):
    queue.insert(index,person_name)
    return queue
#4.Mean person in the queue
def remove_the_mean_person(queue,person_name):
    queue.remove(person_name)
    return queue
#5.NameFellows
def how_many_namefellows(queue,person_name):
    return queue.count(person_name)
#6.Remove the las person
def remove_the_last_person(queue):
    copy=queue.copy()
    queue.pop()
    return copy[-1]
#7.Sort the queue List
def sorted_names(queue):
    return sorted(queue)

print(remove_the_mean_person(['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket'],'Ultron'))
print(add_me_with_my_friends(['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky'))