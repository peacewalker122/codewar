// https://www.codewars.com/kata/514b92a657cdc65150000006/train/cpp
//
int solution(int number) {
  int counter = 0;
  for (int i = 3; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      counter += i;
    }
  }

  return counter;
}
