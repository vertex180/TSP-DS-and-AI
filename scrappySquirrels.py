
import requests

def check_astronaut_suit(json_data):
    for attribute in json_data.get('attributes', []):
        if attribute.get('trait_type') == 'Clothes' and attribute.get('value') == 'Yellow Hood':
            return True
    return False

def main():
    astronaut_suit_squirrels = []
    for squirrel_id in range(1, 2001):
        url = f"https://scrappyart.s3.ap-south-1.amazonaws.com/json/{squirrel_id}"
        print('Check ', squirrel_id)
        response = requests.get(url)
        if response.status_code == 200:
            squirrel_data = response.json()
            print('Check 2')
            if check_astronaut_suit(squirrel_data):
                astronaut_suit_squirrels.append(squirrel_id)
                print('Check 3')
    
    print("Squirrels wearing astronaut suits:", astronaut_suit_squirrels)

if __name__ == "__main__":
    main()