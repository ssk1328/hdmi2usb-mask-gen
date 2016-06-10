#include <stdio.h>

#define HEIGHT 3
#define WIDTH 4
#define LENGTH HEIGHT*WIDTH

struct wipe {
	int count;
	int pixel;
	}; 
	
int main(){
	
	
	int image [HEIGHT][WIDTH] = { 	{1,1,1,1},
									{1,0,0,0},
									{1,1,1,1}  };

	int i;
	int j;
	int image_array[LENGTH];
	
	struct wipe wipe_1 [LENGTH];
	
	for ( i=0; i<HEIGHT; i++){
		for (j=0; j<WIDTH; j++){
//			image[i][j] = 1;
			printf("%d ", image[i][j]);
			image_array[i*WIDTH + j] = image[i][j] ;					
		}
		printf("\n");
	}

	for (i=0; i < LENGTH; i++){
		printf("%d ", image_array[i]);
		wipe_1[i].count = -1;		
		wipe_1[i].pixel = -1;		
	}

	int ptr= 0;
	
	printf("Initialized with %d " , wipe_1[LENGTH-1].pixel);
	

	for (i=0; i < HEIGHT*WIDTH ; i++){
		
		if (image_array[i] == wipe_1[ptr].pixel) {
			wipe_1[ptr].count = wipe_1[ptr].count + 1;
			}
		else {
			ptr = ptr+1;
			wipe_1[ptr].pixel = image_array[i];
			wipe_1[ptr].count = 1;
			}
	}

for (i = 0 ; i<ptr+1 ; i++){
	printf("\n");
	printf ("Encoded values are count: %d, pixel: %d", wipe_1[i].count, wipe_1[i].pixel );
	}


return 0;
}

