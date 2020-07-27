def sentenceMaker(phrase):
    interrogatives = ("how", "when", "why" )
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

result = []
while True:
    user_input = input("Say something: ")
    if user_input == "/end":
        break
    else:
        result.append(sentenceMaker(user_input))

print(" ".join(result))
