base = {"(":0, ")":0, "[":0, "]":0, "{":0, "}":0}
test = "()0"
for i in test:
    if i in base:
        print("i in base:", i)
    else:
        print("not")