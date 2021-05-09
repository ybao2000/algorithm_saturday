import java.util.*;

public class Codeforces710B {
  static int n;
  static long[] x;

  static long dist(long p){
    long d= 0;
    for (int i=0; i<n; i++){
      d += Math.abs(x[i] - p);
    }
    return d;
  }
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    n = Integer.parseInt(in.nextLine());
    x = new long[n];
    long p_left = 1000000000;
    long p_right = -1000000000;
    String[] vals = in.nextLine().split(" ");
    for (int i=0; i<n; i++){
      x[i] = Long.parseLong(vals[i]);
      if (x[i] < p_left) p_left = x[i];
      if(x[i] > p_right) p_right = x[i];
    }
    long ans = 0;
    while (p_left <= p_right)
    {
      long p_mid = (p_left + p_right)/2;
      long t_mid = dist(p_mid);
      long t_mid_prev = dist(p_mid-1);
      if (t_mid >= t_mid_prev){
        p_right = p_mid - 1;
      }
      else {
        long t_mid_next = dist(p_mid + 1);
        if (t_mid <= t_mid_next){
          ans = p_mid;
          break;
        }
        else{
          p_left = p_mid + 1;
        }
      }
    }
    System.out.println(ans);
  }
}