---
title: "SCRAPBOOK"
weight: 1000
---

# SCRAPBOOK
{{< a_noter>}}
Cette page est un brouillon pour tester des snippets, des commandes, des idées, etc. Elle n'est pas destinée à être lue par les étudiants.
{{< /a_noter>}}

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_00.00_SCRAPBOOK_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
  float a = 0.0f;
  printf("a = %.17g\n", a);
  a += 0.1f;
  printf("a = %.17g\n", a);
  a += 0.1f;
  printf("a = %.17g\n", a);
  a += 0.1f;
  printf("a = %.17g\n", a);
  a -= 0.1f;
  printf("a = %.17g\n", a);
  a -= 0.1f;
  printf("a = %.17g\n", a);
  a -= 0.1f;
  printf("a = %.17g\n", a);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
a = 0
a = 0.10000000149011612
a = 0.20000000298023224
a = 0.30000001192092896
a = 0.20000001788139343
a = 0.10000001639127731
a = 1.4901161193847656e-08
```
<p class="run-info">Compiled and executed on 2026-09-18 12:43 from 18f0dd4.</p>
<!-- SNIPPET:END -->

