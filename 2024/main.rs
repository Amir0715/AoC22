use itertools::Itertools;

mod task_1;
mod task_2;
mod task_3;
mod task_4;
mod task_5;
mod task_6;

fn main() {
    let mut multi_prod = (0..3).map(|i| 0..i)
        .multi_cartesian_product();
    
    // task_1::solution();
    //task_2::solution();
    // task_3::solution();
    // task_4::solution();
    // task_5::solution();
    task_6::solution();
}
