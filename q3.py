# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE
with open('romeo_and_juliet.txt', 'r') as file: 
  file_content = file.read()
####

# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE
print(file_content.count("Juliet"))
####
