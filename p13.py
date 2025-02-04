'''f = open("input.txt",'w')
def copy(datafile1,datafile2):
     try:
          f1 = open(datafile1,'r')
          f2 = open(datafile2,'w')
          for line in f1:
               f2.write(line.rstrip("\n")+"\n")
          f1.close()
          f2.close()
          print(f"Content of {datafile1} has successfully copied to {datafile2}")
     except FileNotFoundError:
          print("File not found")
copy("input.txt","output.txt")'''

'''f1 = open("example.txt",'w')
f1.write("monali dash")
f1.close()
def count(file1):
     try:
          f1 = open(file1,'r')
          text = f1.read()
          words = text.split()
          num_words = len(words)
          vowels = 'aeiouAEIOU'
          num_vowels = 0
          for char in text:
               if char in vowels:
                  num_vowels +=1
          print(f"Number of words in {file1}: {num_words}")
          print(f"Number of vowels in {file1}: {num_vowels}")
     except FileNotFoundError:
          print("File not found")
count("example.txt")'''

'''f = open("output.txt",'w')
def storedinput(file1):
     try:
           f1 = open (file1,'w')
           print("Enter text to store input in file")
           while True:
              userinput = input("Enter your text: ")
              if userinput.strip()=="":
                  break
              f1.write(userinput.upper()+"\n")
           print(f"All the input has saved in {file1}")
     except:
          print("File not found")
storedinput("output.txt")'''

f = open("file1.txt",'w')
def copylines(file1, file2):
    try:
        f1=open(file1, 'r')
        f2=open(file2, 'w')
        line_number = 1
        for line in f1:
          if line_number % 2 != 0:
            f2.write(line)
            line_number += 1
        print(f"Alternate lines copied successfully from {file1} to {file2}.")
    except FileNotFoundError:
        print("Error: One of the files was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copylines('file1.txt', 'file2.txt')

  
   

          
