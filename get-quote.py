def primary():
  # print("Keep it logically awesome.")
  #
  # with open("quotes.txt", 'a') as f:
  #    f.write("Ain't no mountain high enough\n")

  f = open("quotes.txt")
  quotes = f.read(100)
  f.close()
#
#
  print(quotes)
#
if __name__== "__main__":
  primary()
