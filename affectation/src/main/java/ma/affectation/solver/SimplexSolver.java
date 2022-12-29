package ma.affectation.solver;

public class SimplexSolver {

    int row;
    int col;
    float[][] MatriceOptimis = new float[row][]; // create a 2d array

    boolean solutionIsUnbounded;
    int pivotRow;



    public void simplex(int NbConstraint, int NbVariable) {
        row = NbConstraint + 1; // row number + 1
        col = NbVariable + 1;   // column number + 1
        float[][] M = new float[0][];

        // initialize references to arrays
        for (int i = 1; i < row + 1; i++) {
            if (col + 1 - 1 >= 0) System.arraycopy(M[i - 1], 0, MatriceOptimis[i], 1, col + 1 - 1);
        }
    }
        /*
         * M= { 1,1,3
         * 1,2,4
         * 2,3,0}
         */
        // computes the val of the simplex tableau
        // should be use in a loop to continously compute until
        // an optimal solution is found

    private float[] calculateRatios(int column) {
        float[] positiveEntries = new float[row];
        float[] res = new float[row];

        int allNegativeCount = 0;
        float b;

        for (int i = 1; i < row; i++) {
            b = MatriceOptimis[i][column];
            if (b > 0) {
                positiveEntries[i] = b;
            } else {
                positiveEntries[i] = 0;
                allNegativeCount++;
            }
            // System.out.println(positiveEntries[i]);
        }

        if (allNegativeCount == row)
            solutionIsUnbounded = true;
        else {
            for (int i = 1; i < row; i++) {
                float val = positiveEntries[i];
                if (val > 0) {
                    res[i] = MatriceOptimis[i][col - 1] / val;
                }
            }
        }

        return res;
    }

        // finds the next entering column
    private int ColoneNg() {
        float[] val = new float[col];
        int localiser = 0;
        float a;
        int pos, count = 0;
        for (pos = 0; pos < col - 1; pos++) {
            if (MatriceOptimis[row - 1][pos] < 0) {
                //System.out.println("negative value found");
                count++;
            }
        }

        if (count > 1) {
            for (int i = 1; i < col - 1; i++) {
                a = MatriceOptimis[row - 1][i];
                val[i] = Math.abs(a);
            }

        } else localiser = count;

        return localiser;
    }

    public ERROR compute() {
        // step 1
        if (CheckOptimality()) {
            return ERROR.IS_OPTIMAL; // solution is optimal
        } else {
            int pivotColumn = ColoneNg();
            // find the entering column

            System.out.println("Pivot : " + pivotColumn);

            // find departing value
            float[] ratios = calculateRatios(pivotColumn);
            if (solutionIsUnbounded == true) {
                return ERROR.UNBOUNDED;
            } else {
                // form the next tableau
                formNextTableau(pivotRow, pivotColumn);

                // since we formed a new table so return NOT_OPTIMAL
                return ERROR.NOT_OPTIMAL;
            }
        }
    }

    private void formNextTableau(int pivotRow, int pivotColumn) {
        float[][] MatriceOptimis = new float[0][];
        float[][] pivotValue = new float[0][];
        int i, j;
        for (j = 0; j < pivotColumn; j++) {
            for (i = 0; i < pivotRow; i++) {
                pivotValue[i][j] = MatriceOptimis[pivotRow][pivotColumn];
            }
        }

        float[] pivotRowVals = new float[row];
        float[] pivotColumnVals = new float[col];
        float[] rowNew = new float[col];

        // divide all entries in pivot row by entry inpivot column
        // get entry in pivot row

        for (j = 1; j < col + 1; j++) {
            System.arraycopy(pivotValue[pivotRow][j], 0, pivotRowVals, 0, col);
        }
        // get entry inpivot colum
        for (i = 1; i < row; i++)
            pivotColumnVals[i] = MatriceOptimis[i][pivotColumn];

        // divide val in pivot row by pivot value
        for (i = 1; i < row + 1; i++)
            rowNew[i] = pivotRowVals[i] / pivotValue[i][pivotRow];

        // subtract from each of the other rows
        for (i = 0; i < row + 1; i++) {
            if (i != pivotRow) {
                for (j = 1; j < col + 1; j++) {
                    float c = pivotColumnVals[i];
                    MatriceOptimis[i][j] = MatriceOptimis[i][j] - (c * rowNew[j]);
                }
            }
        }

        // replace the row
        for (j = 1; j < col + 1; j++) {
            System.arraycopy(rowNew, 0, MatriceOptimis[pivotRow][j], 0, rowNew.length);
        }

    }

    // calculates the pivot row ratios

    // finds the smallest value in an array
    public int findSmallestValue(float[] data) {
        float minimum;
        int c, location = 0;
        minimum = data[0];

        for (c = 1; c < data.length; c++) {
            if (data[c] > 0) {
                if (Float.compare(data[c], minimum) < 0) {
                    minimum = data[c];
                    location = c;
                }
            }
        }

        return location;
    }

    public boolean CheckOptimality() {
        boolean IsOptimal = false;
        int vCount = 0;
        float val2;

        for (int j = 0; j < col - 1; j++) {
            val2 = MatriceOptimis[row - 1][j];
            if (val2 >= 0) {
                vCount++;
            }
        }

        if (vCount == col - 1) {
            IsOptimal = true;
        }

        return IsOptimal;
    }

}

