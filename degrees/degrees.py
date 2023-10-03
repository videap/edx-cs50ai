import csv
import sys

from util import Node, StackFrontier, QueueFrontier, person_name_for_id, movie_for_id

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 4:
        sys.exit("Usage: python degrees.py [directory] [First Artist] [Second Artist]")
    directory = sys.argv[1] if len(sys.argv) >= 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(sys.argv[2]) or person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(sys.argv[3]) or person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    # test()
    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def test():
    print(neighbors_for_person(1))

    exit(0)

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    InitialNode = Node(source, None, None)
    Frontier = QueueFrontier()
    solved = False

    Frontier.add(InitialNode)

    while solved == False:

        #remove next node from the frontier
        try:
            CurrentNode = Frontier.remove()
        except:
            break

        if CurrentNode.state == target:
            print("SOLUTION FOUND")
            solved = True
            # break

        #get neighbours
        neighbors = neighbors_for_person(CurrentNode.state)

        #add them to frontier
        for n in neighbors:
            NewNode = Node(n[1], CurrentNode.state, n[0])
            Frontier.add(NewNode)

        # Frontier.show(people,movies)

    if solved:
        path=[(CurrentNode.action, CurrentNode.state)]


        while CurrentNode.parent != source:
            CurrentNode = get_from_explored(Frontier.explored, CurrentNode.parent, CurrentNode.action)
            path.append((CurrentNode.action, CurrentNode.state))
        path.reverse()
    else:
        path = None

    arr = []
    arr.reverse





    # should return array of tuples (movie, person)
    return path


def get_from_explored(explored_nodes, state, action):
    for node in explored_nodes:
        print(f"Checking state {node.state} if it's equeal to {state}, and also {node.action} is equal to {action}")
        if node.state == state:
            print("found it!")
            return node
    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]



def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[f"{person_id}"]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for co_star in movies[f"{movie_id}"]["stars"]:
            neighbors.add((movie_id, co_star))

    return neighbors


if __name__ == "__main__":
    main()
