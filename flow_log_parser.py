import csv

class FlowLogParser:
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

    def __init__(self, flow_logs_name, lookup_table_name):
        self.flow_logs_name = flow_logs_name
        self.lookup_table_name = lookup_table_name
        self.lookups = {}
        self.matches_tag = {'Untagged': 0}
        self.matches_port_protocol = {}

    # Parse the lookup table and return the lookups and matches_tag
    def parse_lookup_table(self):
        try:
            with open(self.lookup_table_name, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.lookups[(row[0], row[1])] = row[2]
                    self.matches_tag[row[2]] = 0
        except FileNotFoundError:
            print(f"Lookup table with the name: {self.lookup_table_name} not found. Please check the file name and try again.")
            raise
        except Exception as e:
            print(f"An error occurred while parsing the lookup table: {e}")
            raise

    # Parse the flow logs and return the matches_tag and matches_port_protocol
    def parse_flow_logs(self):
        try:
            with open(self.flow_logs_name, 'r') as f:
                for line in f:
                    data = line.split()
                    # Making sure the line is not empty
                    protocol = self.PROTOCOLS.get(data[7], 'Unknown')
                    if (data[6], protocol) in self.lookups:
                        self.matches_tag[self.lookups[(data[6], protocol)]] += 1
                    elif (data[6], protocol.upper()) in self.lookups:
                        self.matches_tag[self.lookups[(data[6], protocol.upper())]] += 1
                    else:
                        self.matches_tag['Untagged'] += 1

                    if (data[6], protocol) in self.matches_port_protocol:
                        self.matches_port_protocol[(data[6], protocol)] += 1
                    else:
                        self.matches_port_protocol[(data[6], protocol)] = 1
        except FileNotFoundError:
            print(f"Flow logs file with the name: {self.flow_logs_name} not found. Please check the file name and try again.")
            raise
        except Exception as e:
            print(f"An error occurred while parsing the flow logs: {e}")
            raise

    # Output the results to matches_tag.txt and matches_port_protocol.txt
    def output_results(self):

        try:
            # Write the tags results to matches_tag.txt
            with open('matches_tag.txt', 'w') as matches_tag_file:
                matches_tag_file.write('Tag,Count\n')
                for tag, count in self.matches_tag.items():
                    matches_tag_file.write(tag + ',' + str(count) + '\n')
                
            # Write the port and protocol results to matches_port_protocol.txt
            with open('matches_port_protocol.txt', 'w') as matches_port_protocol_file:
                matches_port_protocol_file.write('Port,Protocol,Count\n')
                for port_protocol, count in self.matches_port_protocol.items():
                    matches_port_protocol_file.write(str(port_protocol[0])+ ',' + str(port_protocol[1]) + ',' + str(count) + '\n')
        
        except Exception as e:
            print(f"An error occurred while writing the results to the output files: {e}")
            raise

if __name__ == '__main__':
    parser = FlowLogParser('flow_logs.txt', 'lookup_table.csv')
    parser.parse_lookup_table()
    parser.parse_flow_logs()
    parser.output_results()