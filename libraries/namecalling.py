import random

namecalling = ["Bitch", "Dumbass", "KnuckleHead", "ShitHead", "NumSkull", "HammerHead", "Bozo", "Wuss",
               "Fatso", "Wanker", "Weirdo", "Porker", "Geezer", "Spastic", "Doorknob", "Inbreeder",
               "Birdbrain", "Lamebrain", "Boogerface", "Poo-poo head"]


def namecaller():
    return namecalling[random.randint(0,len(namecalling))]