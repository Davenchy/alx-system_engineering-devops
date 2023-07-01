#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - runs infinite loop
 * Return: zero
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - A program that forks 5 zombie processes and print their PIDs
 * Return: exit status code
 */
int main(void)
{
	int pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
	}

	return (infinite_while());
}
