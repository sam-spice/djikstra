#!/usr/bin/python3


from CS312Graph import *
import time
from Queues import *
import random


class NetworkRoutingSolver:
    def __init__( self, display ):
        pass



    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network



    def getShortestPath( self, destIndex ):
        self.dest = destIndex

        path_edges = []
        total_length = self.network.nodes[destIndex].dist

        node = self.network.nodes[destIndex]
        while node.prev != None:
            path_edges.append((node.loc, node.prev.loc, '{:.0f}'.format(node.dist - node.prev.dist)))
            node = node.prev
        return {'cost':total_length, 'path':path_edges}



    def computeShortestPaths( self, srcIndex, use_heap=False ):

        if use_heap:
            priority_q = HeapQueue()
        else:
            priority_q = ArrayQueue()

        self.source = srcIndex

        t1 = time.time()
        self.initialize_values()
        priority_q.make_queue(self.network.nodes)
        while not priority_q.is_empty():
            curr_node = priority_q.delete_min()
            for edge in curr_node.neighbors:
                if edge.dest.dist > (edge.src.dist + edge.length):
                    edge.dest.dist = edge.src.dist + edge.length
                    edge.dest.prev = edge.src
                    priority_q.decrease_key(edge.dest)
        t2 = time.time()

        return (t2-t1)

    def initialize_values(self):
        for node in self.network.nodes:
            node.dist = math.inf
            node.prev = None
        startNode = self.network.nodes[self.source]
        startNode.dist = 0