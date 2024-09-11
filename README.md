1. ### Getting User Input
The program starts by asking the user for their name and three favorite numbers. It stores these inputs for further operations.<br>
```python 
user_name = str(input("Enter you name: "))
print(f"Hello {user_name}! Let's explore your favorite numbers ")

num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
```
stored_numbers = [num1, num2, num3]

- The program captures the user's name and stores it as a string.
- Then, it asks for three favorite numbers and stores them as integers in the list **stored_numbers**.

2. ### Checking if Numbers are Even or Odd
Next, the code checks whether each stored number is even or odd and stores the result.
```python 
even_odd_info = []
for num in stored_numbers:
    if num % 2 == 0:
        even_odd_info.append((num, "even."))
    else:
        even_odd_info.append((num, "odd."))
```
- It iterates over the list of favorite numbers **(stored_numbers)**.
- For each number, it checks if it's even (num % 2 == 0) or odd.
- The result is appended to the **even_odd_info** list as a tuple containing the number and its classification (**"even" or "odd")**.

3. ### Displaying Even/Odd Results
Now, the program prints whether each of the favorite numbers is even or odd.
```python 
for num, info in even_odd_info:
    print(f"The Number {num} is {info}")
```
- This loop goes through the **even_odd_info** list and displays the even/odd information for each number in a friendly format.

4. ### Squaring the Stored Numbers
The next step involves calculating and displaying the square of each favorite number.
```python
 for num in stored_numbers:
    square = num * num
    print(f"The Number {num} and its square: {num, square}")
```
- For each number in **stored_numbers**, the program computes its square **(num * num)**.
- It then prints the original number alongside its square.

5. ### Summing the Stored Numbers
The program calculates and prints the sum of the favorite numbers using Python’s built-in sum() function.
```python
sum_of_numbers = sum(stored_numbers)
print(f"Amazing ! The sum of your favorite numbers is: {sum_of_numbers}")

```
- It computes the sum of all three numbers in **stored_numbers**.
- The result is printed as a part of the output.

6. ### Checking if the Sum is a Prime Number
Finally, the program checks if the sum of the numbers is a prime number or not.
```python 
is_prime = True
for prime in stored_numbers:
    if prime <= 1:
        is_prime = False
    else:
        for i in range(2, prime):
            if (prime % i) == 0:
                is_prime = False
                break
```
- If the sum is less than or equal to 1, it's not prime.
- Otherwise, it checks for factors other than 1 and the number itself.
- If a factor is found, **is_prime** is set to **False**.

7. ### Displaying the Prime Check Result
```python 
if is_prime:
    print(f"WOW ! {sum_of_numbers} is a prime number!")
else:
    print(f"OPSSS ! {sum_of_numbers} is not a prime number, but it's still awesome!")

```
- Based on the is_prime flag, the program prints whether the sum is prime or not.
- Either way, the result is presented in a fun way to the user!
