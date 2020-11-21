MAX_NODE_CAPACITY=2

class TokenHolder():
    def add_token(self,token):
        pass
    def remove_token(self):
        pass

class Node(TokenHolder):
    capacity=0
    tokens=[]
    log=[]
    def add_token(self,token):
        if self.capacity+1<MAX_NODE_CAPACITY:
            self.tokens.append(token)
            self.capacity+=1
            token.log("added to node")
            self.log.append("Token added")
        else:
            self.log.append("Max capacity limit already reached")
    def remove_token(self):
        token=self.tokens.pop()
        self.capacity-=1
        token.log("removed from node")
        self.log.append("Token removed")
        return token

class Transition(TokenHolder):
    tokens=[]
    log=[]
    def add_token(self,token):
        self.tokens.append(token)
        token.log("added to transtion")
        self.log.append("Token added")
    def remove_token(self):
        token=self.tokens.pop()
        token.log("removed from transition")
        self.log.append("Token removed")
        return token

class Token():
    logs=[]
    def log(self,message):
        self.logs.append(message)

class Arc():
    def __init__(self,transition,node):
        self.transition=transition
        self.node=node

class NodeToTransition(Arc):
    def move(self):
        self.transition.add_token(self.node.remove_token())

class TransitionToNode(Arc):
    def move(self):
        self.node.add_token(self.transition.remove_token())

if __name__=='__main__':
    token1=Token()
    tr1=Transition()
    n1=Node()
    arc1=NodeToTransition(tr1,n1)
    n1.add_token(token1)
    arc1.move()
    print(tr1.log)