from fractions import Fraction

def probability_of_sum(target_sum):
    favorable_outcomes = 0
    total_outcomes = 0
    
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if die1 != die2 and die1 + die2 == target_sum:
                favorable_outcomes += 1
            total_outcomes += 1
    
    probability = Fraction(favorable_outcomes, total_outcomes)
    return probability

target_sum = 6
result = probability_of_sum(target_sum)
print(f"{result}")
