class Name:
    def __init__(self,first_name,last_name,email,age):
        self.first_name =first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        self.is_rewards_member=True
        self.gold_card_points=200
        if self.is_rewards_member==True:
            print("User already a member.")
            return False
        else:
            return True
    
    def spend_points(self, amount):
        self.gold_card_points -=amount
        if self.gold_card_points>170:
            print('you have enough points')
        else:
            print("you don't have enough points")

Oussema = Name ("Oussama","Nouira","ouxavi80@gmail.com",20)
Oussema.display_info()
Oussema.enroll()
Oussema.display_info()
Oussema.spend_points(50)
Oussema.display_info()