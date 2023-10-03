class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.state == other.state
        else:
            return False


class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.explored = []

    def add(self, node):
        if self.not_duplicated(node):
            self.frontier.append(node)

    def not_duplicated(self, node):
        explored = any(explored_node == node for explored_node in self.explored) or any(frontier_node == node for frontier_node in self.frontier)
        return not explored

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            self.explored.append(node)
            return node



class QueueFrontier(StackFrontier):
    def __init__(self):
        self.frontier = []
        self.explored = []

    def add(self, node):
        if self.not_duplicated(node):
            self.frontier.append(node)

    def not_duplicated(self, node):
        explored = any(explored_node == node for explored_node in self.explored) or any(frontier_node == node for frontier_node in self.frontier)
        return not explored

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            self.explored.append(node)
            return node

    def show(self, people, movies):
        print("----------------------------------------")
        print("The frontier is:")
        for i in self.frontier:
            print(person_name_for_id(i.state, people), movie_for_id(i.action, movies), person_name_for_id(i.parent, people))

        print("")
        print("The explored set is:")
        for i in self.explored:
            print(person_name_for_id(i.state, people), movie_for_id(i.action, movies), person_name_for_id(i.parent, people))


        print("----------------------------------------")




def person_name_for_id(id, people):
    try:
        return people[f"{id}"]["name"]
    except KeyError:
        return "KeyError"
def movie_for_id(id, movies):
    try:
        return movies[f"{id}"]["title"]
    except KeyError:
        return "KeyError"