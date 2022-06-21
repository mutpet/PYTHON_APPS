
heroes = {"batman": "Bruce Wayne", 
         "dr.strange": "Stephen Strange", 
         "doctor strange": "Stephen Strange",
         "spiderman": "Peter Parker",
         "pókember": "Peter Parker",
         "iron man": "Tony Stark",
         "vasember": "Tony Stark",
         "captain america": "Steve Rogers",
         "amerika kapitány": "Steve Rogers",
         "thor": "Thor Odin fia",
         "hulk": "Bruce Banner",
         "war machine": "James Rhodes",
         "black widow": "Natasha Romanoff",
         "fekete özvegy": "Natasha Romanoff",
         "vision": "Vízió",
         "vízió": "Vízió",
         "hawkeye": "Clint Barton",
         "sólyomszem": "Clint Barton",
         "black panther": "T'Challa",
         "fekete párduc": "T'Challa",
         "antman": "Scott Lang",
         "ant-man": "Scott Lang",
         "hangya": "Scott Lang",
         "wanda": "Wanda Maximoff",
         "aquaman": "Arthur Curry",
         "flash": "Barry Allen",
         "villam": "Barry Allen",
         "green lantern": "Harold 'Hal' Jordan",
         "zöld lámpás": "Harold 'Hal' Jordan",
         "hitman": "Tommy Monaghan",
         "joker": "Jack Napier",
         "lex luthor": "Alexander Joseph Luthor",
         "poison ivy": "Dr.Pamela Lillian Isley",
         "superman": "Clark Jerome Kent",
         "two face": "Harvey Dent",
         "two-face": "Harvey Dent",
         "kétarc": "Harvey Dent",
         "nick fury": "Nicholas Joseph"

}


def getRealName(find_hero):
 if find_hero in heroes:  
     for key, value in heroes.items():
      if key == find_hero:
         print(f"A megadott szuperhős hétköznapi, civil neve: {value}")
 else:
     print("A keresett szuperhős nem található!")

     
def cleanValidateInput(user_input):
  find_hero = "".join(user_input.rstrip().lstrip())
  #find_hero = user_input
  getRealName(find_hero.lower())

user_input = input("Kérlek add meg a szuperhős karakter nevét!\n")
cleanValidateInput(user_input)


