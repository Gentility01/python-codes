# # dictionary can be used to store values together

# # report = {
# #     "name": "amaka",
# #     "school" : "abia poly",
# #     "age" : 30
# # }
# # print(report)
# # print(report["school"])
# # print(report.get("name"))
# # report ["datebirth"] = 1950
# # print(report)

# # number = input("enter a number: ")
# # dictionary = {
# #     "1" : "one",
# #     "2" : "two",
# #     "3" : "three",
# #     "4" : "four",
# #     "5" : "five",
# #     "5" : "five",
# #     "6" : "six",
# #     "7" : "seven",
# #     "8" : "eight",
# #     "9" : "nine",
# #     "0" : "zero"
# # }
# # output = ""


# # for cha in number:
# #     output += dictionary.get(cha, "!")+", "
# # print(output) 

# finds = input("enter a word: ")

# words = {
#     "man" : "a male human being",
#     "woman" : "a female human being",
#     "noun": "a name of a person animal place or thing",
#     "car" : "a technology for transport"
# }

# output = ""

# # if finds == "man":
# #     print(words.get("man"))
# # if finds == "woman":
# #     print(words["woman"])    

# for mapout in finds:
#     output += words.get(finds, f"{finds} not found in dictionary") + ", "
#     break
# print(output)

start_game = input("enter a command >>> ")
game = {
    "help" : """
start -> to start.
stop -> to stop.
quit -> to quit.
    """,
    "start" : "your car is started",
    "stop" : "your car have stoped",
}
output = ""

for fact in start_game:
    output += game.get(start_game, "!")
    break

print(output)    


