class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        treeDict={i:[] for i in range(n)}

        for node,nei in edges:
            treeDict[node]=treeDict.get(node,[])
            treeDict[node].append(nei)
            treeDict[nei]=treeDict.get(nei,[])
            treeDict[nei].append(node)

        visited=set()
        def dfs(node,parent):
            visited.add(node)

            for nei in treeDict[node]:
                if nei==parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei,node):
                    return False
            return True
        if not dfs(0,None):
            return False
        else:
            return len(visited)==n 

