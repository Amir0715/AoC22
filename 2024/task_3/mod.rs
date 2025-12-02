use regex::{Captures, Regex};
use std::error::Error;
use std::fs::File;
use std::io::Read;

fn read_input() -> Result<String, Box<dyn Error>> {
    let file_path = "D:\\projects\\aoc-24\\src\\task_3\\input";
    let mut f = File::open(file_path)?;
    let mut input = String::new();
    f.read_to_string(&mut input)?;

    Ok(input)
}

pub(crate) fn solution() {
    let input = read_input();
    // let result_part1 = part_1(input.unwrap());
    let result_part2: i32 = part_2(input.unwrap());

    // println!("task3: result of part1: {}", result_part1);
    println!("task3: result of part2: {}", result_part2);
}

struct MulParams {
    x: i32,
    y: i32,
}

fn map_to_mul_params(cap: Captures) -> MulParams {
    let x: i32 = cap.name("x").unwrap().as_str().parse::<i32>().unwrap();
    let y: i32 = cap.name("y").unwrap().as_str().parse::<i32>().unwrap();
    MulParams { x, y }
}

fn part_1(input: String) -> i32 {
    let regex = Regex::new(r"mul\((?<x>\d+),(?<y>\d+)\)").unwrap();

    let result = regex
        .captures_iter(&input)
        .map(map_to_mul_params)
        .fold(0, |acc: i32, item: MulParams| acc + item.x * item.y);
    result
}

fn part_2(input: String) -> i32 {
    // идея: также с помощью регулярки получить список ключевых слов,
    // начать итеррироваться
    // если встретили do() - включаем
    // если встретили don't() - выключаем
    //

    let regex = Regex::new(r"mul\((?<x>\d+),(?<y>\d+)\)|do(n't)?\(\)").unwrap();
    let mut toggle = true;
    let mut sum = 0;
    for captures in regex.captures_iter(&input) {
        println!("{:?}", captures);

        let word = captures.get(0).unwrap().as_str();
        match word {
            "do()" => {
                toggle = true;
            }
            "don't()" => {
                toggle = false;
            }
            _ => {
                if !toggle { continue; } 
                
                let item = map_to_mul_params(captures);
                sum += item.x * item.y;
            }
        }
    }

    sum
}
