#first : write a function in python to read the content from atext file "ABC.txt" line by line and display the same on screen
def read_and_display_file(file_path):
  with open(file_path, 'r') as file:
      for line in file:
          print(line.strip())


file_path = "ABC.txt"
read_and_display_file(file_path)

#Write a function in python to count and display the total number of words in atext file "ABC.txt"
def count_and_display_words(file_path):
  with open(file_path, 'r') as file:
          text = file.read()
          words = text.split()
          word_count = len(words)

  print(f"Total number of words: {word_count}")



file_path2= "ABC.txt"
count_and_display_words(file_path)

#write a function in python to count uppercase character in atext file "story.txt"
def count_uppercase_characters(file_path):
   uppercase_count = 0
   with open(file_path,'r') as file:
      text = file.read() 
      for char in text:
          if char.isupper():
                  uppercase_count += 1
   print(f"Total number of uppercase characters: {uppercase_count}")


file_path3= "ABC.txt"
count_uppercase_characters(file_path)


#write a function display_words() in python to read lines fron a text file "story.txt", and display those words, which are less than 4 characters

def display_words(file_path):
   with open(file_path,'r') as file:
        for line in file:
              words = line.split()
              for word in words:
                  if len(word) < 4:
                      print(word)
file_path4= "ABC.txt"
display_words(file_path)