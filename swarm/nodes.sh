for NODE in `seq 1 5`; do docker-machine create --driver virtualbox "node-${NODE}" 
done
