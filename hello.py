from py2neo import Graph



graph = Graph("http://neo4j:admin@localhost:7474/db/data/")


#print graph.order
#results = graph.cypher.execute("CREATE (a:Person {name:{N}})", {"N": "Ash"})
results = graph.cypher.execute("MATCH (a:Person) RETURN a")
#results = graph.find('Person','name','Ash')
print results
	
#print type(results)