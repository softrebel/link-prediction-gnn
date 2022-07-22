import pandas as pd
from stellargraph import StellarGraph
import networkx as nx
def load_twitter_graph():
    with open('ego-twitter/out.ego-twitter','r') as f:
        edges=[x.strip().split('\t') for x in f.readlines()[2:]]

    df = pd.DataFrame(
        edges,columns=['source','target']
    )
    nodes=[x[0] for x in edges]
    nodes.extend([x[1] for x in edges])
    node_count=len(set(nodes))
    graph = StellarGraph(edges=df,node_features=node_data)
    return graph


def load_twitter_graph_with_feature():
    with open('ego-twitter/out.ego-twitter','r') as f:
        edges=[x.strip().split('\t') for x in f.readlines()[2:]]

    G = nx.from_edgelist(edges)
    d=pd.DataFrame(range(G.number_of_nodes()),index=G.nodes)
    node_data=pd.get_dummies(d[0])
    graph = StellarGraph(G, node_features=node_data)
    return graph


if __name__ == '__main__':
    load_twitter_graph()

