user_name = str(input("Enter you name: "))
print(f"Hello {user_name}! Let's explore your favorite numbers ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

stored_numbers = [num1,num2,num3]

#checking if numbers are even or odd
even_odd_info =[]
for num in stored_numbers:
        if num % 2 == 0:
            even_odd_info.append((num, "even."))
        else:
            even_odd_info.append((num, "odd."))
    

#displaying even/ odd numbers
for num, info in even_odd_info:
        print(f"The Number {num} is {info}")

#squaring the stored numbers 
for num in stored_numbers:
    square = num * num
    print(f"The Number {num} and its square: {num,square}")


#printing the sum of stored numbers

sum_of_numbers = sum(stored_numbers) #used sum pre defined function
print(f"Amazing ! The sum of your favorite numbers is: {sum_of_numbers}" )

#checking if the stored numbers are prime or not
is_prime = True
for prime in stored_numbers:
      if prime <= 1:
        is_prime = False
      else:
            for i in range(2, prime):
                if (prime % i) == 0:
                    is_prime = False
                    break

if is_prime:
    print(f"WOW ! {sum_of_numbers} is a prime number!")
else:
    print(f"OPSSS ! {sum_of_numbers} is not a prime number, but it's still awesome!")
        
         