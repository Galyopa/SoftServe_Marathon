"""Nicky and Dev work in a company where each member is given his income in the form of points. On Nicky's birthday, Dev decided to give some of his points as a gift. The number of points Dev is gifting is the total number of visible zeros visible in the string representation of the N points he received this month.

Let's say that Nicky got M points from Dev. By the company law, if M is even and greater than 0, Nicky must give one point to the company. If M is odd, the company gives Nicky one additional point.

Given the number of points N Dev received this month, calculate the number of points Nicky will receive as a gift and return this number in its binary form.

Note: visible zeros are calculated as follows:

0, 6 and 9 contain 1 visible zero each;
8 contains 2 visible zeros;
other digits do not contain visible zeros.
Example

For N = "565", the output should be
Cipher_Zeroes(N) = 10.

There's one visible zero in "565". Since one is odd, the company will give an additional point, so Nicky will receive 2 points.
210 = 102, so the output should be 10.

Input/Output

[input] string N

The number of points Dev received this month.

Constraints:
1 ≤ N ≤ 101000.

[output] integer

The number of points Nicky will receive in the binary representation.
"""

def Cipher_Zeroes(N):
    d = { '0': 1, '6': 1, '9': 1, '8': 2}
    count = sum(d.get(x, 0) for x in N)
    if count == 0:
        return '0'
    if count % 2 == 1:
        count += 1
    else:
        count -= 1
    # res = ''
    # while count > 0:
    #     res = ('0' if count % 2 == 0 else '1') + res
    #     count //= 2
    return int(bin(count)[2:])


print(Cipher_Zeroes("565"))

print(Cipher_Zeroes("8200"))

print(Cipher_Zeroes("4900"))

print(Cipher_Zeroes("7481"))

print(Cipher_Zeroes("4"))

print(Cipher_Zeroes("0"))

print(Cipher_Zeroes("2628426728"))