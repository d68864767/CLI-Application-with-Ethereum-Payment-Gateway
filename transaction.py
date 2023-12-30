```python
# transaction.py

import psycopg2
from config import DATABASE_CONFIG
from payment_verification import verify_payment

# Establish a connection to the database
try:
    conn = psycopg2.connect(
        host=DATABASE_CONFIG['host'],
        port=DATABASE_CONFIG['port'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password'],
        dbname=DATABASE_CONFIG['database']
    )
    print("Database connection successful")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

# Create a cursor object
cur = conn.cursor()

def record_transaction(user_id, transaction_id):
    """
    Record a transaction in the database.

    Parameters:
    user_id (str): The ID of the user making the payment.
    transaction_id (str): The ID of the transaction to record.

    Returns:
    bool: True if the transaction was recorded successfully, False otherwise.
    """

    # Verify the payment
    if not verify_payment(user_id, transaction_id):
        return False

    # Record the transaction
    try:
        cur.execute("""
            INSERT INTO transactions (user_id, transaction_id, amount)
            VALUES (%s, %s, %s)
        """, (user_id, transaction_id, 1))
        print(f"Transaction {transaction_id} from user {user_id} recorded.")
        return True
    except Exception as e:
        print(f"Failed to record transaction: {e}")
        return False

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
```
