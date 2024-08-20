import csv

protocol_dict = {
    '1': 'icmp',
    '2': 'igmp',
    '6': 'tcp',
    '17': 'udp',
    '47': 'gre',
    '50': 'esp',
    '51': 'ah',
    '132': 'sctp'
}

def parse_lookup_table():
    lookups = {}
    matches_tag = {'Untagged': 0}

    with open('lookup_table.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            lookups[(row[0], row[1])] = row[2]
            matches_tag[row[2]] = 0
    
    return lookups, matches_tag

def parse_flow_logs(lookups, matches_tag):

    matches_port_protocol = {}

    with open('flow_logs.txt', 'r') as f:
        for line in f:
            data = line.split()
            if (data[6], protocol_dict[data[7]]) in lookups:
                matches_tag[lookups[(data[6], protocol_dict[data[7]])]] += 1
            else:
                matches_tag['Untagged'] += 1
            if (data[6], data[7]) in matches_port_protocol:
                matches_port_protocol[(data[6], protocol_dict[data[7]])] += 1
            else:
                matches_port_protocol[(data[6], protocol_dict[data[7]])] = 1
    
    return matches_tag, matches_port_protocol

lookups, matches_tag = parse_lookup_table()
matches_tag, matches_port_protocol = parse_flow_logs(lookups, matches_tag)

print(matches_tag)
print(matches_port_protocol)