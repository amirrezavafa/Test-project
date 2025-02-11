def is_eligible_for_discount(age, membership, purchase_amount, is_student, has_referred_friends):
    """
    Determines if a customer is eligible for a discount.
    
    Parameters:
    age (int): The age of the customer.
    membership (str): The type of membership ('standard', 'premium').
    purchase_amount (float): The total purchase amount.
    is_student (bool): Indicates if the customer is a student.
    has_referred_friends (bool): Indicates if the customer has referred friends.
    
    Returns:
    bool: True if eligible for discount, False otherwise.
    """
    if ((age >= 18) and (membership == 'premium')) or \
       ((purchase_amount >= 100) and (age < 65)) or \
       ((is_student) or (has_referred_friends)):
        return True
    else:
        return False
