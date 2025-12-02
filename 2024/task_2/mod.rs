use crate::task_2::Order::{Ascending, Descending};
use std::arch::x86_64::_xgetbv;
use std::collections::hash_map::Keys;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;
use std::process::Command;

fn read_input() -> Vec<Vec<i32>> {
    let file_path = "D:\\projects\\aoc-24\\src\\task_2\\input";
    let mut vec = Vec::with_capacity(1000);

    let file = File::open(Path::new(file_path)).unwrap();
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line.unwrap();
        let words: Vec<_> = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
        vec.push(words);
    }

    vec
}

pub(crate) fn solution() {
    let vec = read_input();

    let result_part1: i32 = part_1(&vec);
    // let result_part2: i32 = part_2(&vec);

    println!("task2: result of part1: {}", result_part1);
    // println!("\ntask2: result of part2: {}", result_part2);
}

#[derive(Debug)]
enum Order {
    Ascending,
    Descending,
}

fn part_1(vec: &Vec<Vec<i32>>) -> i32 {
    let mut safe_count = 0;
    for line in vec.iter() {
        let mut l = line.iter().take(line.len() - 1);
        let mut r = line.iter().skip(1);

        let mut is_safe = true;

        // Расчитали первые элементы
        let l_value = l.next().unwrap();
        let r_value = r.next().unwrap();

        let order: Order;

        match *l_value - *r_value {
            diff if diff >= 1 && diff <= 3 => {
                order = Descending;
            }
            diff if diff <= -1 && diff >= -3 => {
                order = Ascending;
            }
            _ => {
                continue;
            }
        }

        while is_safe {
            let l_next = l.next();
            let r_next = r.next();
            if r_next.is_none() || l_next.is_none() {
                break;
            }

            let l_value = l_next.unwrap();
            let r_value = r_next.unwrap();

            match (&order, l_value - r_value) {
                (Descending, diff) if diff < 1 || diff > 3 => {
                    is_safe = false;
                    break;
                }
                (Ascending, diff) if diff > -1 || diff < -3 => {
                    is_safe = false;
                    break;
                }
                (_, _) => {}
            }
        }

        if is_safe {
            safe_count += 1
        }
    }
    safe_count
}

fn part_2(vec: &Vec<Vec<i32>>) -> i32 {
    // !!!Not worked!!!
    
    
    let mut safe_count = 0;
    for line in vec.iter() {
        println!();
        // O(N)
        let diffs = line.windows(2).map(|w| w[1] - w[0]).collect::<Vec<i32>>();
        print!("original: {:?}, diffs: {:?}", line, diffs);

        // O(N)
        if diffs.iter().all(|x| x.is_positive() && *x >= 1 && *x <= 3) {
            // SAFE | все разницы в [+1, +3]
            safe_count += 1;
            print!(" -> safe");
            continue;
        }

        // O(N)
        if diffs
            .iter()
            .all(|x| x.is_negative() && *x >= -3 && *x <= -1)
        {
            // SAFE | все разницы в [-3, -1]
            safe_count += 1;
            print!(" -> safe");
            continue;
        }

        // алгоритм фикса
        // +2 -1 +2 +1 -> +2 +1 +1 - SAFE
        //   +
        // +1 +5 -2    -> +1 +3    - SAFE
        //      +
        // +1 +5 +1 +1 -> +1 +6 +1 - UNSAFE

        let mut fixed_diff = Vec::new();
        let mut windows = diffs.windows(2);
        let mut can_remove = 1;
        loop {
            let w = windows.next();
            if w.is_none() {
                break;
            }
            
            let w = w.unwrap();
            let l = *w.first().unwrap();
            let r = *w.last().unwrap();
            if (l < 1 && l > 3 || l < -3 && l > -1) && can_remove > 0 {
                let diff = l + r;
                fixed_diff.push(diff);

                can_remove -= 1;
            } else {
                fixed_diff.push(l);
                fixed_diff.push(r);
            }
        }

        print!(", fixed_diff {:?}", fixed_diff);

        // O(N)
        if fixed_diff
            .iter()
            .all(|x| x.is_positive() && *x >= 1 && *x <= 3)
        {
            // SAFE | все разницы в [+1, +3]
            safe_count += 1;
            print!(" -> safe");
            continue;
        }

        // O(N)
        if fixed_diff
            .iter()
            .all(|x| x.is_negative() && *x >= -3 && *x <= -1)
        {
            // SAFE | все разницы в [-3, -1]
            safe_count += 1;
            print!(" -> safe");
            continue;
        }

        print!(" -> unsafe");
    }
    safe_count
}
