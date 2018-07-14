import xmlrpc.client

import re
import socket
import urllib3


class SCGITransport(xmlrpc.client.Transport):
    def single_request(self, host, handler, request_body, verbose=0):
        # Add SCGI headers to the request.
        headers = {'CONTENT_LENGTH': str(len(request_body)), 'SCGI': '1'}
        header = '\x00'.join(('%s\x00%s' % item for item in headers.items())) + '\x00'
        header = '%d:%s' % (len(header), header)
        request_body = '%s,%s' % (header, request_body)
        #print(host)
        sock = None
        
        try:
            if host:
                u = urllib3.util.url.parse_url(host)
                host = u.host
                port = u.port
                #host, port = urllib3.splitport(host)
                addrinfo = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
                sock = socket.socket(*addrinfo[0][:3])
                sock.connect(addrinfo[0][4])
            else:
                sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                sock.connect(handler)
            
            self.verbose = verbose
            
            sock.send(request_body.encode())
            return self.parse_response(sock.makefile())
        finally:
            if sock:
                sock.close()
    
    def parse_response(self, response):
        p, u = self.getparser()
        
        response_body = ''
        while True:
            data = response.read(1024)
            if not data:
                break
            response_body += data
        
        # Remove SCGI headers from the response.
        response_header, response_body = re.split(r'\n\s*?\n', response_body, maxsplit=1)
        
        if self.verbose:
            print('body:', repr(response_body))
        
        p.feed(response_body)
        p.close()
        
        return u.close()


class SCGIServerProxy(xmlrpc.client.ServerProxy):
    def __init__(self, uri, transport=None, encoding=None, verbose=False, allow_none=False, use_datetime=False):
        #print(uri)
        u = urllib3.util.url.parse_url(uri)
        type = u.scheme
        uri = u.request_uri
        host = u.host
        port = u.port
        #print(u, type, uri)
        #type, uri = urllib3.splittype(uri)
        if type not in ('scgi'):
            raise IOError('unsupported XML-RPC protocol')
        #self.__host, self.__handler = urllib3.splithost(uri)
        self.__host = host + ':' + str(port)
        #self.__port = port
        self.__handler = uri #TODO: CHECK ME
        if not self.__handler:
            self.__handler = '/'
        
        if transport is None:
            transport = SCGITransport(use_datetime=use_datetime)
        transport.set_port = u.port
        self.__transport = transport
        self.__encoding = encoding
        self.__verbose = verbose
        self.__allow_none = allow_none
 
    def __close(self):
        self.__transport.close()
    
    def __request(self, methodname, params):
        # call a method on the remote server
    
        request = xmlrpc.client.dumps(params, methodname, encoding=self.__encoding, allow_none=self.__allow_none)
        response = self.__transport.request(self.__host, self.__handler, request, verbose=self.__verbose)
        if len(response) == 1:
            response = response[0]
        return response
    
    def __repr__(self):
        return ("<SCGIServerProxy for %s%s>" % (self.__host, self.__handler) )
    
    __str__ = __repr__
    
    def __getattr__(self, name):
        # magic method dispatcher
        return xmlrpc.client._Method(self.__request, name)

    # note: to call a remote object with an non-standard name, use
    # result getattr(server, "strange-python-name")(args)

    def __call__(self, attr):
        """A workaround to get special attributes on the ServerProxy
           without interfering with the magic __getattr__
        """
        if attr == "close":
            return self.__close
        elif attr == "transport":
            return self.__transport
        raise AttributeError("Attribute %r not found" % (attr,))

def main():
    server = SCGIServerProxy('scgi://127.0.0.1:5000')
    print(server.system.listMethods())

if __name__ == "__main__":
    main()

