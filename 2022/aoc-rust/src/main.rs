use std::env;
use std::fs;


fn day1(data: String) {
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
    println!("Part 1: {}", elves[0]);
    println!("Part 2: {}", &elves[0] + &elves[1] + &elves[2]);
}

fn day2(data: String) {
    const TIE: u32 = 3;
    const WIN: u32 = 6;
    let rounds = data.split("\n");

    let mut score1: u32= 0;
    let mut score2: u32 = 0;
    for moves in rounds {
        let opp: u8 = moves.as_bytes()[0] - b'A';
        let you: u8 = moves.as_bytes()[2] - b'X';

        // Part 1
        if you == opp {
            score1 += you as u32 + 1 + TIE;
        } else if (you + 1) % 3 == opp {
            score1 += you as u32 + 1;
        } else {
            score1 += you as u32 + 1 + WIN;
        }

        // Part 2
        if 0 == you {
            let you = (opp + 2) % 3;
            score2 += you as u32 + 1;
        } else if 1 == you {
            let you = opp;
            score2 += you as u32 + 1 + TIE;
        } else if 2 == you {
            let you = (opp + 1) % 3;
            score2 += you as u32 + 1 + WIN;
        }
    }

    println!("Part 1: {}", score1);
    println!("Part 2: {}", score2);
}

fn day3(data: String) {
    let rucksacks = data.split("\n");

    let mut first = "";
    let mut sum1: u32 = 0;
    let mut sum2: u32 = 0;
    let mut common: Vec<char> = Vec::new();
    for (idx, ruck) in rucksacks.enumerate() {
        let div = ruck.len() / 2;
        let parts = ruck.split_at(div);

        // Part 1
        let mut item: Option<char> = None;
        for chr in parts.0.chars() {
            match parts.1.find(|c| c == chr) {
                Some(_) => {
                    item = Some(chr);
                    break;
                },
                None => continue
            }
        }

        let item = item.unwrap();
        if item as u8 <= b'Z' {
            sum1 += item as u32 - 38;
        } else {
            sum1 += item as u32 - 96;
        }

        // Part 2
        if idx % 3 == 0 {
            first = ruck;
            common.clear();
        } else if idx % 3 == 1 {
            for chr in ruck.chars() {
                match first.find(|c| c == chr) {
                    Some(_) => common.push(chr),
                    None => continue
                }
            }
        } else {
            let mut group: Option<char> = None;
            for chr in common.clone() {
                match ruck.find(|c| c == chr) {
                    Some(_) => {
                        group = Some(chr);
                        break;
                    },
                    None => continue
                }
            }

            let group = group.unwrap();
            if group as u8 <= b'Z' {
                sum2 += group as u32 - 38;
            } else {
                sum2 += group as u32 - 96;
            }
        }
    }

    println!("Part 1: {}", sum1);
    println!("Part 2: {}", sum2);
}

fn main() {
    const TEST: bool = false;
    const INPUT_DIR: &str = "./input/";

    let args: Vec<String> = env::args().collect();

    let day: &str;
    let day_fn: fn(String);
    match args.len() {
        2 => {
            day = args[1].trim();
            match day {
                "1" => day_fn = day1,
                "2" => day_fn = day2,
                "3" => day_fn = day3,
                _ => {
                    eprintln!("Error: days 1-3 currently available");
                    return;
                }
            };
        },
        _ => {
            eprintln!("Usage: {} day", &args[0]);
            return;
        }
    }

    let file_name: String = if TEST {
        format!("test{}.txt", day)
    } else {
        format!("input{}.txt", day)
    };

    let data = fs::read_to_string(INPUT_DIR.to_owned() + &file_name)
        .expect("could not read file");

    println!("Computing day {}...", day);
    day_fn(data);
}
