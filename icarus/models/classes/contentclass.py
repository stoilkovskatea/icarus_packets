__all__=['Content']

class Content():
    '''Class describing a content of multiple chunks

    -------------
    Parameters:
        content_id : ID of each the content i.e. content: 1, 2, 3... n_contents
        chunk_id : Each content consists of n number of chunk i.e. 1.1, 1.2, ... , 1.chunks
        chunks: Number of chunks per content
        parameter : Unique parameter for each object using the current object and chunk ID
        '''

    def __init__(self, content_id=0, chunk_id=0):
        self.content_id = content_id
        self.chunk_id = chunk_id

        self.chunks = 0
        self.parameter = str(self.content_id) + '.' + str(self.chunk_id)

    def __hash__(self):
        return hash(self.parameter)

    def __eq__(self, other):
        return self.parameter
