from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

game_knowledge = And(
    # A is either a Knight or Knage, but not both
    Or(AKnight, AKnave),
    Or(
        Or(Not(AKnight),AKnave),
        Or(Not(AKnave),AKnight)
    ),

    # B is either a Knight or Knage, but not both
    Or(BKnight, BKnave),
    Or(
        Or(Not(BKnight),BKnave),
        Or(Not(BKnave),BKnight)
    ),

    # C is either a Knight or Knage, but not both
    Or(CKnight, CKnave),
    Or(
        Or(Not(CKnight),CKnave),
        Or(Not(CKnave),CKnight)
    ),

)


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    game_knowledge,

    # A says "I am both a knight and a knave."
    Or(Not(AKnight), And(AKnight, AKnave)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    game_knowledge,

    # A says "We are both knaves."
    Or(Not(AKnight), And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    game_knowledge,

    # A says "We are the same kind."
    Or(Not(AKnight), BKnight),
    Or(Not(AKnave), BKnight),

    # B says "We are of different kinds."
    Or(Not(BKnight),  AKnave),
    Or(Not(BKnave),  AKnave),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    game_knowledge,

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(Not(AKnight), AKnight),
    Or(Not(AKnave), AKnight),

    # B says "A said 'I am a knave'."
    Or(Not(BKnight), Or(Not(AKnight), AKnave)),
    Or(Not(BKnave), Or(Not(AKnave), AKnight)),

    # B says "C is a knave."
    Or(Not(BKnight), CKnave),
    Or(Not(BKnave), CKnight),

    # C says "A is a knight."
    Or(Not(CKnight), AKnight),
    Or(Not(CKnave), BKnave),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
