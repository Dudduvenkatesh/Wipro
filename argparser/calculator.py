import argparse
parser=argparse.ArgumentParser(description="calculator CLI Tool")
#reading the arguments
parser.add_argument("num1",type=int,help="first number")
parser.add_argument("num2",type=int,help="second number")
 
#Optional flags
parser.add_argument("--add",action="store_true",help="addition")
parser.add_argument("--sub",action="store_true",help="subtraction")
parser.add_argument("--mul",action="store_true",help="multiplication")
parser.add_argument("--all", action="store_true", help="Perform all operations")

 
args= parser.parse_args()

add_result = args.num1 + args.num2
sub_result = args.num1 - args.num2
mul_result = args.num1 * args.num2

if args.all:
    print("\n CALCULATOR FULL REPORT")
    print("------------------------")
    print("Addition :", add_result)
    print("Subtraction :", sub_result)
    print("Multiplication :", mul_result)
else:
    if args.add:
        print("Addition :", add_result)
    if args.sub:
        print("Subtraction :", sub_result)
    if args.mul:
        print("Multiplication :", mul_result)
    if not (args.add or args.sub or args.mul):
        parser.print_help()

