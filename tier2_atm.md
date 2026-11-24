# Tier 2: ATM Withdrawal Algorithm

## Goal
Withdraw money from an ATM.

## Steps

1. Insert ATM card.
2. Check whether the card is valid.
3. If the card is invalid, reject the card and stop.
4. Request the user's PIN.
5. Check whether the PIN is correct.
6. If the PIN is incorrect, request it again, allowing a limited number of attempts.
7. Display the available ATM options.
8. Select withdrawal.
9. Enter the amount to withdraw.
10. Check whether the amount is valid.
11. Check whether the user's account has enough money.
12. Check whether the ATM has enough cash.
13. Dispense the requested cash.
14. Update the user's account balance.
15. Return the ATM card.
16. Display a transaction confirmation.
17. End the transaction.

## Possible Problems

- Invalid card: Reject the card and stop.
- Incorrect PIN: Allow another attempt, up to the permitted limit.
- Insufficient account balance: Cancel the withdrawal.
- Insufficient ATM cash: Ask the user to enter a smaller amount or cancel.
- Failed transaction: Do not deduct money unless the withdrawal is successfully completed.

## Completion Condition

The transaction is complete when the cash is dispensed, the account is correctly updated, and the card is returned.