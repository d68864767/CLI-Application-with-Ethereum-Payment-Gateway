```python
# payment_verification.py

import web3
from web3 import Web3
from config import ETH_WALLET_ADDRESS, ETH_WALLET_API_KEY

# Initialize Web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + ETH_WALLET_API_KEY))

def verify_payment(user_id, transaction_id):
    """
    Verify that a payment of 1 ETH has been made by the user.

    Parameters:
    user_id (str): The ID of the user making the payment.
    transaction_id (str): The ID of the transaction to verify.

    Returns:
    bool: True if the payment is verified, False otherwise.
    """

    # Get the transaction details
    try:
        transaction = w3.eth.getTransaction(transaction_id)
    except Exception as e:
        print(f"Failed to get transaction: {e}")
        return False

    # Check that the transaction is to the correct address and for the correct amount
    if transaction['to'] == ETH_WALLET_ADDRESS and transaction['value'] == w3.toWei(1, 'ether'):
        print(f"Payment of 1 ETH from user {user_id} verified.")
        return True
    else:
        print(f"Payment verification failed for user {user_id}.")
        return False
```
