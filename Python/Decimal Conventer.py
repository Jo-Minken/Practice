
def DC_Conventer(num, base, **kwargs):
    result = kwargs.get("result", [])

    d_num = "0123456789ABCDEF"
    d = num % base
    result.append(d_num[d])

    nd = num // base
    
    if nd > 0:
        DC_Conventer(nd, base, result= result)
    else:
        print("".join(reversed(result)))


DC_Conventer(10, 2)
DC_Conventer(1000, 16)
DC_Conventer(1000, 2)
