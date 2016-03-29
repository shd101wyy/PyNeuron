# Outstar network
from neuron_type.out_star_network import OutstarNetwork
outstar=OutstarNetwork(4,3)
outstar.train([0,1,-1,-1])
outstar.train([1,1,-1,-1])
outstar.train([1,1,-1,-1])
outstar.train([1,1,-1,-1])
outstar.train([1,1,-1,-1])
outstar.train([1,1,-1,-1])

print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight