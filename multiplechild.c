#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
int main(void) {
  char name[10];
  int status = 0;
  pid_t child_pid, wpid;
  child_pid = fork();
  printf("\nPlease enter 4 names: ");
  for(int i = 1; i < 5; i++) { 
    if((child_pid = fork())== 0) {
      scanf("%s", name);
      printf("\nName is %s", name);
      exit(0);
    }
  }
  while ((wpid = wait (&status)) > 0);
   printf("\nJob is done.");
 
  return EXIT_SUCCESS;
}
