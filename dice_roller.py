import random as r
def main():
  d_r= int(input("Enter the number of time wanna roll the dice:"))
  d_s=0
  for i in range(d_r):
    roll= r.randint(1,6)
    d_s+=roll
    print('You rolled a die of {}'.format(roll))
  print("You rolled a total of {}".format(d_s))

if __name__== "__main__":
  main()