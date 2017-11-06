'''
Created on Oct 12, 2016

@author: mwitt_000
'''
import network_3
import link_3
import threading
from time import sleep

##configuration parameters
router_queue_size = 0 #0 means unlimited
simulation_time = 1 #give the network sufficient time to transfer all packets before quitting

if __name__ == '__main__':
    object_L = [] #keeps track of objects, so we can kill their threads
    
    #create network nodes
    client1 = network_3.Host(1)#need to add 4 clients
    object_L.append(client1)
    client2 = network_3.Host(2)#need to add 4 clients
    object_L.append(client2)
    client3 = network_3.Host(3)#need to add 4 clients
    object_L.append(client3)
    client4 = network_3.Host(4)#need to add 4 clients
    object_L.append(client4)
    router_a = network_3.Router(name='A', intf_count=1, max_queue_size=router_queue_size)
    object_L.append(router_a)
    router_b = network_3.Router(name='B', intf_count=1, max_queue_size=router_queue_size)
    object_L.append(router_b)
    router_c = network_3.Router(name='C', intf_count=1, max_queue_size=router_queue_size)
    object_L.append(router_c)
    router_d = network_3.Router(name='D', intf_count=1, max_queue_size=router_queue_size)
    object_L.append(router_d)
    
    #create a Link Layer to keep track of links between network nodes
    link_layer = link_3.LinkLayer()
    object_L.append(link_layer)
    
    #add all the links
    link_layer.add_link(link_3.link_3(client, 0, router_a, 0, 50))
    link_layer.add_link(link_3.link_3(router_a, 0, server, 0, 50))
    
    
    #start all the objects
    thread_L = []
    thread_L.append(threading.Thread(name=client1.__str__(), target=client1.run))
    thread_L.append(threading.Thread(name=client2.__str__(), target=client2.run))
    thread_L.append(threading.Thread(name=client3.__str__(), target=client3.run))
    thread_L.append(threading.Thread(name=client4.__str__(), target=client4.run))
    thread_L.append(threading.Thread(name=router_a.__str__(), target=router_a.run))
    thread_L.append(threading.Thread(name=router_b.__str__(), target=router_b.run))
    thread_L.append(threading.Thread(name=router_c.__str__(), target=router_c.run))
    thread_L.append(threading.Thread(name=router_d.__str__(), target=router_d.run))
    thread_L.append(threading.Thread(name="Network", target=link_layer.run))
    
    for t in thread_L:
        t.start()
    
    
    #create some send events    
    #for i in range(3):
    #    client.udt_send(2, 'Sample data %d' % i)
    
    client1.udt_send(2, 'This part surprisingly took a long long time to get done with. Hope rest is easy. Woohooo. is this 80 already?',
                        50)
    
    #give the network sufficient time to transfer all packets before quitting
    sleep(simulation_time)
    
    #join all threads
    for o in object_L:
        o.stop = True
    for t in thread_L:
        t.join()
        
    print("All simulation threads joined")



# writes to host periodically