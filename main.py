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
        node, remains = self._findChildNode(self.root, urlParts[0], urlParts[1:])
        if remains is not None:
            self._addChildNode(node, remains)

    def _findChildNode(self, node, url, remains):
        if self._hasThisChild(node, url):
            child = self._getChildNodeByName(node, url)
            if not remains:
                return child, None
            return self._findChildNode(child, remains[0], remains[1:])
        else:
            remains.insert(0, url)
            return node, remains

    def _hasThisChild(self, node, name):
        return node.childNameList.count(name) != 0

    def _getChildNodeByName(self, parent, name):
        index = parent.childNameList.index(name)
        return parent.childNode[index]

    def _addChildNode(self, parent, url):
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

    def matchUrl(self, urlString):
        urlParts = urlString.split("/")
        node, remains = self._findChildNode(self.root, urlParts[0], urlParts[1:])
        if remains is None:
            print node.n
        else:
            print "url match failed!!!"

if __name__ == "__main__":
    urlTrieTree = PathTrie()
    urlTrieTree.absurdInTree("www.some.com/other/url")
    urlTrieTree.absurdInTree("www.some.com/2other/edf")
    urlTrieTree.absurdInTree("www.some.com/other/url2")
    urlTrieTree.matchUrl("www.some.com/other/url")