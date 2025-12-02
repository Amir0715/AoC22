use std::collections::{HashMap, HashSet};
use std::error::Error;
use std::fs::File;
use std::io::Read;

fn read_input<'a>() -> Result<(HashMap<i32, HashSet<i32>>, Vec<Vec<i32>>), Box<dyn Error>> {
    let file_path = "D:\\projects\\aoc-24\\src\\task_5\\input";
    let mut f = File::open(file_path)?;
    let mut input = String::new();
    f.read_to_string(&mut input)?;
    
    let mut page_rules = HashMap::<i32, HashSet<i32>>::new();
    
    // // Итерируемся до первой пустой строки
    for line in input.lines().take_while(|x| !x.is_empty()) {
        let line_elems = line.split('|')
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        
        let left = line_elems[0];
        let right = line_elems[1];
        match page_rules.get_mut(&left) {
            None => {
                page_rules.insert(left, HashSet::from([right]));
            }
            Some(vec) => {
                vec.insert(right);
            }
        }
    }

    println!("rules: {:?}", page_rules);

    let mut update_input = Vec::new();
    for line in input.lines().skip_while(|x| !x.is_empty()).skip(1) {
        let line_elems = line.split(',')
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();

        update_input.push(line_elems)
    }
    
    Ok((page_rules, update_input))
}


pub(crate) fn solution() {
    let input = read_input();
    let (tree, arrays) = input.unwrap();
    // let result_part1: i32 = part_1(tree, arrays);
    let result_part2: i32 = part_2(&tree, arrays);

    // println!("task5: result of part1: {}", result_part1);
    println!("task5: result of part2: {}", result_part2);
}

fn part_1(page_rules: HashMap<i32, HashSet<i32>>, input_updates: Vec<Vec<i32>>) -> i32 {
    let mut median_sums = 0;
    for line in input_updates {
        let mut is_correct = true;
        for windows in line.windows(2) {
            let left = windows[0];
            let right = windows[1];
            
            if !page_rules.contains_key(&left) || !page_rules.get(&left).unwrap().contains(&right) {
                is_correct = false;
                break;
            }
        }
        
        print!("{:?} -> {}", line, is_correct);
        
        if is_correct {
            let median_index = (line.len() / 2);
            println!(" ; median_index={}", median_index);
            median_sums += line[median_index];
        }
        
    }

    median_sums
}

fn part_2(page_rules: &HashMap<i32, HashSet<i32>>, input_updates: Vec<Vec<i32>>) -> i32 {
    let mut median_sums = 0;
    for line in input_updates {
        let mut is_correct = true;
        for windows in line.windows(2) {
            let left = windows[0];
            let right = windows[1];

            if !page_rules.contains_key(&left) || !page_rules.get(&left).unwrap().contains(&right) {
                is_correct = false;
                break;
            }
        }
        
        if !is_correct {
            // println!("\nOriginal: {:?}", line);
            let line_fixes = fix_order(&page_rules, &line);
            // print!("Fixed: {:?}", line_fixes);
            
            let median_index = line_fixes.len() / 2;
            // println!(" ; median_index={}\n", median_index);
            median_sums += line_fixes[median_index];
        }
    }

    median_sums
}

fn fix_order(page_rules: &HashMap<i32, HashSet<i32>>, incorrect_vec: &Vec<i32>) -> Vec<i32> {
    let mut copy_incorrect_vec = incorrect_vec.clone();
    let empty_hash_set = &HashSet::default();
    let mut x = 0;
    while x < copy_incorrect_vec.len() {
    // for mut x in 0..copy_incorrect_vec.len() {
        let x_value = copy_incorrect_vec[x];
        for y in 0..x {
            let y_value = copy_incorrect_vec[y];
            // println!("x={x} | y = {y} | [x] = {x_value} | [y] = {y_value}");
            
            // для каждого ключа y значение под индексом x должно быть в множестве
            // если оно так - пока все хорошо
            // если условие не выполняет - необходимо свапнуть элементы y и x и начать заново (сбросить x)
            if !page_rules.get(&y_value).unwrap_or(empty_hash_set).contains(&x_value) {
                copy_incorrect_vec.swap(x, y);
                // println!("swap {x_value} and {y_value}");
                // println!("new array: {:?}", copy_incorrect_vec);
                x = 0;
                break;
            }
        }
        
        x += 1;
    }

    copy_incorrect_vec
}
