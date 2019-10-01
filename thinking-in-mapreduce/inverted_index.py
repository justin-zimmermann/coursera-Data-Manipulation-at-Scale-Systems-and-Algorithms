import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: text
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, record[0])

def reducer(key, list_of_values):
    # key: word
    # value: list of document identifiers
    deduplicated_list = []
    set_of_values = set(list_of_values)
    for v in set_of_values:
      deduplicated_list.append(v)
    mr.emit((key, deduplicated_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
