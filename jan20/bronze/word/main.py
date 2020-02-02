def readInput():
  f = open("word.in")
  data = f.readlines()
  f.close()
  numWords, maxLength = data[0].split()
  return int(maxLength), data[1].split()

def main(maxLength, words):
  result = ""
  curLength = 0
  i = 0

  while i < len(words):
    word = words[i]
    # calculates a possible space if we include next char
    posLength = curLength + len(word)

    # would wrap around, so reset
    if posLength > maxLength:
      result += "\n" + word
      curLength = len(word)
    else:
      # otherwise, was less than maxLength, so attempt to write
      if curLength == 0:
        result += word
        curLength += len(word)
      else:
        result += " " + word
        curLength += len(word)
      
    i += 1
  return result

def output():
  f = open("word.out", "w+")
  maxLength, words = readInput()
  f.write(str(main(maxLength, words)) + "\n")
  f.close()

output()
  