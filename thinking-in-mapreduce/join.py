import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: whole record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of records
    total = []
    for v in list_of_values:
        if v[0] == "order":
            for v2 in list_of_values:
                if v2[0] == "line_item":
                    for e in v:
                        total.append(e)
                    for e2 in v2:
                        total.append(e2)
                    mr.emit(total)
                    total = []

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
