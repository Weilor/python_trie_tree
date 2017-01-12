# -*- coding: utf-8 -*-
# @Author: acezio
# @Description: this module can parse url string to a trie tree

class PathNode(object):

    def __init__(self, n=None):
        self.n = n
        self.childNode = []
        self.childNameList = []


class PathTrie(object):

    def __init__(self):
        self.root = PathNode()

    def absurdInTree(self, urlString):
        urlParts = urlString.split("/")
        node, remains = self.findChildNode(self.root, urlParts[0], urlParts[1:])
        if remains is not None:
            self.addChildNode(node, remains)

    def findChildNode(self, node, url, remains):
        if self.hasThisChild(node, url):
            child = self.getChildNodeByName(node, url)
            return self.findChildNode(child, remains[0], remains[1:])
        else:
            remains.insert(0, url)
            return node, remains

    def hasThisChild(self, node, name):
        return node.childNameList.count(name) != 0

    def getChildNodeByName(self, parent, name):
        index = parent.childNameList.index(name)
        return parent.childNode[index]

    def addChildNode(self, parent, url):
        for name in url:
            child = PathNode(name)
            parent.childNode.append(child)
            parent.childNameList.append(name)
            parent = child

    def traversalTrieTree(self, node=None):
        if node is None:
            node = self.root
        print node.n
        if node.childNode:
            for node in node.childNode:
                self.traversalTrieTree(node)

if __name__ == "__main__":
    urlTrieTree = PathTrie()
    urlTrieTree.absurdInTree("www.some.com/other/url")
    urlTrieTree.absurdInTree("www.some.com/2other/edf")
    urlTrieTree.absurdInTree("www.some.com/other/url2")
    urlTrieTree.traversalTrieTree()
