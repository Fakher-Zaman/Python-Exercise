import pickle

LIST = [10, 20, 30, 40, 50]
file = open("writeData.txt", "wb")
pickle.dump(LIST, file)
file.close
