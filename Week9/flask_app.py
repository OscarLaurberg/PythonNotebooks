#!flask/bin/python
from flask import Flask, jsonify, abort, request
import random as rand
import networkx as nx
from networkx.readwrite import json_graph
import json



app = Flask(__name__)

#return jsonify({'Python': [dict(row) for row in python]})
@app.route('/wiki/RandomNodes', methods=['GET'])
def randomNode():
    G = nx.read_edgelist('../downloads/wiki-vote.txt')
    randomNumber = rand.choice(list(G.nodes))

    data1 = json.dumps(json_graph.node_link_data(G.subgraph(G[randomNumber])))
    data = json.loads(data1)
    print(data)
    #neighborNodes = list(G.neighbors(randomNumber)))
    nn = list(G.neighbors(randomNumber))
    json_nn = json.dumps(nn)
    #data.append(json_nn)
    #data.update(nn)
    #data.update(json_nn)
    #neighborNodes = json.dumps(json_graph.node_link_data(list(nn)))
    #print(neighborNodes)

    return json.dumps(data)


@app.route('/wiki/hello', methods=['GET'])
def hello_worldy():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

