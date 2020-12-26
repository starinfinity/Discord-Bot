import random

pickline = ["You’re so hot, my zipper is falling for you.",
            "They say that kissing is a language of love, so would you mind starting a conversation with me?",
            "I’m on top of things. Would you like to be one of them?",
            "Hey! My name is Microsoft. Can I crash at your place tonight?",
            "Is your name winter? Because you’ll be coming soon.",
            "Do you want to commit a sin for your next confessional?",
            "I’m not into watching sunsets, but I’d love to see you go down.",
            "Are you an exam? Because I have been studying you like crazy.",
            "Can you tell me what time you’ll come back to my place, please?",
            "Give me your car keys so I can drive you crazy.",
            "Is your name Earl Grey? Because you look like a hot-tea!",
            "I love my bed but I’d rather be in yours.",
            "Are you a haunted house? I’m going to scream when I’m in you.",
            "Your body is made up of 70% water. . .and I’m thirsty.",
            "Are you undressing me with your eyes?!",
            " Your outfit would look great on my bedroom floor.",
            "Is it hot in here? Or is it just you?"]


def pickup():
    return pickline[random.randint(0,len(pickline))]