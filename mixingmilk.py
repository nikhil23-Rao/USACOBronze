def main():
    i1 = input("")
    i2 = input("")
    i3 = input("")
    bucket1 = i1.split(" ")
    bucket2 = i2.split(" ")
    bucket3 = i3.split(" ")
    bucket1 = [int(i) for i in bucket1]
    bucket2 = [int(i) for i in bucket2]
    bucket3 = [int(i) for i in bucket3]
    for i in range(1, 101):
        if ((i-1) % 3 == 0):
            if ((bucket2[0] - bucket2[1]) >= bucket1[1]):
                bucket2 = [bucket2[0], bucket1[1] + bucket2[1]]
                bucket1 = [bucket1[0], 0]
            else:
                bucket1 = [bucket1[0], bucket1[1] - (bucket2[0] - bucket2[1])]
                bucket2 = [bucket2[0], bucket2[0]]
        if ((i-2) % 3 == 0):
            if ((bucket3[0] - bucket3[1]) >= bucket2[1]):
                bucket3 = [bucket2[0], bucket2[1] + bucket3[1]]
                bucket2 = [bucket1[0], 0]
            else:
                bucket2 = [bucket2[0], bucket2[1] - (bucket3[0] - bucket3[1])]
                bucket3 = [bucket3[0], bucket3[0]]
        if ((i-3) % 3 == 0):
            if ((bucket1[0] - bucket1[1]) >= bucket3[1]):
                bucket1 = [bucket3[0], bucket1[1] + bucket3[1]]
                bucket3 = [bucket3[0], 0]
            else:
                bucket3 = [bucket3[0], bucket3[1] - (bucket1[0] - bucket1[1])]
                bucket1 = [bucket1[0], bucket1[0]]

    return [bucket1[1], bucket2[1], bucket3[1]]


res = main()
print(res)
