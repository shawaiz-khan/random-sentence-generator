import random

subjects = [
    "He",
    "She",
    "They",
    "The dog",
    "The cat",
    "John",
    "Mary",
    "The teacher",
    "A scientist",
    "The child",
]
verbs = [
    "jumps",
    "runs",
    "eats",
    "sleeps",
    "reads",
    "writes",
    "plays",
    "sings",
    "dances",
    "laughs",
]
objects = [
    "a book",
    "the ball",
    "the cake",
    "a song",
    "the park",
    "the piano",
    "a movie",
    "the game",
    "the story",
    "the toys",
]


def generateSentence():
    while True:
        newSubject = random.choice(subjects)
        newVerb = random.choice(verbs)
        newObject = random.choice(objects)
        sentence = f"{newSubject} {newVerb} {newObject}."

        yield sentence


newSentence = generateSentence()

choice = int(input("How many sentences you want to generate? (1 - 10): "))


for _ in range(choice):
    print(next(newSentence))
