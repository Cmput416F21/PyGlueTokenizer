public static int fibonacciOf ( int n ) {
  if ( n == 0 || n == 1 ) {
    return n ;
  }
  return fibonacciOf ( n - 1 ) + fibonacciOf ( n - 2 ) ;
}
