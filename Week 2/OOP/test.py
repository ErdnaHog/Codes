class Counter:
    count1 = 0
    def __init__(self):
        self.count2 = 0

c = Counter()

Counter.count1 += 5
print(Counter.count1)
c.count1 += 5
print(c.count1)
