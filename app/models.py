
class Torrent:
    def __init__(self, hash):
        self.id = hash
        self.name = ''
        self.size = 0
        self.path = ''
        self.state = 0
        self.chunk_size = 0
        self.completed_chunks = 0
        self.owner ='' #d.custom1
        self.category = '' #d.custom2
        self.label = '' #d.custom2 too ?
        self.multiple_files = False #d.is_multi_file
        self.private = False #d.is_private
        self.proiority=0 #d.priority
        self.ratio = 0 #d.ratio
