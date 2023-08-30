#!/usr/bin/python3
import argparse
import subprocess

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output


parser = argparse.ArgumentParser()
# -b default:debug(0) or perf(1)
# -c default:1 3
parser.add_argument('-b', '--arg1', help='Select the compiled version default:debug(0) or perf(1)')
parser.add_argument('-c', '--arg2', help='Select the action of commit default:1 3')

args = parser.parse_args()
args1_check_flag = True
if args.arg1 is None:
    compiled_version = "DEBUG"
else:
    if (args.arg1 == 'debug') or (args.arg1 == 'DEBUG') or (args.arg1 == '0'):
        compiled_version = "DEBUG"
    elif (args.arg1 == 'perf') or (args.arg1 == 'PERF') or (args.arg1 == '1'):
        compiled_version = "PERF"
    else:
        args1_check_flag = False
        print("-b argument error Select the compiled version default:debug(0) or perf(1)")

args2_check_flag = True
if args.arg2 is None:
    commit_action = "1"
else:
    if args.arg2 == '1':
        commit_action = "1"
    elif args.arg2 == '3':
        commit_action = "3"
    else:
        args2_check_flag = False
        print("-c argument error Select the action of commit default:1 3")

if args1_check_flag and args2_check_flag:
    cmd_str = "rsync -v zuoyang@192.168.11.121:/home/zuoyang/haishen-build/haishen5/src/fw/_out/Vail_1333Bx_Product_H5XX1_" + compiled_version + "/Bin/H5XX1_firmware.secured.tim ./ "
    ret = run_command(cmd_str)
    print(ret)
    cmd_str="nvme fw-download -f H5XX1_firmware.secured.tim /dev/nvme0n1"
    ret = run_command(cmd_str)
    print(ret)
    cmd_str="nvme fw-commit /dev/nvme0n1 -s 1 -a "+commit_action
    ret = run_command(cmd_str)
    print(ret)

    
