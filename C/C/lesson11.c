#include <stdio.h>

int main() {
	int x = 258;
	// &, |
	// we are familiar with && and ||

	// >>, <<
	// << - �������� ����� �� 2
	// >> - ����� ����� �� 2 ������
	while (x > 0) {
		printf("%d\n", x & 1); // ��������� ����������
		x = x >> 2;
	}
	//printf("%d", x & 1); // ��������� ����������

	return 0;
}