import time

# Declare constants
brC = [
    ("((", "", ")", "", ")", ""),
    ("(", "(", "", "", "))", ""),
    ("(", "", ")", "(", "", ")"),
    ("", "((", "", "", ")", ")"),
    ]
ops = ["+","-","*","/"]
indexes = [0, 1, 2, 3]

# Initialization
numInput = input("\nInput integers: ")
start = time.time()

# Split the input into 4 
nums = numInput.split(" ")
if len(nums) == 4:

    # Generating all index permutations
    indexC = []
    newC = []
    for i in indexes:
        for j in indexes:
            for k in indexes:
                for l in indexes:
                    newC.append(i)
                    if (j != i):
                        newC.append(j)
                        if (k != i) and (k!= j):
                            newC.append(k)
                            if (l != i) and (l != j) and (l != k):
                                newC.append(l)
                    # If the array length is 4 and the permutation contained is not a listed index combination,
                    # add the new combination to the combination list
                    if len(newC) == 4:
                        if indexC.count(newC) == 0:
                            indexC.append(newC)
                    # Empty the generated array
                    newC = []

    # Generating and testing mathematical expressions based on bracket order,
    # index permutation, and operator combinations
    solutions = []
    nSol = 0
    for i in indexC:
        for br in brC:
            for op1 in ops:
                for op2 in ops:
                    for op3 in ops:
                        expression = br[0] + nums[i[0]] + op1 + br[1] + nums[i[1]] + br[2] + op2 + br[3] + nums[i[2]] + br[4] + op3 + nums[i[3]] + br[5]
                        # Avoiding division by zero
                        try:
                            # Calculate mathematical expression
                            if eval(expression) == 24:
                                duplicate = False
                                # Check for duplicate
                                for expr in solutions:
                                    if (expr == expression):
                                        duplicate = True
                                        break
                                if not duplicate:
                                    solutions.append(expression)
                                    print(expression)   # Printing solution expression
                                    nSol = nSol + 1     # Increasing number of solution
                        except ZeroDivisionError:
                            nSol = nSol
    # Print total number of solutions              
    print("\n" + str(nSol) + " solutions found \nin " + str(time.time() - start) + " seconds.")
else:
    print("Invalid entry.\n")