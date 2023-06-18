# QA = Question and Answer dictionary from Database (key and value are in string format)
# inp = input from the user in string format
def closests_match(QA, inp):
    inp = inp.strip().split()
    for i in range(len(inp)):
        # Converting input to lower case
        inp[i] = inp[i].lower()
    # Creating a dictionary to store value to match closest question
    d = {key: 0 for key in QA.values()}
    for j in d.keys():
        count = 0
        for i in inp:
            if i in j:
                count += 1
        d[j] = count
    large = 0
    question = ""
    for (key, value) in d.items():
        if value > large:
            large = value
            question = key
    if large == 0:
        # It will return False if the Question entered (input ) does not exist
        # Tuple with False , input
        return ((False, inp))
    else:
        # It will return True and the answer to the question (Input) closest match
        return display(QA, question)


def display(QA, question):
    for (key, value) in QA.items():
        if (value == question):
            return ((True, key))


# Debugging
'''
QA = {"Reva University": "what is your name",
      "Hi, I am mercury bot": "who are you"}
print(closests_match(QA, input("Enter your question :")))
'''

# main file calling function sting_match
# Template
'''
key, value = closests_match(QA, inp)
if ( value == True)
    print(key)
else:
'''
