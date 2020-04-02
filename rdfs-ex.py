# Answer RDFS exercise

u = Graph()
v = Graph()
d = Graph()

u.parse('rdfs.ttl', format='turtle')
v.parse('rdfs.ttl', format='turtle')

DeductiveClosure(RDFS_Semantics).expand(v)
d = v - u

print("RDFS inference generated additional {} triples".format(len(d)))

for s,p,o in sorted(g.triples((None,None,None))):
    print(s,p,o)