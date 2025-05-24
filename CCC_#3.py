# the first two are directions to turn

# remaining three are number of steps to take

# this leads you to the secret formula

sequences = []
sequence = 0
print("hi")

while sequence != "99999":
    sequence = input("")
    print(sequence)
    sequences.append(sequence)

direction = ""
output = ""

print(sequences)

for sequence in sequences:
    output = ""
    sum = int(sequence[0]) + int(sequence[1])
    steps = f"{sequence[2]}{sequence[3]}{sequence[4]}"
    if sum == 0:
        direction = direction
    else:
        if (sum) % 2 == 0:
            direction = "right"
        else:
            direction = "left"
    output = f"{direction} {steps}"   
    print(output)