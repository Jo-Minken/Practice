"""
　　　　0C0
　　　1C0 1C1
　　2C0 2C1 2C2
　3C0 3C1 3C2 3C3
4C0 4C1 4C2 4C3 4C4

"""

def p_triangle(level):
    row = []

    for i in range(level):
        prev_row = row
        row =[]

        for j in range(i+1):
            if j in [0, i]:
                row.append(1)
            else:
                row.append(prev_row[j-1] + prev_row[j])
        
        print_blank = " " * (level - i - 1)
        output = (print_blank, " ".join([ str(item) for item in row]), print_blank)
        print("".join(output))

p_triangle(15)

"""
Formula: 

rC0 = 1
rCn = rCn-1 * (r - n + 1) / n
"""