/*
main.c
lab1_l

Created by PATRICIA MARIA DE OLIVEIRA on 02/01/2019.
Copyright © 2019 PATRICIA MARIA DE OLIVEIRA. All rights reserved.
 
This program read in two floating point matrices. The dimensions of the matrices are chosen
 by the user at run-time. The two matrices should be multiplied together ( assuming the dimensions are
 legal for multplication)
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int main() {
    
    srand((unsigned int)time(NULL));
    
    int r_m1=0, c_m1=0, r_m2=0, c_m2=0;  ;
    
    printf("Insert the size of the first matrix\n");
    printf("Rows: ");
    scanf("%d", &r_m1);
    printf("Columns: ");
    scanf("%d", &c_m1);
    printf("\nInsert the size of the second matrix\n");
    printf("Rows: ");
    scanf("%d", &r_m2);
    printf("Columns: ");
    scanf("%d", &c_m2);
    
    double matrix1[r_m1][c_m1], matrix2[r_m2][c_m2];
    int i, j;
    
    if (c_m1 != r_m2){
        printf("The matrices can't be multiplied with each other.\n");
    }else{
        /* generate floating point matrix 1 */
        for (i=0; i<r_m1; i++){
            for (j=0; j<c_m1; j++){
                matrix1[i][j] = (float)rand()/RAND_MAX;
            }
        }
        
        /* generate floating point matrix 2 */
        for (i=0; i<r_m1; i++){
            for (j=0; j<c_m1; j++){
                matrix2[i][j] = (float)rand()/RAND_MAX;
            }
        }
        
        /* multiplicating both floating point matrices 1 and 2 */
        int k=0;
        float sum=0.0, product[r_m1][c_m2];
        for ( i= 0; i < r_m1; i++) {
            for (j = 0; j < c_m2; j++) {
                for (k = 0; k < r_m2; k++) {
                    sum = sum + matrix1[i][k] * matrix2[k][j];
                }
                product[i][j] = sum;
                sum = 0.0;
            }
        }
        
       /* print the product of matrix 1 and matrix 2 */
        printf("\nThe product of matrix 1 and matrix 2 is:\n");
        for (i=0; i<r_m1; i++){
            for (j=0; j<c_m1; j++){
                printf("%lf\t", product[i][j]);
            }
        }
        
    }
    
   printf("\n\n");

    return 0;
}
