def start_server(wlan):
    from socket import socket, getaddrinfo, SOL_SOCKET, SO_REUSEADDR
    from time import sleep
    from .responses import ok, unsupported
    from sys import print_exception
     
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
     
    addr = getaddrinfo('0.0.0.0', 80)[0][-1]
    
    # Open socket
    sock = socket()
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(1)
     
    print('listening on', addr)
    
    isRunning = True
     
    # Listen for connections
    while isRunning:
        connection = None
        
        try:
            connection, address = sock.accept()
            print('client connected from', addr)

            request = connection.recv(1024)
            # print(request)
            request = request.decode('ascii')
            
            parts = request.split()
            
            operation = parts[0]
            route = parts[1]
            
            print(f'Operation: {operation}')
            print(f'Route: {route}')
            
            if route == '/stop':
                print('Stopping Server')
                isRunning = False;
                
            if route == '/light':
                from light import toggle_light
                toggle_light()
                
            response = ok()
            
            connection.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            connection.send(response)
     
        except Exception as e:
            print_exception(e)
        finally:
            if connection:
                connection.close()
                connection = None
    
    print('Closing Socket...')
    sock.close()
    print('Closed Socket.')

