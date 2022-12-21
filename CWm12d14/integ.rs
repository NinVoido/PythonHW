const DX: f64 = 1e-8;

fn f(x: f64, a: [f64;3]) -> f64 {
    return a[0]*x*x + a[1]*x + a[2]
}

fn integ(f: fn(f64) -> f64, x: f64) -> f64 {
    return (f(x) + f(x+DX))/2.0*DX
}

fn main() {
    let my_fn = |x| f(x, [1.0, 0.0, 0.0]);
    let mut sum = 0.0;
    let mut curx = 0.0;
    while curx < 1.0 {
        sum += integ(my_fn, curx);
        curx += DX;
    }
    println!("{}", sum);
}
