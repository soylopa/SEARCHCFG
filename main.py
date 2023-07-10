import requests
def recipe_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = ''
    app_key = ''
    result = requests.get('https://developer.spotify.com/documentation/web-api/'.format(ingredient, app_id, app_key))   
    data = result.json()
    return data['hits']
def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
    print()
run()