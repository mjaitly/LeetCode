import javafx.util.Pair;
import java.util.*;

class Office_N {
    // W for width, H for height, N for no of offices to build
    int W, H, N;

    // dx and dy value together gives (x,y)
    // which helps to move in 4 adjacent cells
    // Right (1,0)
    // Left (-1,0)
    // Down (0,1)
    // Up (0,-1)
    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};
    Map<String, Integer> dp = new HashMap<>();

    int[][] grid;

    // Constructor will set the values and clear the hashmap.
    public Office_N(int w, int h, int n) {
        W = w;
        H = h;
        N = n;
        dp.clear();
        grid = new int[W][H];

        for (int[] r : grid) {
            Arrays.fill(r, 0);
        }
    }

    // We convert the 2D array of W*H into 1D array in Row Order (if square matrix or Width is less),
    // or Column Wise (if Height is less)
    // BitMask holds the bits 0 empty spots, and 1 for where offices are present
    // Left means how many offices are still left to be built
    public int solve(int[][] grid, int left) {

        // If no more offices are left to be built, get the maximum distance for this scenario
        if (left == 0) {
            return bfs(grid);
        }

        StringBuilder k = new StringBuilder();

        for (int i = 0; i < W; i++) {
            for (int j = 0; j < H; j++) {
                if (grid[i][j] == 1) {
                    k.append(i + ":" + j + "::");
                }
            }
        }

        k.append("#" + left);
        // if the current scenario along with offices left are already processed, return the result
        String key = k.toString();
        if (dp.containsKey(key)) {
            return dp.get(key);
        }

        int[][] gridtemp = new int[W][H];
        for (int i = 0; i < W; i++) {
            for (int j = 0; j < H; j++) {
                gridtemp[i][j] = grid[i][j];
            }
        }

        //  We are trying every possible scenario to build offices in the given grid
        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < W; i++) {
            for (int j = 0; j < H; j++) {
                // If no office present in (i,j)th location, put one office there and check the minimum distance for that scenario
                if (gridtemp[i][j] == 0) {
                    gridtemp[i][j] = 1;
                    int val = solve(gridtemp, left - 1);
                    minDist = Math.min(minDist, val);
                    gridtemp[i][j] = 0;
                }
            }
        }

        // Store the min distance possible for the current scenario
        dp.put(key, minDist);
        return minDist;
    }

    // This function gives the maximum distance from all the empty spots to the offices for a given case of scenario
    private int bfs(int[][] grid) {
        // get a distance matrix with initial values as -1
        int[][] dist = new int[W][H];
        for (int[] row : dist)
            Arrays.fill(row, -1);

        int maxDist = 0;
        // Queue for processing the cells in Bredth-First-Search order.
        Queue<Pair<Integer, Integer>> Q = new LinkedList<>();

        // if office is present at (i,j)th location, the distance is 0, and put the (i,j) pair in Queue
        for (int i = 0; i < W; i++) {
            for (int j = 0; j < H; j++) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    Q.add(new Pair<>(i, j));
                }
            }
        }


        while (!Q.isEmpty()) {
            Pair<Integer, Integer> kv = Q.poll();
            int x = kv.getKey();
            int y = kv.getValue();

            // Get maximum distance for (i,j)th location
            maxDist = Math.max(maxDist, dist[x][y]);

            // Process all adjacent cells
            for (int d = 0; d < dx.length; d++) {
                int xNew = x + dx[d];
                int yNew = y + dy[d];

                // if the adjacent cell is within grid boundary, and is not yet processed,
                // set the max dist of he adjacent cell 1 more than the (i,j)th cell
                // add the adjacent cell to queue
                if (xNew >= 0 && xNew < W && yNew >= 0 && yNew < H && dist[xNew][yNew] == -1) {
                    dist[xNew][yNew] = dist[x][y] + 1;
                    Q.add(new Pair<>(xNew, yNew));
                }
            }
        }

        return maxDist;
    }

    public static void main(String[] args) {
        Office_N ofc = new Office_N(4, 4, 3);
        int res = ofc.solve(ofc.grid, ofc.N);
        System.out.println(res);
    }
}