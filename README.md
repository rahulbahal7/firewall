firewall
========
Network intrusion detection systems and firewalls tend to be vulnerable to evasion attacks. 
While one form of evasion takes advantage of desynchronization between the NIDS/firewall and end hosts, 
evasion vulnerabilities can also arise from the detection approach adopted.

FIREWALL EVASION

An application-level firewall is running on the project server at 127.0.0.1 port 2002. 
It is filtering connections to a vulnerable service that implements a JSON-based request–response protocol. 
In particular, the firewall will filter any AUTH command sent to the vulnerable service, but allow all others through. 
However, this firewall uses packet-filtering instead of stateful stream reassembly – that is, the firewall will match 
its filtering predicates against packet payloads, but not against the entire contents of the network stream.

Your task is to bypass the firewall, send an AUTH command to the vulnerable service, and collect the secret it returns.

AUTH command has the following format:
{
    command: "AUTH",
    user: <string>
}