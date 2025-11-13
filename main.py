import csv

class DataItem:
  def __init__ (self, line):
    self.movie_name = line[0]
    self.genre = line[1]
    self.release_date = line[2]
    self.director = line[3]
    self.revenue = line[4]
    self.rating = line[5]
    self.min_duration = line[6]
    self.production_company = line[7]
    self.quote = line[8]
    pass 

def Main():

  file = "MOCK_DATA.csv"
  counter = 0

  with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if(counter == 0): # dont read in the line of labels
        continue
      # create a data item from row
      # feed the appropriate field into the hash function to get a key
      # mod the key value by the hash table length
      # try to insert DataItem into hash table
      # handle any collisions
      count += 1

if __name__ == "__main__":
    main()
