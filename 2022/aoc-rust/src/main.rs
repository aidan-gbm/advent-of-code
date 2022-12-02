use std::fs;


fn main() {
    let data = fs::read_to_string("./input/input1.txt")
        .expect("could not read file");

    let data = data.split("\n");

    let mut sum = 0;
    let mut elves: Vec<u32> = Vec::new();
    for line in data {
        if line.is_empty() {
            elves.push(sum);
            sum = 0;
        } else {
            let cals: u32 = line.trim().parse()
                .expect("bad input");
            sum += cals;
        }
    }

    elves.sort_unstable();
    elves.reverse();
    for idx in 0..3 {
        println!("Elf {}: {}", idx + 1, &elves[idx]);
    }

    println!("Total: {}", &elves[0] + &elves[1] + &elves[2]);
}

