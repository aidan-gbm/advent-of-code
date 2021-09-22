#!/usr/bin/env bash

x=0
y=0
CARD=0 # NORTH (0), EAST (1), SOUTH (2), WEST (3)
file="day1.in"
while IFS='' read -r line; do
    IFS=', ' read -ra steps <<< $line
    for step in ${steps[@]}; do
        dir=${step:0:1}
        len=${step:1:3}
        case $dir in
            "L")
                CARD=$(($CARD - 1))
                ;;
            "R")
                CARD=$(($CARD + 1))
                ;;
        esac

        if [[ $CARD -gt 3 ]]; then
            CARD=0
        elif [[ $CARD -lt 0 ]]; then
            CARD=3
        fi

        case $CARD in
            0)
                y=$(($y + $len))
                ;;
            1)
                x=$(($x + $len))
                ;;
            2)
                y=$(($y - $len))
                ;;
            3)
                x=$(($x - $len))
                ;;
        esac
    done
done < $file
dist=$((${x#-} + ${y#-}))
echo "Final Distance: $dist"
