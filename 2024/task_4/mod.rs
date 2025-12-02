use diagonal::{diagonal_pos_neg, diagonal_pos_pos, straight_y};
use regex::Regex;
use std::error::Error;
use std::fmt::Alignment::Left;
use std::fs::File;
use std::io::Read;
use std::result;

fn read_input() -> Result<String, Box<dyn Error>> {
    let file_path = "D:\\projects\\aoc-24\\src\\task_4\\input";
    let mut f = File::open(file_path)?;
    let mut input = String::new();
    f.read_to_string(&mut input)?;

    Ok(input)
}

fn print_matrix(matrix: &Vec<Vec<char>>) {
    print!("[\n");
    for i in 0..matrix.len() {
        print!("\t{:?}\n", matrix[i]);
    }
    print!("]");
}

pub(crate) fn solution() {
    let input = read_input();
    // let result_part1 = part_1(input.unwrap());
    let result_part2: i32 = part_2(input.unwrap());

    // println!("task4: result of part1: {}", result_part1);
    println!("task4: result of part2: {}", result_part2);
}

fn rotate_matrix(matrix: &mut Vec<Vec<char>>) {
    print_matrix(matrix);

    matrix.iter_mut().for_each(|row| row.reverse());

    for i in 0..matrix.len() {
        let row = &matrix[i];
        for j in 0..row.len() {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    println!();
    print_matrix(matrix);
    println!()
}

fn string_from_matrix(matrix: &mut Vec<Vec<char>>) -> String {
    let mut result_string = String::new();
    matrix.iter_mut().fold(&mut result_string, |row, chars| {
        let line: String = chars.iter().collect();
        row.push_str(line.as_str());
        row.push_str("\n");
        row
    });

    result_string
}

fn rotate_string(input: &String) -> String {
    let mut char_matrix: Vec<Vec<char>> =
        input.lines().map(|line| line.chars().collect()).collect();

    // rotate_matrix(&mut char_matrix);
    // string_from_matrix(&mut char_matrix)

    let result = straight_y(&char_matrix);
    let buffer = &mut String::new();
    let result_string = result
        .into_iter()
        .map(|chars| chars.into_iter().collect::<String>())
        .fold(buffer, |mut acc, s| {
            acc.push_str(s.as_str());
            acc.push('\n');
            acc
        });

    result_string.to_string()
}

fn to_diagonals(input: &String) -> (String, String) {
    // Возвращает строки по диагонали

    let char_matrix: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
    let diagonal_pos_pos_vec = diagonal_pos_pos(&char_matrix);
    let buffer = &mut String::new();
    let diagonal_pos_pos_string = diagonal_pos_pos_vec
        .into_iter()
        .map(|chars| chars.into_iter().collect::<String>())
        .fold(buffer, |mut acc, s| {
            acc.push_str(s.as_str());
            acc.push('\n');
            acc
        });

    let diagonal_pos_neg_vec = diagonal_pos_neg(&char_matrix);
    let buffer = &mut String::new();
    let diagonal_pos_neg_string = diagonal_pos_neg_vec
        .into_iter()
        .map(|chars| chars.into_iter().collect::<String>())
        .fold(buffer, |mut acc, s| {
            acc.push_str(s.as_str());
            acc.push('\n');
            acc
        });

    (
        diagonal_pos_pos_string.to_string(),
        diagonal_pos_neg_string.to_string(),
    )
}

fn count(input: &String) -> i32 {
    let xmas_re = Regex::new(r"XMAS").unwrap();
    let xmas_re_revers = Regex::new(r"SAMX").unwrap();

    let count = xmas_re.captures_iter(&input).count() as i32;
    let count_revers = xmas_re_revers.captures_iter(&input).count() as i32;
    count + count_revers
}

fn part_1(input: String) -> i32 {
    /*  Идея -
        начинаем искать в исходной строке с помощью регулярки
        поворачиваем строку по часовой стрелке, ищем уже в ней
        после, берем все диагонали и ищем в них
    */
    let original_xmas_count = count(&input);

    let rotated_input = rotate_string(&input);
    let rotated_xmas_count = count(&rotated_input);

    let (main_d, sub_d) = to_diagonals(&input);
    let main_d_count = count(&main_d);
    let sub_d_count = count(&sub_d);

    println!();
    // println!("horizontal_counts: {horizontal_counts}");
    // println!("vertical_counts: {vertical_counts}");
    // println!("main_d: {main_d_count}");
    // println!("sub_d: {sub_d_count}");
    println!("horizontal {}: \n{}", original_xmas_count, input);
    println!();

    println!("vertical {}: \n{}", rotated_xmas_count, rotated_input);
    println!();

    println!("main_d {}: \n{}", main_d_count, main_d);
    println!();

    println!("sub_d {}: \n{}", sub_d_count, sub_d);

    original_xmas_count + rotated_xmas_count + main_d_count + sub_d_count
}

fn pattern_mas(matrix: &Vec<Vec<char>>, anchor: (usize, usize)) -> i32 {
    let i = anchor.0;
    let j = anchor.1;

    // i - строка, j - столбец
    let a = 'A';

    let left_up = matrix[i - 1][j - 1];
    let up = matrix[i - 1][j];
    let right_up = matrix[i - 1][j + 1];

    let left = matrix[i][j - 1];
    let right = matrix[i][j + 1];

    let left_down = matrix[i + 1][j - 1];
    let down = matrix[i + 1][j];
    let right_down = matrix[i + 1][j + 1];

    
    let mut count = 0;
    let l1 = String::from_iter(vec![left_up, a, right_down]);
    let l2 = String::from_iter(vec![left_down, a, right_up]);
    if (l1 == "MAS" || l1 == "SAM") && (l2 == "MAS" || l2 == "SAM") {
        count += 1;
    }

    if count > 0 {
        println!("---[{i}][{j}]---");
        println!("{left_up}{up}{right_up}");
        println!("{left}{a}{right}");
        println!("{left_down}{down}{right_down}");
        println!("------------");
        println!("{l1} {l2}");
        println!("count: {count}\n\n");
    }
    count
}

fn part_2(input: String) -> i32 {
    // Найти все буквы A начиная от [1...^1], т.е. с отступом в одну букву по краям
    // после чего перебрать элементы, которые находятся по диагонали (применить некую маску)
    let matrix_chars: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();

    let mut count = 0;
    for i in 1..(matrix_chars.len() - 1) {
        for j in 1..(matrix_chars[i].len() - 1) {
            if matrix_chars[i][j] == 'A' {
                count += pattern_mas(&matrix_chars, (i, j));
            }
        }
    }

    count
}
