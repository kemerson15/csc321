# packet capture
open Docker Desktop
run docker compose up
open 4 windows 
get into your final directory in all four windows
get into your nodes: docker compose exec node00, node01, node02 bash
adjust the localhost to the correct nodes and then run the codes in the correct nodes (to make sure they work)
in one of the nodes, run tcpdump -w file.pcap
then rerun the server and client files while tcpdump is running
kill the terminals

# parsing out relevant packets
in the final directory, mergecap the two files (task and weather) into one (full-take)
