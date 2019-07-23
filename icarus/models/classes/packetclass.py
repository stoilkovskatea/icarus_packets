class Packet():

    def __init__(self, receiver=None, serving_node=None, current_node=None,
                 current_hop=0, content=None):

        self.receiver = receiver
        self.serving_node = serving_node
        self.current_node = current_node
        self.current_hop = current_hop
        self.content = content


