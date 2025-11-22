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

def hashKey(key, size):
  num = 0
  length = len(key)
  for i in range(length):
    num = num + (ord(key[i]) * (31 ** (length - i - 1)))
  return num % size

def hashName(file, hash_table):
  counter = 0
  unused_bucket = 0
  collision_count = 0


  with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    size = sum(1 for row in reader) - 1 # get number of lines in file for hash table size
    unused_bucket = size
    hash_table = [[] for _ in range(size)] # initialize hash table with no values
    csvfile.seek(0) # reset file read position to beginning
    for row in reader:
      if(counter == 0): # dont read in the line of labels
        counter += 1
        continue

      # create a data item from row
      data = DataItem(row)
    
      # feed the appropriate field into the hash function to get a key
      # mod the key value by the hash table length
      key = hashKey(data.movie_name, size)
      # try to insert DataItem into hash table
      if(hash_table[key] == []): # if bucket is empty
        unused_bucket -= 1
        hash_table[key] = [data]
      else:
        hash_table[key].append(data)
        collision_count += 1
      # handle any collisions
      counter += 1

  return unused_bucket, collision_count

def hashQuote(file, hash_table):
  counter = 0
  unused_bucket = 0
  collision_count = 0


  with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    size = sum(1 for row in reader) - 1 # get number of lines in file for hash table size
    unused_bucket = size
    hash_table = [[] for _ in range(size)] # initialize hash table with no values
    csvfile.seek(0) # reset file read position to beginning
    for row in reader:
      if(counter == 0): # dont read in the line of labels
        counter += 1
        continue

      # create a data item from row
      data = DataItem(row)
    
      # feed the appropriate field into the hash function to get a key
      # mod the key value by the hash table length
      key = hashKey(data.quote, size)
      # try to insert DataItem into hash table
      if(hash_table[key] == []): # if bucket is empty
        unused_bucket -= 1
        hash_table[key] = [data]
      else:
        hash_table[key].append(data)
        collision_count += 1
      # handle any collisions
      counter += 1

  return unused_bucket, collision_count

def main():

  file = "MOCK_DATA.csv"
  hash_table1 = []

  start = time.time() # start timer
  unused_bucket1, collision_count1 = hashName(file, hash_table1)
  end = time.time() # end timer
  programTime1 = end - start
  
  hash_table2 = []

  start = time.time() # start timer
  unused_bucket2, collision_count2 = hashQuote(file, hash_table2)
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
