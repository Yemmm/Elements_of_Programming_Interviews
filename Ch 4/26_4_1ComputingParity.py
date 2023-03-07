def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1

        x &= x - 1
    return result

n = int(input("The word given by the user is: "))
print(parity(n))


#Question
'''
In Python, you can compute the parity of an integer by counting the number of 1 bits in its binary representation and checking if that count is odd or even. Here’s an example function that computes the parity of an integer x:

def parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
This function uses a loop to iterate over the bits of x from right to left. In each iteration, it uses the bitwise AND operator & to extract the least significant bit of x, and the bitwise XOR operator ^= to update the parity result. Finally, it uses the right shift operator >>= to shift x to the right by 1 bit, discarding the least significant bit.

For example, to compute the parity of the integer 5 (which is 101 in binary), you can call the parity function like this:

x = 5
print(f"parity({x}) = {parity(x)}")
This code would output:

parity(5) = 0
indicating that the parity of 5 is 0 (even).
'''

#Space and Time for above commented example
'''
The time complexity of the parity function is O(log(x)), where x is the input integer. This is because the function uses a loop that iterates once for each bit in the binary representation of x, and the number of bits in x is log2(x) + 1. In each iteration, the function performs a constant number of bitwise operations, so the total time complexity is O(log(x)).

The space complexity of the parity function is O(1), because it uses a constant amount of memory to store the result and x variables, regardless of the size of the input integer.
'''