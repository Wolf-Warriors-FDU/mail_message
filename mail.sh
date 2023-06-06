#!/bin/sh
###
 # @Descripttion: your project
 # @version: 1.0
 # @Author: JiangFeng
 # @Date: 2023-06-05 22:07:15
 # @LastEditors: JiangFeng
 # @LastEditTime: 2023-06-06 20:28:45
### 


# you can modified this script for more useful functions.
#==================do your job==================#
# cd ~/your project
# CUDA_VISIBLE_DEVICES=0 python3 train.py 
txt_file=./test.txt
message=`tail -n -5 $txt_file`

#================modify the email===============#
send_to_email=jiangf21@m.fudan.edu.cn  # example
# password_own="" # get from smtp

#=================send an email=================#
python3 mail.py --send_to "$send_to_email"\
  --subject "test bash" --message "$message"



