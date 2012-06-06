/* Palindrome program */

#include<stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
  if (argc > 1) {
    int i; 
    int len = strlen(argv[1]);
    for (i = 0; i < len/2; i++) {
      if (argv[1][i] != argv[1][len - i - 1]) {
     	printf("Not a palindrome.\n");
        return 0;
	  }
    }
    printf("This is a palindrome.\n");
  }
  return 0;
}
