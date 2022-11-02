# handshake.py


# Function
def handshakes(n):
  # Bonus
  if not isinstance(n, int):
    raise TypeError("Integers only")
  if n < 1:
    raise ValueError("Positive integers only")
  
  if n < 2:
    return 0
  return n - 1 + handshakes(n-1)


# Main program
people = int(input("Enter a natural number of people: "))
h = handshakes(people)
print(h, "handshakes were exchanged.")