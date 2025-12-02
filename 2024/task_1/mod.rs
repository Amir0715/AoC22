use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn read_input() -> (Vec<i32>, Vec<i32>) {
    let file_path = "D:\\projects\\aoc-24\\src\\task_1\\input";
    let mut left = Vec::with_capacity(1000);
    let mut right = Vec::with_capacity(1000);

    let file = File::open(Path::new(file_path)).unwrap();
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line.unwrap();
        let words: Vec<_> = line.split_whitespace().collect();
        let left_word = words[0].parse::<i32>().unwrap();
        let right_word = words[1].parse::<i32>().unwrap();
        left.push(left_word);
        right.push(right_word);
    }

    (left, right)
}

pub(crate) fn solution() {
    let (mut left, mut right) = read_input();
    left.sort();
    right.sort();

    let result_sum: i32 = part_1(&left, &right);
    let result_sum_2: i32 = part_2(&left, &right);
    
    println!("result of part1: {}", result_sum);
    println!("result of part2: {}", result_sum_2)
    
}

fn part_1(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    left
        .iter()
        .zip(right.iter())
        .map(|(x, y)| (x - y).abs())
        .sum()
}

fn part_2(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let chunks = right
        .chunk_by(|a, b| a == b)
        .map(|x| (x[0], x.len() as i32 * x[0]));
    
    let hasp_map: HashMap<i32, i32> = HashMap::from_iter(chunks);
    
    left.iter()
        .map(|x| hasp_map.get(x).unwrap_or(&0))
        .sum()
}
