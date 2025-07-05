Question: Meet-Up Point of Digit-Sum Sequences
You are given two positive integers, a and b.

You define a sequence for any number where the next term is calculated by adding the number to the sum of its digits. That is:

Copy
Edit
next_term(x) = x + sum_of_digits(x)
Starting with the numbers a and b, repeatedly replace the smaller number with its next term (as per the rule above), until both numbers become equal.

Return the number at which both sequences meet for the first time.


Input: a = 471, b = 480
Output: 507

Explanation:
Sequence for 471: 471 → 483 → 498 → 519 → **507** ...
Sequence for 480: 480 → 492 → **507** ...
They meet at 507.
