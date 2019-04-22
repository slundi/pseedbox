
class File:
    def __init__(self):
        self.path = '' #f.path, f.frozen_path?
        self.size = 0 #F.size_bytes
        self.chunks = 0 #f.size_chunks
        self.completed_chunks = 0 #f.completed_chunks
        self.proiority = 1 #F.priority, 0=do not download, 1=normal, 2=high
        self.prioritize_first = True #f.prioritize_first, f.prioritize_first.disable, f.prioritize_first.enable
        self.prioritize_last = True #f.prioritize_last, f.prioritize_last.disable, f.prioritize_last.enable
#f.is_created

class Torrent(object):
    def __init__(self, hash):
        self.id = hash
        self.name = '' #d.name
        self.size = 0 #d.size_bytes
        self.path = '' #d.directory
        self.state = 0 #d.state
        self.chunks = 0 #d.size_chunks
        self.chunk_size = 0 #d.chunk_size
        self.completed_chunks = 0 #d.completed_chunks
        self.owner ='' #d.custom1
        self.category = '' #d.custom2
        self.label = '' #d.custom2 too ?
        self.multiple_files = False #d.is_multi_file
        self.private = False #d.is_private
        self.proiority = 0 #d.priority
        self.ratio = 0 #d.ratio
        self.files = []

#Closed items are not open (d.is_open), with state=0.
#Paused items are open, but not active, with state=1.
#Started items are both open and active, with state=1.
#d.size_files number of files (excluding directories)

class Peer:
    def __init__(self):
        self.address='' #p.address
        self.banned = False #p.banned / p.banned.set
        self.client = '' #p.client_version
        self.completed = 0 #p.completed_percent
        self.download_rate = 0 #p.down_rate
        self.downloaded = 0 #p.down_total
        self.upload_rate = 0 #p.up_rate
        self.uploaded = 0 #p.up_total
        self.id = '' #p.id (peer ID hash)
        self.encrypted = True #p.is_encrypted
        self.incoming = False #p.is_incoming
