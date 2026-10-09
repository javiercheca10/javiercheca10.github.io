#include <stdio.h>
#include "platform.h"
#include "xil_printf.h"
#include <arm_neon.h>
#include "xtime_l.h"
#include <math.h>

#define N 8
#define SAMPLES 32

XTime begin_tick;
XTime end_tick;
XTime execution_ticks;
float execution_time_in_us;

const float h[N] = { -0.0010, 0.1219, 0.1862, 0.2429, 0.2429, 0.1862, 0.1219,
		-0.0010 };

void generate_signal(float x[], float omega) {
	for (int n = 0; n < SAMPLES; n++) {
		x[n] = cos(omega * n);
	}
}

void fir_filter_neon(float x[], float y[]) {
	for (int n = N - 1; n < SAMPLES; n += 4) {
		float32x4_t yn = vdupq_n_f32(0);
		for (int k = 0; k < N; k++) {
			float32x4_t hk = vdupq_n_f32(h[k]);
			float32x4_t xn = vld1q_f32(&x[n - k]);
			yn = vmlaq_f32(yn, hk, xn);
		}
		vst1q_f32(&y[n], yn);
	}
}

int main() {
	float x[SAMPLES], y[SAMPLES];
	float omega1 = 2 * M_PI / 16;

	generate_signal(x, omega1);

	XTime_GetTime(&begin_tick);

	fir_filter_neon(x, y);

	XTime_GetTime(&end_tick);

	execution_ticks = end_tick - begin_tick;
	execution_time_in_us = (float) (execution_ticks * 2.0 * 1000000)
			/ (float) XPAR_CPU_CORTEXA9_CORE_CLOCK_FREQ_HZ;

	printf("Output FIR (NEON paralelo):\n");
	for (int i = 7; i < SAMPLES; i++) {
		printf("y[%d] = %f\n", i, y[i]);
	}

	printf("\t\t-begin execution tick %llu\n", begin_tick);
	printf("\t\t-end execution tick %llu\n", end_tick);
	printf("\t\t-total execution ticks %llu\n", execution_ticks);
	printf("\t\t-execution time in microseconds %f\n", execution_time_in_us);

	return 0;
}