cases = int(input())
results = ["NO"] * cases
for i in range(cases):
    original = [char for char in input()]
    hashed = [char for char in input()]
    if len(original) <= len(hashed):
        #what chars and how many of them are needed to pass
        requiredChars = {}
        for char in original:
            if char in requiredChars:
                requiredChars[char] = requiredChars[char] + 1
            else:
                requiredChars[char] = 1
        currentChars = {}
        #initialize from offset = 0, then check for matches
        for index in range(len(original)):
            if hashed[index] in requiredChars:
                if hashed[index] in currentChars:
                    currentChars[hashed[index]] = currentChars[hashed[index]] + 1
                else:
                    currentChars[hashed[index]] = 1
        #go on and on until match is found or run to the end of string
        if currentChars.__eq__(requiredChars):
            results[i] = "YES"
        else:
            for offSet in range(len(hashed) - len(original)):
                if hashed[offSet] in requiredChars:
                    currentChars[hashed[offSet]] = currentChars[hashed[offSet]] - 1
                if hashed[offSet + len(original)] in requiredChars:
                    if hashed[offSet + len(original)] in currentChars:
                       currentChars[hashed[offSet + len(original)]] = currentChars[hashed[offSet + len(original)]] + 1
                    else:
                        currentChars[hashed[offSet + len(original)]] = 1
                if currentChars.__eq__(requiredChars):
                    results[i] = "YES"
                    break

for result in results:
    print(result)