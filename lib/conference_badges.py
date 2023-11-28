def badge_maker(name):
    return f"Hello, my name is {name}."
names = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]

badges = [badge_maker(name) for name in names]

for badge in badges:
    print(badge)

def batch_badge_creator(names):
    
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return None

def printer(names):
    return None
