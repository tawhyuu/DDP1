def fibo(n, a, b):
 
    if (n > 0):
 
        # Function call
        fibo(n - 1, b, a + b)
 
        # Print the result
        print(a, end=" ")
 
 
# # Driver Code
# if __name__ == "__main__":
 
#     N = 10
#     fibo(N, 0, 1)

def print_space(space):
     
    # base case
    if (space == 0):
        return
    print(" ", end = "")
 
    # recursively calling print_space()
    print_space(space - 1)
 
# function to print asterisks
def print_asterisk(asterisk):
     
    # base case
    if(asterisk == 0):
        return
    print("* ", end = "")
 
    # recursively calling asterisk()
    print_asterisk(asterisk - 1)
 
# function to print the pattern
def pattern(n, num):
     
    # base case
    if (n == 0):
        return
    print_space(n - 1)
    print_asterisk(num - n + 1)
    print("")
 
    # recursively calling pattern()
    pattern(n - 1, num)
 
# Driver Code
n = 5
pattern(n, n)

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
N = 3

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')