import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/today?language=en"

def get_random_technology_fact():
    response= requests.get(url)
    if response.status_code == 200:
        fact_data= response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to find fact")

while True:
    user_input= input("Press enter to get random fact or type q to quit...")

    if user_input.lower() == 'q':
        break
    get_random_technology_fact()