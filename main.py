import random

#lists of components
excuse_starters = [
    "I'm sorry, but", "What had happened was", "Unfortunately,", "I regret to inform you that", "Due to unforeseen circumstances,"
    ]

excuse_reasons = [
    "there was a plethora of ducks circling in the road", "my alarm didn't go off", "I ate some bad Taco Bell", "my computer crashed and I lost all of my work"
    ]

excuse_endings = [
    "so I couldn't complete the task on time.", "was stranded for hours.", "which led to the delay.", "resulting in my inability to meet the deadline", "so uh, I don't have it done."
    ]
    
def generate_excuse():
    excuse_parts = []
    excuse_parts.append(random.choice(excuse_starters))
    excuse_parts.append(random.choice(excuse_reasons))
    excuse_parts.append(random.choice(excuse_endings))
    return " ".join(excuse_parts)
   
    
    final_excuse = random_starter + " " + random_reason + " " + random_ending
    return final_excuse
    
num_excuse = int(input("Enter the number of excuses to generate: "))


print("Generated excuses: ")
for _ in range(num_excuse):
        excuse = generate_excuse();
        print(excuse)
        print("-" * 40)
    
 