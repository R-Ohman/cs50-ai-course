from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


xor_for_pairs_of_symbols = And(
    # A is a Knight or a Knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B is a Knight or a Knave
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # C is a Knight or a Knave
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    xor_for_pairs_of_symbols,
      
    Implication(AKnight, And(AKnight, AKnave)),         
    Implication(AKnave, Not(And(AKnight, AKnave))),     
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    xor_for_pairs_of_symbols,

    # If sentance is true, A is a Knight
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    xor_for_pairs_of_symbols,

    # A said truth -> B is the same kind
    Implication(
        AKnight,
        BKnight
    ),

    # A said lie -> B is different kind
    Implication(
        AKnave,
        BKnight
    ),

    # B said truth -> A is different kind
    Implication(
        BKnight,
        AKnave
    ),

    # B said lie -> A is the same kind
    Implication(
        BKnave,
        AKnave
    )

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    xor_for_pairs_of_symbols,

    Implication(AKnight, Or(AKnight, AKnave)),       # A said truth about being a knight/knave
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    Implication(
        BKnight,
        And(AKnave, CKnave)
    ),

    Implication(
        BKnave,
        Not(And(AKnave, CKnave))
    ),

    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
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
