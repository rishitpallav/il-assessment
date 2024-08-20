import csv

# List of supported protocols
PROTOCOLS = {
    '1': 'icmp',
    '2': 'igmp',
    '6': 'tcp',
    '17': 'udp',
    '47': 'gre',
    '50': 'esp',
    '51': 'ah',
    '132': 'sctp'
}

# Parse the lookup table and return the lookups and matches_tag
def parse_lookup_table(lookup_table_name):
    lookups = {}
    matches_tag = {'Untagged': 0}

    try:
        with open(lookup_table_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                lookups[(row[0], row[1])] = row[2]
                matches_tag[row[2]] = 0
    except FileNotFoundError:
        print(f"Lookup table with the name: {lookup_table_name} not found. Please check the file name and try again.")
        raise
    except Exception as e:
        print(f"An error occurred while parsing the lookup table: {e}")
        raise

    return lookups, matches_tag

# Parse the flow logs and return the matches_tag and matches_port_protocol
def parse_flow_logs(lookups, matches_tag, flow_logs_name):

    matches_port_protocol = {}

    try:
        with open(flow_logs_name, 'r') as f:
            for line in f:
                data = line.split()
                # Making sure the line is not empty
                protocol = PROTOCOLS.get(data[7], 'Unknown')
                if (data[6], protocol) in lookups:
                    matches_tag[lookups[(data[6], protocol)]] += 1
                else:
                    matches_tag['Untagged'] += 1

                if (data[6], data[7]) in matches_port_protocol:
                    matches_port_protocol[(data[6], protocol)] += 1
                else:
                    matches_port_protocol[(data[6], protocol)] = 1
    except FileNotFoundError:
        print(f"Flow logs file with the name: {flow_logs_name} not found. Please check the file name and try again.")
        raise
    except Exception as e:
        print(f"An error occurred while parsing the flow logs: {e}")
        raise

    return matches_tag, matches_port_protocol

# Output the results to matches_tag.txt and matches_port_protocol.txt
def output_results(matches_tag, matches_port_protocol):

    # Write the tags results to matches_tag.txt
    with open('matches_tag.txt', 'w') as matches_tag_file:
        matches_tag_file.write('Tag,Count\n')
        for key, value in matches_tag.items():
            matches_tag_file.write(key + ',' + str(value) + '\n')
        
    # Write the port and protocol results to matches_port_protocol.txt
    with open('matches_port_protocol.txt', 'w') as matches_port_protocol_file:
        matches_port_protocol_file.write('Port,Protocol,Count\n')
        for key, value in matches_port_protocol.items():
            matches_port_protocol_file.write(str(key[0])+ ',' + str(key[1]) + ',' + str(value) + '\n')

lookups, matches_tag = parse_lookup_table('lookup_table.csv')
matches_tag, matches_port_protocol = parse_flow_logs(lookups, matches_tag, 'flow_logs.txt')

output_results(matches_tag, matches_port_protocol)