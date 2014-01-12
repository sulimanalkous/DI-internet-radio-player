#!/bin/bash
number=0
until [ $number -gt 0 ];do
awk -F"\t" '
BEGIN {
print "====================================================================="
printf "%-6s %-24s %s\n", "No.", "Station", "Description"
print "====================================================================="
}
{ printf "%-6s %s\n", $1, $3 }' urls | awk -F"-" '{ printf "%-30s %s\n", $1, $2 }'
echo
echo "Enter the number of station ?"
read no

mplayer -msgcolor `cat urls | grep $no |cut -f 2`
$number=$no
done
