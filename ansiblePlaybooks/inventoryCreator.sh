#!/bin/bash
file=$1"-ec2_invent.csv"

if [[ $1 = "" ]]; then
  echo -e "\nSample Usage I: $0 C3"
  echo -e "Sample Usage II: $0 C101"
  echo -e "Tenant's inventory file must exist in output dir \n"
else
  echo '[linux]' > ansibleInventoryFiles/$1"-hosts"
  #for h in `cat output/$file` do; awk -F "," '{print $3 " " $1}' >> ansibleInventory/$1"-hosts"; done
  for h in `cat ../output/$file | grep -v Name`; do echo $h | awk -F "," '{print $3 " " $1}' >> ansibleInventoryFiles/$1"-hosts"; done
fi 