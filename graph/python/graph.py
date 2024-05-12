from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = set()

    while search_queue: #while queue isn't empty
        person = search_queue.popleft() #grab the first person off the queue
        if not person in searched:
            if person_is_seller(person): #check if the person is a mango seller
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person] #not a a mango seller, add all of the person's friends to the search queue
                searched.add(person)
    return False

search("you")