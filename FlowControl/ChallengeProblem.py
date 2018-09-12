ip = input("Enter your IP address: ")
segments = int(1)
segmentLength = int(0)
# i = ""

if ip[-1] != ".":
    ip += "."

for i in ip:
    if i == ".":
        print("Segment {0} is {1} numbers long".format(segments, segmentLength))
        segments += 1
        segmentLength = 0
    else:
        segmentLength += 1

# if i != ".":
#     print("Segment {0} is {1} numbers long".format(segments, segmentLength))
