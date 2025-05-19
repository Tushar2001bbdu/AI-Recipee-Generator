# AI Recipe Generator Presentation

---

## Slide 1: Introduction

### AI Recipe Generator

- Uses **spaCy** NLP to extract ingredients from user input
- Matches ingredients with a small recipe database
- Suggests recipes based on available ingredients

---

## Slide 2: Key Components

- **spaCy**: For natural language processing
- **Recipe Database**: A dictionary of recipes and ingredients
- Functions:
  - `extract_ingredients(text)`: Extracts nouns (ingredients) from user input
  - `find_recipes(user_input)`: Matches ingredients with recipes

---

## Slide 3: How It Works

1. User inputs ingredients (e.g. "onion, tomato, garlic")
2. Extract nouns using spaCy NLP
3. Find recipes where 2 or more ingredients match
4. Display possible recipes to the user

---

## Slide 4: Code Snippet

```python
import spacy

nlp = spacy.load("en_core_web_sm")

recipes = {
    "pasta": ["tomato", "garlic", "onion", "pasta"],
    "fried rice": ["rice", "onion", "carrot", "peas", "soy sauce"],
    "omelette": ["egg", "onion", "salt", "pepper"],
    "salad": ["lettuce", "tomato", "cucumber", "olive oil"],
    "poha": ["flattened rice", "mustard seeds", "onion", "turmeric"]
}

def extract_ingredients(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

def find_recipes(user_input):
    user_ingredients = extract_ingredients(user_input)
    matched = []
    for recipe, ingredients in recipes.items():
        if len(set(user_ingredients).intersection(set(ingredients))) >= 2:
            matched.append(recipe)
    return matched
