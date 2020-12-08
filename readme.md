README
=============================

Step 1 -- reserve rspec from Geni 
-----------------------------

Use the rspec in the repository.

Step 2 -- some basic configurations on client and cache nodes 
-----------------------------

On client node, run: 

    
    sudo apt-get update   
    sudo apt-get install python-pip   
    sudo apt-get install python-tk   
    pip install requests   
    pip install matplotlib

On cache node, run: 

    sudo apt-get update  
    sudo apt-get install trafficserver  
    cd /var/run  
    sudo mkdir trafficserver  
    cd /etc/trafficserver/  
    sudo vi records.config  

Then we go into the file, move the cursor to the bottom and press ‘a’ to 
edit the file. Add the following sentence into the file to set up a forward proxy.
The default port is 8080.

    CONFIG proxy.config.url_remap.remap_required INT 0
    CONFIG proxy.config.reverse_proxy.enabled INT 0

Then press ‘Esc’ to stop editing. And input _:wp_ to quit the file. 

Step 3 -- run experiment without cache 
---------------------------

On client node, upload _withoutCache.py_ to the node and run it.

    python withoutCache.py

Step 4 -- run experiment with cache 
---------------------------

On cache node, run the following command to start the cache server.

    cd /usr/bin
    sudo ./traffic_server start
 
On client node, upload withCache.py to the node and run it.

    python withCache.py
