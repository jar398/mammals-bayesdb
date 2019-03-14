# Hmm... not sure this is the best / right version to use...
# the newer traits_dumper script generates a csv file, not JSON,
# so this will need to be updated to work with csv input.
# Instead of json.load you'll need to do csv.reader and so on.
# Shouldn't be too hard, but it's a bit of work.

"""
  "t.eol_pk", 
  "page.page_id", 
  "page.canonical", 
  "predicate.uri", 
  "t.object_page_id", 
  "obj.uri", 
  "t.normal_measurement", 
  "normal_units.uri", 
  "t.normal_units", 
  "t.literal"
"""

import sys, csv, json

def convert(inpath, outpath):
  with open(inpath, 'r') as infile:
    j = json.load(infile)
    columns = j["columns"]
    data = j["data"]

    # Scan the data to find unique predicate URIs
    predicate_column = columns.index("predicate.name")
    predicates = set()
    for datum in data:
      uri = datum[predicate_column]
      if uri != None:
        predicates.add(uri)
      else:
        print >>sys.stderr, 'No predicate', datum
    print len(predicates)
    predicates = sorted(list(predicates))

    # Make an index of the predicates (column label to column number)
    predicate_index = {uri: i for (uri, i) in zip(predicates, range(len(predicates)))}

    # Collect traits by taxon
    page_id_column = columns.index("page.page_id")
    canonical_column = columns.index("page.canonical")
    by_page = {}
    page_id_to_canonical = {}
    for datum in data:
      id = datum[page_id_column]
      if id in by_page:
        by_page[id].append(datum)
      else:
        by_page[id] = [datum]
        page_id_to_canonical[id] = datum[canonical_column]

    value_columns = map(lambda h: columns.index(h),
                        ["t.object_page_id", 
                         "obj.name",     # or .uri
                         "t.normal_measurement", 
                         "t.literal"])

    def get_value(datum):
      for i in value_columns:
        if datum[i]:
          return datum[i]
      return None

    # Predicate URIs become the columns.
    with open(outpath, 'w') as outfile:
      writer = csv.writer(outfile)
      writer.writerow(['page_id', 'canonical'] + predicates)
      # Write traits for one page (row)
      for (page_id, datums) in by_page.items():
        stuff = [page_id, page_id_to_canonical[page_id]]
        row = stuff + [None] * len(predicates)
        for datum in datums:
          # Get predicate URI from trait record
          uri = datum[predicate_column]
          value = get_value(datum)
          if isinstance(value, unicode):
            value = value.encode('utf-8')
          ix = predicate_index.get(uri)
          if ix:
            row[ix + len(stuff)] = value
        writer.writerow(row)

convert(sys.argv[1], sys.argv[2])
