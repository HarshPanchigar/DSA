# Problem 3 — Character & Temperature Classifier
#
# Take:
#
# A temperature temp
# A character ch
#
# For temperature, print:
#
# Cold   → temp < 15
# Warm   → 15 <= temp <= 30
# Hot    → temp > 30
#
# For the character, determine whether it is:
#
# Vowel
# Consonant
# Uppercase
# Lowercase
# Digit
# Special Character
from idlelib.sidebar import temp_enable_text_widget

temp = 3
ch = "Harsh"

if temp <= 15:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("HOT")

if ch.isalpha():
    if ch.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")

    if ch.isupper():
        print("Uppercase")
    else:
        print("Lowercase")

elif ch.isnumeric():
    print("Digit")

else:
    print("Special Character")