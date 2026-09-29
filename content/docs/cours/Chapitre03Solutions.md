---
title: "Chapitre 3 : solutions"
draft: true
weight: 21
---
# Chapitre 3 : solutions

## Solutions exercices

{{< pdf src="/pdfs/1242.1.03_Operateurs_Correction.pdf" >}}

### `1242.1_03.01_Operators`

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exercices_03.01_Operators_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
#include <float.h>
#include <math.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
  // EXERCICE 1
  {
    printf("EXERCICE 1\n");
    int memory = 42;
    memory += 1;

    int word = 42;
    word *= 8;

    int currency = 42;
    currency -= 1;

    int a = 42;
    int b = 2;
    a %= b;

    int part = 42;
    int nb_persons = 4;
    part /= nb_persons;

    int x = 10;
    int y, z;
    x *= y = z = 4;
    printf("x=%d y=%d z=%d\n", x, y, z);
  }

  // EXERCICE 2
  {
    // a)
    printf("EXERCICE 2a\n");
    int n = 5, p = 9;
    float x;
    x = p / n;
    printf("x=%f\n", x);
    x = (float)p / n;
    printf("x=%f\n", x);
    x = (p + 0.5) / n;
    printf("x=%f\n", x);
    x = (int)(p + 0.5) / n;
    printf("x=%f\n", x);

    // b)
    printf("EXERCICE 2b\n");
    int a;
    a = 10 % 10;
    printf("a=%d\n", a);
    a = 5 % 10;
    printf("a=%d\n", a);
    // ERROR: modulo zero
#if ACTIVATE_WARNINGS_AND_ERRORS
    a = 10 % 0;
    printf("%d\n", a);
#endif
    a = 0 % 10;
    printf("a=%d\n", a);
  }

  // EXERCICE 3
  {
    printf("EXERCICE 3\n");
    int x = 2, y = 1, z = 3;
    z += -x++ + ++y;
    printf("%d %d %d\n", x, y, z);
  }

  // EXERCICE 4
  {
    // a)
    printf("EXERCICE 4a\n");
    bool result = 3 <= 2 - 1;
    printf("result=%s\n", result ? "true" : "false"); // To display "true" or "false"
    result = 3 * (4 > 4) + 2.5;
    printf("result=%s\n", result ? "true" : "false");
    result = (4 == 5.1) / 2 + 1;
    printf("result=%s\n", result ? "true" : "false");
    result = true && false || true;
    printf("result=%s\n", result ? "true" : "false");
    int n = 42;
    result = 3 + (n > n - 1);
    printf("result=%s\n", result ? "true" : "false");
    result = !true && false || !false;
    printf("result=%s\n", result ? "true" : "false");

    // b)
    printf("EXERCICE 4b\n");
    int x = 5;
    result = (x >= 5) && (x <= 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 10;
    result = (x >= 5) && (x <= 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 7;
    result = (x >= 5) && (x <= 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 4;
    result = (x >= 5) && (x <= 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 11;
    result = (x >= 5) && (x <= 10);
    printf("result=%s\n", result ? "true" : "false");

    // c)
    printf("EXERCICE 4c\n");
    x = 5;
    result = (x < 5) || (x > 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 10;
    result = (x < 5) || (x > 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 7;
    result = (x < 5) || (x > 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 4;
    result = (x < 5) || (x > 10);
    printf("result=%s\n", result ? "true" : "false");
    x = 11;
    result = (x < 5) || (x > 10);
    printf("result=%s\n", result ? "true" : "false");
  }

  // EXERCICE 5
  {
    // a)
    {
      printf("EXERCICE 5a\n");
      int n = 5, p = 9;
      int q;
      q = n < p; /* 1 */
      printf("n=%d p=%d q=%d\n", n, p, q);
      q = n == p; /* 2 */
      printf("n=%d p=%d q=%d\n", n, p, q);
      q = p % n + (p > n); /* 3 */
      printf("n=%d p=%d q=%d\n", n, p, q);
    }

    // b)
    {
      printf("EXERCICE 5b\n");
      int n = 10, p = 5, q = 10, r;
      r = n == (p = q);
      n = p = q = 5;
      n += p += q;
      printf("n=%d p=%d q=%d r=%d\n", n, p, q, r);
    }

    // c)
    {
      printf("EXERCICE 5c\n");
      double a = 3.5 * 6;
      int b = 243 * -83;
      int c = (int)(20.35 * 24);
      int d = (int)85.35 * 2;
      int e = 'w' - 2024;
      char f = 23 / 9;
      printf("a=%lf b=%d c=%d d=%d e=%d f=%d \n", a, b, c, d, e, f);
    }

    // d) SEE correction

    // e)
    {
      printf("EXERCICE 5e\n");
      int x = 2;
      printf("x=%d\n", x);
      x = 3 + (3 > x);
      printf("x=%d\n", x);

      // FIXME: this is an undefined behavior
#if ACTIVATE_WARNINGS_AND_ERRORS
      x += x -= 2;
      printf("x=%d\n", x);
      x = (++x - 6) * 3;
      printf("x=%d\n", x);
#endif
      x *= (5 > x) * (3 + 23);
      printf("x=%d\n", x);
    }

    // f) SEE correction
  }

  // EXERCICE 6 A)
  {
    printf("EXERCICE 6A\n");
    unsigned char x = 0xAA; // 1010 1010

    printf("Masking %x\n", x);
    x = x | 0xC0; // x|=0xC0;
    printf("Masking the 2 most significant bits: %x\n", x);
    x = x & 0xFC; // x&=0xFC
    printf("Masking the 2 least significant bits: %x\n", x);
    x = (x >> 3) & 0x07;
    printf("Display bits 3, 4 and 5: %x\n", x);

    // In binary (bit shift, then masking to keep least significant bit, then print as integer)
    unsigned char bit3 = (x >> 0) & 0x01;
    unsigned char bit4 = (x >> 1) & 0x01;
    unsigned char bit5 = (x >> 2) & 0x01;
    printf("Display bits 3, 4 and 5 in binary = %d%d%d\n", bit5, bit4, bit3);
  }

  // EXERCICE 6 B) V1
  {
    printf("EXERCICE 6B V1\n");
    unsigned int x = 0x03020100;
    unsigned char b0, b1, b2, b3;
    unsigned int mask = 0xFF;

    b0 = ((x & mask));

    mask <<= 8;
    b1 = ((x & mask) >> 8);

    mask <<= 8;
    b2 = ((x & mask) >> 16);

    mask <<= 8;
    b3 = ((x & mask) >> 24);

    printf("b3:%X b2:%X b1:%X b0:%X\n", b3, b2, b1, b0);
  }

  // EXERCICE 6 B) V2
  {
      printf("EXERCICE 6B V2\n");
      unsigned int x = 0x03020100;
      unsigned char b0, b1, b2, b3;

      b0 = x;
      b1 = x >> 8;
      b2 = x >> 16;
      b3 = x >> 24;

      printf("b3:%X b2:%X b1:%X b0:%X\n", b3, b2, b1, b0);
  }

  // EXERCICE 7
  {
      printf("EXERCICE 7\n");
      // Integer overflow: INT_MAX + 1 = INT_MIN
      printf("INT_MAX: %d INT_MAX+1: %d\n", INT_MAX, INT_MAX + 1);
      printf("DBL_MAX: %g\n", DBL_MAX);
      // 1000 is NOT significant compared to DBL_MAX
      // DBL_MAX + 1000 == DBL_MAX
      printf("DBL_MAX+1000: %g\n", DBL_MAX + 1000);
      // => Infinity
      printf("DBL_MAX*2 : %g\n", DBL_MAX * 2);
#if ACTIVATE_WARNINGS_AND_ERRORS
      printf("q = 1/0: %f \n", 1 / 0);
      float q = 1.0f / 0;
      printf("q = 1.0f/0: %f \n", q);
      printf("1/q : %f \n", 1 / q);
      printf("q/q : %f \n", q / q);
#endif
      printf("sqrt(-1) : %f \n", sqrt(-1));
  }

  return 0;
}
```
<!-- SNIPPET:END -->

## Solutions Auto-évaluations
Pas d'auto-évaluation pour ce chapitre.
