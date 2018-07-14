from torf import Torrent

def get_file_list(path):
    t = Torrent.read(path)
    print('Torrent size: ', t.size)
    #print(t)
    mi = t.metainfo
    #print(mi['info'])
    return mi['info']['files']

def main():
    print('main')
    get_file_list('test/Fate Zero.torrent')

if __name__ == "__main__":
    main()
