import random
data = [
    {"name": "Cristiano Ronaldo", "followers": 630, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 482, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 430, "description": "Singer/Actress", "country": "USA"},
    {"name": "Kylie Jenner", "followers": 400, "description": "Entrepreneur", "country": "USA"},
    {"name": "Dwayne 'The Rock' Johnson", "followers": 390, "description": "Actor/Wrestler", "country": "USA"},
    {"name": "Ariana Grande", "followers": 380, "description": "Singer", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 364, "description": "Entrepreneur", "country": "USA"},
    {"name": "Beyoncé", "followers": 316, "description": "Singer", "country": "USA"},
    {"name": "Khloé Kardashian", "followers": 311, "description": "Entrepreneur", "country": "USA"},
    {"name": "Justin Bieber", "followers": 296, "description": "Singer", "country": "Canada"},
    {"name": "Kendall Jenner", "followers": 292, "description": "Model", "country": "USA"},
    {"name": "Taylor Swift", "followers": 263, "description": "Singer", "country": "USA"},
    {"name": "Neymar Jr.", "followers": 222, "description": "Footballer", "country": "Brazil"},
    {"name": "Virat Kohli", "followers": 259, "description": "Cricketer", "country": "India"},
    {"name": "Nicki Minaj", "followers": 225, "description": "Rapper", "country": "USA"},
    {"name": "Jennifer Lopez", "followers": 251, "description": "Singer/Actress", "country": "USA"},
    {"name": "Miley Cyrus", "followers": 212, "description": "Singer/Actress", "country": "USA"},
    {"name": "Kourtney Kardashian", "followers": 227, "description": "Entrepreneur", "country": "USA"},
    {"name": "Shakira", "followers": 88, "description": "Singer", "country": "Colombia"},
    {"name": "Billie Eilish", "followers": 110, "description": "Singer", "country": "USA"}
]
account_A  = random.choice(data)

account_B = random.choice(data)

if(account_A == account_B):
    account_B  = random.choice(data)
    
def account(account):
    account_name = account["name"]
    account_description  =account["description"]
    account_country  =account["country"]
    return(f"{account_name} a {account_description} from {account_country}")

print(f"Compare A : {account(account_A)}.")
print(f"Compare B : {account(account_B)}.")

guess = input("Who has more followers? Type 'A' or 'B':").lower()

a_follower_count = account_A["followers"]
b_follower_count = account_B["followers"]
    