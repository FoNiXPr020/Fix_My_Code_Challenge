#!/usr/bin/node
/*
    Lets Print a square with the character...
*/


if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1)
}

iSize = parseInt(process.argv[2], 10)

for (let i = 0 ; i < iSize ; i ++) {
    for (let j = 0 ; j < iSize ; j ++) {
        process.stdout.write("#");
    }
    process.stdout.write("\n");
}