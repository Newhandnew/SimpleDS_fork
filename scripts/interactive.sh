#!/bin/sh

#################################################################################### 
# This script runs the SimpleDS system for training dialogue agents 
# <ahref="mailto:h.cuayahuitl@gmail.com">Heriberto Cuayahuitl</a>
####################################################################################

stty cols 120

if [ $1 = "train" ] ; then
   for i in $(seq 1 50000) 
   do
     xterm -geometry 120x50 -T "SimpleDS.Server" -e "ant SimpleDS" &
     sleep 2
     cd web/main
     xterm -geometry 80x20 -T "SimpleDS.Client" -e "node runclient.js train"
     #node runclient.js train
     cd ../../
     echo "iteration ${i}"
     sleep 1
   done
   echo "done!!!"

elif [ $1 = "test" ] ; then 
   xterm -geometry 120x50 -T "SimpleDS.Client" -hold -e "ant SimpleDS" &
   sleep 1
   xterm -geometry 120x50 -T "interactive" -hold -e "python android_client.py" &
   sleep 1
   cd web/main
   xterm -geometry 80x20 -T "SimpleDS.Client" -hold -e "node runclient.js test"
   #node runclient.js test
   cd ../../

else 
   echo "usage: run.sh (train | test)" 
fi 

