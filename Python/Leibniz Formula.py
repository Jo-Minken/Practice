"""
The program should take a number as argument to define how many times to do the calculation, for instance, if the argument equals to 5, the calculation should looks like below:

pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...

return the pi value calculated by this formula, compare with the accurate pi value by changing input value.
"""

def leibniz_pi(n):
    pi_sum = 0
    for i in range(n):
        if i % 2 == 0:
            pi_sum += 4/(2*i+1)
        else:
            pi_sum -= 4/(2*i+1)

        # denominator = sign = 1
        # pi += 4/denominator*sign
        # denominator += 2
        # sign *= -1

    print("n = {}, Pi = {}".format(n, pi_sum))

leibniz_pi(1)
leibniz_pi(5)
leibniz_pi(1000000)