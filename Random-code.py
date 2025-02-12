import random
from is_eligible_for_discount import is_eligible_for_discount

for _ in range(20):
    age = random.randint(10, 80)
    membership = random.choice(['standard', 'premium'])
    purchase_amount = random.uniform(0, 200)
    is_student = random.choice([True, False])
    has_referred_friends = random.choice([True, False])

    result = is_eligible_for_discount(age, membership, purchase_amount, is_student, has_referred_friends)
    print(f"Test: ({age}, {membership}, {purchase_amount:.2f}, {is_student}, {has_referred_friends}) → {result}")
