import rdflib

with open('teacherinfo.txt', 'r', encoding='utf-8') as rubro:
    documento = rubro.readlines()

GraficoFinal = rdflib.Graph()

for i in range(0, len(documento)):
    linha = documento[i]
    if (linha.split(':', 1)[0] == 'Name'):
        s = rdflib.URIRef('http://baike.com/resource/' + linha.split(':', 1)[1].replace(" ", ""))
        for j in range((i + 1), len(documento)):
            line = documento[j]
            if (line.split(':', 1)[0] == 'Name'):
                break
            p = rdflib.URIRef('http://baike.com/resource/' + line.split(':', 1)[0].replace(" ", ""))
            o = rdflib.URIRef('http://baike.com/resource/' + line.split(':', 1)[1].replace(" ", ""))
            GraficoFinal.add((s, p, o))

GraficoFinal.serialize('final.rdf')
