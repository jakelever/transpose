import argparse
import sys

def main():
	parser = argparse.ArgumentParser('Command-line tool to transpose some data from std-in')
	parser.add_argument('-t',required=False,default='\t',type=str,help='Delimiter (default=\\t)')
	parser.add_argument('-n',action='store_true',help='Number output rows from one')
	parser.add_argument('-n0',action='store_true',help='Number output rows from zero')
	parser.add_argument('-o',required=False,type=str,help='Alternative output delimiter')
	args = parser.parse_args()

	f = sys.stdin

	data = []
	expected_col_count = None
	for line in f:
		split = line.rstrip('\n').split(args.t)
		if expected_col_count is not None:
			assert len(split) == expected_col_count

		expected_col_count = len(split)
		data.append(split)
	
	for c in range(expected_col_count):
		if args.n:
			output = [ str(c+1) ]
		elif args.n0:
			output = [ str(c) ]
		else:
			output = []

		output += [ x[c] for x in data ]

		if args.o:
			print(args.o.join(output))
		else:
			print(args.t.join(output))
		
