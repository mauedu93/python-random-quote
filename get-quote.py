def primary():
  # print("Keep it logically awesome.")
  #
  # with open("quotes.txt", 'a') as f:
  #    f.write("Ain't no mountain high enough\n")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  # print(quotes[-1][:-1])
#
#
  for n in range(10):
      print(quotes[n][:-1])
#
if __name__== "__main__":
  primary()
