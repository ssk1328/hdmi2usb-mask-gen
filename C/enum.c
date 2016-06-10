#include <stdio.h>
#include <math.h>

enum wipe_style { 
	WIPE_HORIZOANTAL, 
	WIPE_VERTICAL,
	CHECKBOARD, 
	DIAGONAL_LEFT,
	DIAGONAL_RIGHT,	
	CLOCK_WIPE };

struct wipe {
	int count,
	int pixel
	};

struct wipe* generate_wipe(enum wipe_style type, int position, int length);


int main(){
	
    enum wipe_style wipet = WIPE_HORIZOANTAL;
    int mask_2D[HEIGHT][WIDTH];
    int diag = 
    int length = 100;
    int position = 30;
    int i,j;
    
	switch (wipet){
		
		case WIPE_HORIZOANTAL:
			for(i=0;i<HEIGHT; i++){
				for (j=0; j<WIDTH; j++){
					if (j< WIDTH*position/length){
						mask_2D[i][j] = 1;
					}
					else {
						mask_2D[i][j] = 0;
					}				
				}
			} 
		
		case WIPE_VERTICAL:
			for(i=0;i<HEIGHT; i++){
				for (j=0; j<WIDTH; j++){
					if (i< HEIGHT*position/length){
						mask_2D[i][j] = 1;
					}
					else {
						mask_2D[i][j] = 0;
					}				
				}
			} 		
			
		case DIAGONAL_LEFT:
			
			for(i=0;i<HEIGHT; i++){
				for (j=0; j<WIDTH; j++){
					if (i+j < (HEIGHT+WIDTH)*position/length){
						mask_2D[i][j] = 1;
					}
					else {
						mask_2D[i][j] = 0;
					}				
				}
			} 				
		
		case DIAGONAL_RIGHT:
			
			for(i=0;i<HEIGHT; i++){
				for (j=0; j<WIDTH; j++){
					if (i-j < ((HEIGHT+WIDTH)*position/length) - HEIGHT){
						mask_2D[i][j] = 1;
					}
					else {
						mask_2D[i][j] = 0;
					}				
				}
			} 						
	}	

return 0;
}
