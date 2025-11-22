import csv, time

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

def hash(key, size):
  num = 0
  for char in key:
    num += ord(char)
  return num % size


def main():

  file = "MOCK_DATA.csv"
  counter1 = 0
  hash_table1 = []
  unused_bucket1 = 0
  collision_count1 = 0

  start = time.time() # start timer
  with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    size = sum(1 for row in reader) - 1 # get number of lines in file for hash table size
    unused_bucket1 = size
    hash_table1 = [[] for _ in range(size)] # initialize hash table with no values
    csvfile.seek(0) # reset file read position to beginning
    for row in reader:
      if(counter1 == 0): # dont read in the line of labels
        counter1 += 1
        continue

      # create a data item from row
      data = DataItem(row)
    
      # feed the appropriate field into the hash function to get a key
      # mod the key value by the hash table length
      key = hash(data.movie_name, size)
      # try to insert DataItem into hash table
      if(hash_table1[key] == []): # if bucket is empty
        unused_bucket1 -= 1
        hash_table1[key] = [data]
      else:
        hash_table1[key].append(data)
        collision_count1 += 1
      # handle any collisions
      counter1 += 1

  end = time.time() # end timer
  programTime1 = end - start

  counter2 = 0
  hash_table2 = []
  unused_bucket2 = 0
  collision_count2 = 0

  start = time.time() # start timer
  with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    size = sum(1 for row in reader) - 1 # get number of lines in file for hash table size
    unused_bucket2 = size
    hash_table2 = [[] for _ in range(size)] # initialize hash table with no values
    csvfile.seek(0) # reset file read position to beginning
    for row in reader:
      if(counter2 == 0): # dont read in the line of labels
        counter2 += 1
        continue

      # create a data item from row
      data = DataItem(row)
    
      # feed the appropriate field into the hash function to get a key
      # mod the key value by the hash table length
      key = hash(data.quote, size)
      # try to insert DataItem into hash table
      if(hash_table2[key] == []): # if bucket is empty
        unused_bucket2 -= 1
        hash_table2[key] = [data]
      else:
        hash_table2[key].append(data)
        collision_count2 += 1
      # handle any collisions
      counter2 += 1

  end = time.time() # end timer
  programTime2 = end - start

  print("Hash Table 1 Results (Movie Title as Key):")
  print(f"Time taken to insert items: {programTime1:0.2f} seconds")
  print(f"Number of unused buckets: {unused_bucket1}")
  print(f"Number of collisions: {collision_count1}")

  print("Hash Table 2 Results (Movie Quote as Key):")
  print(f"Time taken to insert items: {programTime2:0.2f} seconds")
  print(f"Number of unused buckets: {unused_bucket2}")
  print(f"Number of collisions: {collision_count2}")

if __name__ == "__main__":
    main()
