import pytest
from is_eligible_for_discount import is_eligible_for_discount

# داده‌های تولید شده توسط LLM به صورت لیست
test_cases = [
    (18, 'premium', 50, False, False, True),   # تست شرط اول (membership == 'premium' ∧ age >= 18)
    (17, 'premium', 50, False, False, False),  # تست شرط age >= 18 به عنوان false
    (18, 'standard', 50, False, False, False), # تست membership == 'premium' به عنوان false
    (25, 'standard', 100, False, False, True), # تست شرط دوم (purchase_amount >= 100 ∧ age < 65)
    (70, 'standard', 100, False, False, False),# تست شرط دوم با age < 65 به عنوان false
    (25, 'standard', 99, False, False, False), # تست purchase_amount >= 100 به عنوان false
    (25, 'standard', 50, True, False, True),   # تست شرط سوم (is_student == True)
    (25, 'standard', 50, False, True, True),   # تست has_referred_friends == True
    (25, 'standard', 50, False, False, False), # تست (is_student == False) ∧ (has_referred_friends == False)
    (18, 'premium', 100, True, True, True),    # تستی که همه شرایط را شامل شود
    (17, 'standard', 99, False, False, False), # تست مقادیر حداقلی
    (65, 'standard', 100, False, False, False) # تست مقدار مرزی برای age == 65
]

@pytest.mark.parametrize("age, membership, purchase_amount, is_student, has_referred_friends, expected", test_cases)
def test_is_eligible_for_discount(age, membership, purchase_amount, is_student, has_referred_friends, expected):
    assert is_eligible_for_discount(age, membership, purchase_amount, is_student, has_referred_friends) == expected
