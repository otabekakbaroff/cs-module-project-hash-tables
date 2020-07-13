def word_count(s):
  s=s.lower()
  words=s.split()
  counts={}
  for i in range(len(words)):
    if words[i] in counts:
      counts[words[i]]=counts[words[i]]+1
    else:
      counts[words[i]]=1
  return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))