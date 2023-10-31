import string
from collections import Counter
import matplotlib.pyplot as plt
clear = open("text.txt", encoding='utf-8').read()
lower = clear.lower()
punctuation = lower.translate(str.maketrans('', '', string.punctuation))

split = punctuation.split()
remove_letter = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                 "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                 "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                 "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                 "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                 "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                 "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                 "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                 "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                 "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
emp_list = []
for letter in split:
    if letter not in remove_letter:
        emp_list.append(letter)
emotional_list = []
with open("emotional.txt", "r") as file:
    for i in file:
        show = i.replace(",", "").replace("'", "").replace("\n", "").strip()
        word, emotion = show.split(":")
        # print("word :" + word + " " + "emotion :" + emotion)

        if word in emp_list:
            emotional_list.append(emotion)
# print(emotional_list)
num = Counter(emotional_list)
print(num)
fig, axl = plt.subplots()
axl.bar(num.keys(), num.values())
fig.autofmt_xdate()
plt.bar(num.keys(), num.values())
plt.savefig('output.png')
plt.show()
