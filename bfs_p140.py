from collections import deque

def main():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["an1uj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    peopleQueue = deque()
    peopleQueue += graph["you"]

    while True:
        element = peopleQueue.popleft()
        if "1" in element:
            print(element)
            break
        element = graph[element]
        if element != []:
            peopleQueue += element



if __name__ == "__main__":
    main()