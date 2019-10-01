import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    row = record[1]
    column = record[2]
    value = record[3]
    if matrix == 'a':
        for column in range(5):
            mr.emit_intermediate((row, column), record)
    if matrix == 'b':
        for row in range(5):
            mr.emit_intermediate((row, column), record)

def reducer(key, list_of_values):
    # key: row, column tuple
    # value: record
    value = 0
    for v in list_of_values:
      if v[0] == 'a':
          for v2 in list_of_values:
              if v2[0] == 'b' and v2[1] == v[2]:
                  value += v[3] * v2[3]
    mr.emit(key + (value,))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)