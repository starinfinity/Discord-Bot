import random

roasts = ["You’re the reason God created the middle finger.",
          "You’re a grey sprinkle on a rainbow cupcake.",
          "If your brain was dynamite, there wouldn’t be enough to blow your hat off.",
          "You are more disappointing than an unsalted pretzel.",
          "Light travels faster than sound which is why you seemed bright until you spoke.",
          "We were happily married for one month, but unfortunately we’ve been married for 10 years.",
          "Your kid is so annoying, he makes his Happy Meal cry.",
          "You have so many gaps in your teeth it looks like your tongue is in jail.",
          "Your secrets are always safe with me. I never even listen when you tell me them.",
          "I’ll never forget the first time we met. But I’ll keep trying."
          "I forgot the world revolves around you.My apologies, how silly of me.",
          "I only take you everywhere I go just so I don’t have to kiss you goodbye.",
          "Hold still.I’m trying to imagine you with personality.",
          "Our kid must have gotten his brain from you! I still have mine.",
          "Your face makes onions cry.",
          "The only way my husband would ever get hurt during an activity is if the TV exploded.",
          "You look so pretty.Not at all gross, today.",
          "It’s impossible to underestimate you."]


def roaster():
    return roasts[random.randint(0, len(roasts)-1)]
