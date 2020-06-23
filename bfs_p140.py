from collections import deque

def main():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = ["kobla"]
    graph["kobla"] = ["ro1"]
    peopleQueue = deque()
    peopleQueue += graph["you"]
    alreadySearche = set()

    while peopleQueue:
        element = peopleQueue.popleft()
        if not element in alreadySearche:
            alreadySearche.add(element)
            if "1" in element:
                print(element)
                break
            element = graph[element]
            if element != []:
                peopleQueue += element



if __name__ == "__main__":
    main()