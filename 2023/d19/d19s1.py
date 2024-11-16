
input_file = "d19/input.txt"

with open(input_file, "r") as data:
    lines = data.readlines()

# parse input file
inputSplit = lines.index("\n")
workflowStrings = [line.strip('\n') for line in lines[:inputSplit]]
partStrings = [line.strip('\n') for line in lines[inputSplit+1:]]


# make dictionary of lambdas
workflows = {str: list}
for workflow in workflowStrings:
    name = workflow.split('{')[0]
    workflows[name] = []
    rules = workflow.split('{')[1].strip('}').split(',')
    for rule in rules:
        if ':' in rule:
            para = "x,m,a,s"
            cond = rule.split(':')[0]
            ret = rule.split(':')[1]
            ruleLambda = "lambda " + para + ": " + "\"" + ret + "\"" + " if " + cond + " else False"
            workflows[name].append(eval(ruleLambda))
        else:
            ruleLambda = "lambda " + para + ": " + "\"" + rule + "\""
            workflows[name].append(eval(ruleLambda))


acceptedPartSum = 0
# pass each part through workflows to completion, sum as needed
for line in partStrings:
    x,m,a,s = [int(entry[2:]) for entry in line.strip("{}").split(',')]
    tag = "in"
    rejected = False
    accepted = False
    while not (rejected or accepted):
        for func in workflows[tag]:
            if func(x,m,a,s):
                if func(x,m,a,s) == "R":
                    rejected = True
                elif func(x,m,a,s) == "A":
                    accepted = True
                else:
                    tag = func(x,m,a,s)
                break

    if accepted:
        acceptedPartSum += sum([x,m,a,s])

print("what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?", acceptedPartSum)