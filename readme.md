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

Change the two attributes of records.config to the following, to set up
a forward proxy. The default port is 8080. 

    CONFIG proxy.config.url\_remap.remap\_required INT 0 
    CONFIG proxy.config.reverse\_proxy.enabled INT 0

Step 3 -- run experiment without cache 
---------------------------

On client node, download _withoutCache.py_ and run it. 

    sudo wget https://github.com/Yicli0512/CS655-GENI-Mini-Project/blob/master/withoutCache.py
    python withoutCache.py

Step 4 -- run experiment with cache 
---------------------------

On cache node, run the following command to start the cache server. 

    cd /usr/bin 
    sudo ./traffic\_server start

On client node, download _withCache.py_ and run it. 

    sudo wget https://github.com/Yicli0512/CS655-GENI-Mini-Project/blob/master/withCache.py
    python withCache.py
