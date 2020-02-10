#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Create 5 zombie processes
 *
 * Return: 0 integer
 */
int main(void)
{
	pid_t child_pid;
	int c = 5;

	while (c--)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %ld\n", (long)child_pid);
			sleep(0.5);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();

	return (0);
}

/**
 * infinite_while - Infinite while loop
 *
 * Return: 0 Integer.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
