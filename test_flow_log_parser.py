import os
from flow_log_parser import FlowLogParser

def compare_files (file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
    return True

def test_flow_log_parser():

    # TEST 1
    parser = FlowLogParser('tests/flow_logs_test1.txt', 'tests/lookup_table_test1.csv')
    parser.parse_lookup_table()
    parser.parse_flow_logs()
    parser.output_results()

    try:
        assert compare_files('tests/matches_tag_test1.txt', 'matches_tag.txt')
        assert compare_files('tests/matches_port_protocol_test1.txt', 'matches_port_protocol.txt')
    except AssertionError:
        print("TEST 1 FAILED. Make sure the expected output file has new line at the End Of File.")
        return False

    # TEST 2
    parser = FlowLogParser('tests/flow_logs_test2.txt', 'tests/lookup_table_test2.csv')
    parser.parse_lookup_table()
    parser.parse_flow_logs()
    parser.output_results()

    try:
        assert compare_files('tests/matches_tag_test2.txt', 'matches_tag.txt')
        assert compare_files('tests/matches_port_protocol_test2.txt', 'matches_port_protocol.txt')
    except AssertionError:
        print("TEST 2 FAILED. Make sure the expected output file has new line at the End Of File.")
        return False
    
    return True
    
if __name__ == '__main__':
    if test_flow_log_parser():
        print("All tests passed!")
    else:
        print("One or more tests failed. Please make sure the expected output file has new line at the End Of File.")
        print("Please let me know if you have any questions.")