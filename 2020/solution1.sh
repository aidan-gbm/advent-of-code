#!/bin/bash

entries=()
while read line; do
    entries+=($line)
done < input1.txt

function part1() {
    arr=("$@")
    for i in ${arr[@]:1:${#arr[@]}}; do
        [ $(($i+${arr[0]})) == 2020 ] && echo "Part 1: $(($i*${arr[0]}))" && return
    done
    part1 "${arr[@]:1:${#arr[@]}}"
}

# something is really inefficient here
# not sure if return works the way I think in bash
# 'break 2' also gives same results
function part2() {
    arr=("$@")
    for i in ${arr[@]:1:${#arr[@]}}; do
        for j in ${arr[@]:2:${#arr[@]}}; do
            [ $(($i+$j+${arr[0]})) == 2020 ] && echo "Part 2: $(($i*$j*${arr[0]}))" && return
        done
    done
    part2 "${arr[@]:1:${#arr[@]}}"
}

part1 "${entries[@]}"
part2 "${entries[@]}"
