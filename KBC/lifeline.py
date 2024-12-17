import random

def use_lifeline(question, lifelines_used):
    if lifelines_used:
        print("You have already used your lifeline.")
        return None
    else:
        print("Lifeline used! Removing two incorrect option.")
        correct_answer = question["answer"]
        remaining_options = [correct_answer]
        while len(remaining_options)<2:
            option = random.randint(1,4)
            if option!=correct_answer and option not in remaining_options:
                remaining_options.append(option)
                remaining_options.sort()
        new_options = [question["options"][opt-1] for opt in remaining_options]
        return new_options

