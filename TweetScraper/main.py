import Classifier
import os
os.system("pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git")
while True:
  user = input("User: ")
  allign = input("Allignment: ")
  Classifier.classify(user,"300",allign)
