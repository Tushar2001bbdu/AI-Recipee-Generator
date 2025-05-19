import spacy


nlp = spacy.load("en_core_web_sm")

# Sample recipe database (dictionary)
recipes = {
    "pasta": ["tomato", "garlic", "onion", "pasta"],
    "fried rice": ["rice", "onion", "carrot", "peas", "soy sauce"],
    "omelette": ["egg", "onion", "salt", "pepper"],
    "salad": ["lettuce", "tomato", "cucumber", "olive oil"],
    "poha": ["flattened rice", "mustard seeds", "onion", "turmeric"]
}

# Function to extract nouns from user input
def extract_ingredients(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

# Function to match ingredients with recipes
def find_recipes(user_input):
    user_ingredients = extract_ingredients(user_input)
    matched = []

    for recipe, ingredients in recipes.items():
        if len(set(user_ingredients).intersection(set(ingredients))) >= 2:
            matched.append(recipe)

    return matched


print("Welcome to the AI Recipe Generator!")
while True:
    user_input = input("Enter ingredients (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    results = find_recipes(user_input)
    if results:
        print("You can cook:")
        for recipe in results:
            print(f"{recipe}")
    else:
        print(" No matching recipes found.")
