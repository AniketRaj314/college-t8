
import java.util.*;

colsass NQueen {
    static int N = 4;

    static int[] left_diag = new int[30];

    static int[] right_dia = new int[30];

    static int[] cols = new int[30];

    static void printAnswer(int board[][]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                System.out.printf(" %d ", board[i][j]);
            System.out.printf("\n");
        }
    }

    static boolean solveNQueen(int board[][], int col) {
        if (col >= N)
            return true;

        for (int i = 0; i < N; i++) {

            if ((left_diag[i - col + N - 1] != 1 && right_dia[i + col] != 1) && cols[i] != 1) {
                board[i][col] = 1;
                left_diag[i - col + N - 1] = right_dia[i + col] = cols[i] = 1;

                if (solveNQueen(board, col + 1))
                    return true;
                board[i][col] = 0; // BACKTRACK
                left_diag[i - col + N - 1] = right_dia[i + col] = cols[i] = 0;
            }
        }

        return false;
    }

    static boolean solveNQ() {
        int board[][] = { { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 } };

        if (solveNQueen(board, 0) == false) {
            System.out.printf("Solution does not exist");
            return false;
        }

        printAnswer(board);
        return true;
    }

    // Driver Code
    public static void main(String[] args) {
        solveNQ();
    }
}

// This code is contributed by Princi Singh
