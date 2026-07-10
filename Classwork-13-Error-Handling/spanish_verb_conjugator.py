# Classwork 09 - Spanish Verb Conjugator
# Armando Karin Molina Marrufo

# PROCESS - Define pronouns list and conjugation endings dictionary
pronouns = ['Yo', 'Tu', 'El', 'Nosotros', 'Vosotros', 'Ellos']

endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT - Ask user for a Spanish verb
try:
    verb = input("Write a Spanish verb (ar/er/ir): ")

    if len(verb) < 3:
        raise ValueError("The verb is too short to be valid.")

    # PROCESS - Extract stem and ending, then look up conjugations
    stem = verb[:-2]
    ending = verb[-2:]

    if ending not in endings:
        raise KeyError(ending)

    conjugations = endings[ending]

    # OUTPUT - Print all six conjugations
    for index, pronoun in enumerate(pronouns):
        print(f"{pronoun} {stem}{conjugations[index]}")

except ValueError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Error: '{e}' is not a valid Spanish verb ending. Only 'ar', 'er', and 'ir' are supported.")
