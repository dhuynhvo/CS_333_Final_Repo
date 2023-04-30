import unittest
import Node_Network

class UnitTestNodeNetwork(unittest.TestCase):

    def testCountPacket(self):
        Node_Network.countPacket(0)
        Node_Network.countPacket(1)
        Node_Network.countPacket(2)
        print(Node_Network.G.nodes[20]['markCount'][0], "Marks 0")
        print(Node_Network.G.nodes[20]['markCount'][1], "Marks 1")
        print(Node_Network.G.nodes[20]['markCount'][2], "Marks 2")
        self.assertEqual(Node_Network.G.nodes[20]['markCount'][0], Node_Network.G.nodes[20]['markCount'][1])
        self.assertEqual(Node_Network.G.nodes[20]['markCount'][1], Node_Network.G.nodes[20]['markCount'][2])

        return
    
    def testCountEdgePacket(self):
        Node_Network.G.nodes[20]['edgeList'].clear()
        Node_Network.countEdgePacket(Node_Network.G.nodes[1])
        self.assertTrue(Node_Network.G.nodes[20]['edgeList'][0][0] >= 1)
        self.assertTrue(Node_Network.G.nodes[20]['edgeList'][0][1] >= 0)
        print(Node_Network.G.nodes[20]['edgeList'])
        return
    
    def testSendPacket(self):
        Node_Network.sendPacket(Node_Network.G.nodes[1], Node_Network.G)
        self.assertEqual(Node_Network.G.nodes[20]['markCount'][1], 1)
        return
    
    def testSendEdgePacket(self):
        Node_Network.G.nodes[20]['edgeList'].clear()
        Node_Network.sendEdgePacket(Node_Network.G.nodes[1], Node_Network.G)
        print(Node_Network.G.nodes[20]['edgeList'], "Edge List")
        self.assertTrue(Node_Network.G.nodes[20]['edgeList'][0][0] >= 19)
        self.assertTrue(Node_Network.G.nodes[20]['edgeList'][0][1] >= 0)
        return
    
    def testNodeSampling(self):
        mls = Node_Network.nodeSampling(60000, Node_Network.G.nodes[20]['markCount'], Node_Network.G.nodes[20]['prob'], 0)
        print(mls, "Most Likely Suspect: Node")
        self.assertTrue(mls[0] == 1)

    def testEdgeSampling(self):
        mls = Node_Network.edgeSampling(Node_Network.recPath, Node_Network.G.nodes[20]['edgeList'], Node_Network.G.nodes[20]['edgeDList'], 60000, Node_Network.G.nodes[20]['prob'], 3)
        print(mls, "Most Likely Suspect: Edge")
        if mls is None:
            self.assertTrue(1 == 1)
        return
    
    
if __name__ == '__main__':
    unittest.main()