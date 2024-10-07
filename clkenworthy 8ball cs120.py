# Chris Kenworthy, Magic 8Ball. 9/6
# Give random module
import random
# Decide what fortunes should be used
fortunes = ["yes", "no", "it's probable..","don't even think about it", "go all in", "don't count on it", "i'm not so sure...", "definitely", "without a doubt", "with many doubts"];
# Present options
print("""What will you do?
1: Get fortune list
2: Pick a fortune
3: Have your fate decided...
""")
choice = input("Make a decision. 1, 2, or 3? ")
    
if choice == "1":
    print("FORTUNES:")
    for i, value in enumerate(fortunes):
        print(f"{i}) {fortunes[i]}")
elif choice == "2":
    number = int(input("Which fortune would you like? (0-9) "))
    for b, value in enumerate(fortunes):
        if b == number:
            print(f"{fortunes[b]}")
elif choice == "3":
    predict = input("Ask me a question.. ")
    magic = random.randint(0, 9)
    for c, value in enumerate(fortunes):
        if c == magic:
            print(f"{fortunes[c]}")
else:
    print("Uh..not exactly sure where to go from here...")