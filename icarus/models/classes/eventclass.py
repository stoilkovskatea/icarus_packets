__all__=['Event']

class Event():

    def __init__(self, packet=None , timing=0, type_chunk = 'interest', session_id=0, log = True):

        self.packet = packet
        self.timing = timing
        self.log = log
        self.type_chunk = type_chunk
        self.session_id = session_id
    def __lt__(self, other):
        return self.timing < other.timing