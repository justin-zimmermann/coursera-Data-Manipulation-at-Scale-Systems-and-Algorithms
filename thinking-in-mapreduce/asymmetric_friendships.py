import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: person's friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate((record[0], record[1]), 1)
    mr.emit_intermediate((record[1], record[0]), 1)

def reducer(key, list_of_values):
    # key: friendship relation
    # value: exists (1 or 0)
    if len(list_of_values) < 2:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
