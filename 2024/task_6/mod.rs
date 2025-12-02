use std::collections::{HashMap, HashSet};
use std::error::Error;
use std::fs::File;
use std::io::Read;

fn read_input() -> Result<Vec<Vec<char>>, Box<dyn Error>> {
    let file_path = "D:\\projects\\aoc-24\\src\\task_6\\input";
    let mut f = File::open(file_path)?;
    let mut input = String::new();
    f.read_to_string(&mut input)?;

    let field = input
        .lines()
        .map(|x| x.chars().collect::<Vec<_>>())
        .collect();
    print!("field: {:?}\n", field);

    Ok(field)
}

pub(crate) fn solution() {
    let input = read_input();
    let result_part1: i32 = part_1(input.unwrap());
    // let result_part2: i32 = part_2(&tree, arrays);

    // println!("task5: result of part1: {}", result_part1);
    // println!("task5: result of part2: {}", result_part2);
}

fn part_1(field: Vec<Vec<char>>) -> i32 {
    let directions: Vec<(isize, isize)> = vec![
        (-1, 0),    // ^
        (0, 1),     // >
        (1, 0),     // v
        (0, -1)     // <
    ];
    let mut direction_iter = directions.iter().cycle();
    
    let (mut i, mut j) = find_start_position(&field);
    println!("Start pos: [{i}, {j}]");

    let mut loop_i = 0;
    loop {
        let mut direction;
        match direction_iter.next() {
            Some(next_direction) => {
                direction = *next_direction
            }
            _ => {}
        }
        let distance = distance_to_wall(&field, '#', (i, j), direction);
        println!("Loop {loop_i} | Distance to wall: {distance:?}");
        if distance.is_none() {
            break;
        }
        (i, j) = (distance.unwrap().1, distance.unwrap().2);
        loop_i += 1;
    }
    
    12
}

/// Рассчитывает расстояние до ближайшего символа wall_char в с шагом delta
fn distance_to_wall(
    field: &Vec<Vec<char>>,
    wall_char: char,
    start_position: (usize, usize),
    delta: (isize, isize),
) -> Option<(i32, usize, usize)> {
    let mut distance = 0;
    let (mut i, mut j) = (start_position.0, start_position.1);
    loop {
        if i >= field.len() || j >= field[i].len() {
            return None;
        }

        if field[i][j] == wall_char {
            return Some((distance, i, j));
        }

        match i.checked_add_signed(delta.0) {
            None => {
                return None;
            }
            Some(res) => {
                i = res;
            }
        }
        match j.checked_add_signed(delta.1) {
            None => {
                return None;
            }
            Some(res) => {
                j = res;
            }
        }
        
        distance += 1;
    }
}

fn find_start_position(field: &Vec<Vec<char>>) -> (usize, usize) {
    for (i, line) in field.iter().enumerate() {
        for (j, char) in line.iter().enumerate() {
            if *char == '^' {
                return (i, j);
            }
        }
    }

    (0, 0)
}

fn part_2(page_rules: &HashMap<i32, HashSet<i32>>, input_updates: Vec<Vec<i32>>) -> i32 {
    123
}
