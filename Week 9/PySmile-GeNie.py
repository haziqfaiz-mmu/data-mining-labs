import pysmile
import pysmile_license



# Initialize the pysmile network

net = pysmile.Network()

# Read the GeNIe network. Make sure you have built the GeNIe network.

net.read_file("Mobile.xdsl");

# Set evidence of "Call_Time" to "evening"

net.set_evidence("Call_Time", "evening")

# Update the belief of the network

net.update_beliefs()

# retrieve the beliefs of each state for the note "Occupation"

beliefs = net.get_node_value("Occupation")
    
for i in range(0, len(beliefs)):
    print(net.get_outcome_id("Occupation", i) + "=" + str(beliefs[i]))


