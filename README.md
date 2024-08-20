# ILLUMIO ASSESSMENT
## RISHIT PALLAV

### Heading
Thank you for letting me take the assessment. I have completed the assessment in Python 3.11.0. I have used the following libraries:
- csv

### Structure
The program is divided into 2 categories:
1. flow_log_parser.py - This file contains the main code for the assessment.
2. test_flow_log_parser.py - This file contains the test cases for the main code.

The folder tests contains the test cases for the main code.
The files are divided into 4 categories:
1. flow_logs.txt - This file contains the flow logs.
2. lookup_table.csv - This file contains the lookup table.
3. matches_port_protocol.txt - This file contains the matches for port and protocol.
4. matches_tag.txt - This file contains the matches for tag.

The flow_logs, lookup_table are used as input files for the main code. Whereas the matches_port_protocol and matches_tag are used as output files for the main code.
The test cases are written in tests folder.

### How to run the code
To run general code, ensure the appropriate flow_logs.txt and lookup_table.csv are present in the same directory as the code. Then run the following command:
```python flow_log_parser.py```

To run the test cases, ensure the appropriate flow_logs.txt, lookup_table.csv, matches_port_protocol.txt and matches_tag.txt are present in the tests directory. Then run the following command:
```python test_flow_log_parser.py```

The tests folder currently has 2 different test sets:
1. xxxx_test1.txt - This file contains the 1st set of test cases.
2. xxxx_test2.txt - This file contains the 2nd set of test cases.

Please make sure to modify any test cases as needed. But make sure to also modify the corresponding output test file: matches_port_protocol.txt and matches_tag.txt.

### Test Cases
There are 2 sets of test cases:
1. Covers the testcases mentioned in the email. Altough, the email sample output is different, the output here indicates the original output.
2. Covers all the other edge cases. Including case insensitivity, multiple matches, no matches, etc.

### Assumptions
1. The flow logs do not have any headers.
2. The lookup table does not have headers.
3. The flow logs format is version 2. Follows the structure mentioned in the following url: [AWS DOCS](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html)
4. A pair of Port, Protocol belongs to only one tag.
5. A tag can have many Port, Protocol pairs.
6. We are only comparing Destination Ports and not care about source ports.
7. The end of the output files has a newline character.
8. The Protocols used are: TCP, UDP, ICMP, IGMP, ESP, AH, SCTP, GRE.

### Thank you