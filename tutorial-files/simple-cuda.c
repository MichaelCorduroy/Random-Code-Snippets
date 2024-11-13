//simple CUDA file in C 

#include <stdio.h>
#include <stdlib.h>

__global__ void add(int *a, int *b, int *c) {
	*c = *a + *b;
} 

int main(void) {
	int a, b, c;
	int *d_a, *d_b, *d_c;
	int size = sizeof(int);
	a = 2;
	b = 7;
	
	cudaMalloc((void **)&d_a, size);
	cudaMalloc((void **)&d_b, size);
	cudaMalloc((void **)&d_c, size);

	cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
	

	for(int i = 0; i < 10; i++) {
		add<<<1,1>>>(d_a, d_b, d_c);
	}

	cudaMemcpy(d_c, &c, size, cudaMemcpyDeviceToHost);
	printf("%d\n", c);
	return 0;
}


