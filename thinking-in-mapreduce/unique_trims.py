import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: id
    # value: string
    key = record[0]
    value = record[1]
    value_trimmed = value[:-10]
    mr.emit_intermediate(value_trimmed, 1)

def reducer(key, list_of_values):
    # key: trimmed nucleotide
    # value: list of counts
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)