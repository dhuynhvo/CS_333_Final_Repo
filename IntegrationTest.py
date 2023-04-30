import unittest
import Node_Network

class IntegrationTestNodeNetwork(unittest.TestCase):

    totalPacketsSent = 0

    def testSendNodePackets(self):
        testRange = 3000
        totalPacketsSent = 0
        for i in range(0,testRange):
            for i in range(1,21):
                chance = Node_Network.rd.random()
                if chance < Node_Network.G.nodes[i]['sendChance']:
                    totalPacketsSent += 1
                    Node_Network.sendPacket(Node_Network.G.nodes[i], Node_Network.G)

        print(Node_Network.G.nodes[20]['markCount'], "Node Packets Integration")
        if(Node_Network.G.nodes[20]['markCount'][20] > testRange):
            pass

        return
    
    def testSendEdgePackets(self):
        testRange = 3000
        totalPacketsSent = 0

        for i in range(0,testRange):
            for i in range(1,20):
                chance = Node_Network.rd.random()
                if chance < Node_Network.G.nodes[i]['sendChance']:
                    totalPacketsSent += 1
                    Node_Network.sendEdgePacket(Node_Network.G.nodes[i], Node_Network.G)
        #print(Node_Network.G.nodes[20]['edgeList'])

        if(Node_Network.G.nodes[20]['edgeList'].count((19,20)) > 20):
            pass

        return

    def testNodeSamplingFunctions(self):
        testRange = 3000
        totalPacketsSent = 0
        for i in range(0,testRange):
            for i in range(1,21):
                chance = Node_Network.rd.random()
                if chance < Node_Network.G.nodes[i]['sendChance']:
                    totalPacketsSent += 1
                    Node_Network.sendPacket(Node_Network.G.nodes[i], Node_Network.G)

        nodeSuspects = Node_Network.nodeSampling(totalPacketsSent, Node_Network.G.nodes[20]['markCount'], Node_Network.G.nodes[20]['prob'], 0)
        print("Node Sampling Suspects: ", nodeSuspects, "Node Integration")
        print("Total Packets Sent: ", totalPacketsSent, "Node Integration")
        if(nodeSuspects is not None):
            pass

        return
    
    def testEdgeSamplingFunctions(self):
        testRange = 3000
        totalPacketsSent = 0

        for i in range(0,testRange):
            for i in range(1,20):
                chance = Node_Network.rd.random()
                if chance < Node_Network.G.nodes[i]['sendChance']:
                    totalPacketsSent += 1
                    Node_Network.sendEdgePacket(Node_Network.G.nodes[i], Node_Network.G)

        edgeSuspects = Node_Network.edgeSampling(Node_Network.recPath, Node_Network.G.nodes[20]['edgeList'], Node_Network.G.nodes[20]['edgeDList'], totalPacketsSent, Node_Network.G.nodes[20]['prob'], 3)
        print("Edge Sampling Suspects: ", edgeSuspects, "Edge Integration")
        print("Total Packets Sent: ", totalPacketsSent, "Edge Integration")
        if(edgeSuspects is not None):
            pass

        return
    
    def testNodeCountAndEdgeCountFunctions(self):
        testRange = 3000
        totalPacketsSent = 0

        for i in range(0,testRange):
            for i in range(1,20):
                chance = Node_Network.rd.random()
                if chance < Node_Network.G.nodes[i]['sendChance']:
                    totalPacketsSent += 1
                    Node_Network.countPacket(i)
                    Node_Network.countEdgePacket(Node_Network.G.nodes[i])

        if(Node_Network.G.nodes[20]['markCount'][19] > 0 and Node_Network.G.nodes[20]['edgeList'][19].count((19,20)) > 20):
            pass

if __name__ == '__main__':
	unittest.main()