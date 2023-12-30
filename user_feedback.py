```python
# user_feedback.py

def provide_feedback(user_id, transaction_id, success):
    """
    Provide feedback to the user about the status of their transaction.

    Parameters:
    user_id (str): The ID of the user making the payment.
    transaction_id (str): The ID of the transaction to provide feedback for.
    success (bool): Whether the transaction was successful or not.

    Returns:
    str: A message to the user about the status of their transaction.
    """

    if success:
        return f"Transaction {transaction_id} from user {user_id} was successful. Thank you for your payment."
    else:
        return f"Transaction {transaction_id} from user {user_id} failed. Please try again or contact support if the problem persists."
```
