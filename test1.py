import random
sampleMassDist = (0.2, 0.1, 0.15, 0.15, 0.25, 0.15)
# assume sum of bias is 1
def roll(massDist):
    randRoll = random.random() # in [0,1]
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1

print(roll(sampleMassDist))
