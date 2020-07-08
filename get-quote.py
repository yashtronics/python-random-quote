import random

last = 13

def start():
  print("Keep it logically awesome.")

  num = int(input("Number of quotes: "))

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for q in range (0, num):
    rnd = random.randint(0, last)
    print(quotes[rnd].rstrip())

def addquote():
  quote = input("Quote to add: ")
  f = open("quotes.txt", "w")
  f.write(quote)
  f.close()

if __name__== "__main__":
  start()
  addquote()
