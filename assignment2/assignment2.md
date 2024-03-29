
# Assignment 2

**Martin, Erik : 250660**  
**Seim, Håvard : 260699**  
**Group: L**  

**Code is available [here](https://github.com/eemrds/dat600-algorithms/blob/main/assignment2/assignment2.py)**


## Task 1
### Recursive Matrix Chain Multiplication
*Followed algorithm from *Introduction to Algorithms* and this [video](https://youtu.be/zQrR8t7urEE)*
The chain matrix multiplication problem uses a table to store the optimal costs of multiplying a chain of matrices. The optimal cost is the minimum number of scalar multiplications needed to compute the product.

Using this table and the recursive matrix chain multiplication strategy.
For instance:
Let a matrix chain be:
| A1  | A2  | A3  | A4  |
|-----|-----|-----|-----|
| 2x3 | 3x4 | 4x1 | 1x5 |

p = [2, 3, 4, 1, 5]

m[i, j] ={
    0, if i = j
    min(m[i, k] + m[k+1, j] + p[i-1]p[k]p[j]), if i < j
}

m[i, j] = min(m[i, k] + m[k+1, j] + p[i-1]p[k]p[j])


| m | 0 | 1 | 2  | 3  | 4  |
|---|---|---|----|----|----|
| 0 | 0 | 0 | 0  | 0  | 0  |
| 1 | 0 | 0 | 24 | 18 | 28 |
| 2 | 0 |   | 0  | 12 | 27 |
| 3 | 0 |   |    | 0  | 20 |
| 4 | 0 |   |    |    | 0  |

| s | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 3 |
| 2 | 0 |   | 0 | 2 | 2 |
| 3 | 0 |   |   | 0 | 3 |
| 4 | 0 |   |   |   | 0 |

l=2
min {
    k=1: m[1, 2] = m[1, 1] + m[2, 2] + p[0]*p[1]*p[2] = 0 + 0 + 2*3*4 = 24
    k=2: m[2, 3] = m[2, 2] + m[3, 3] + p[1]*p[2]*p[3] = 0 + 0 + 3*4*1 = 12 -- best
    k=3: m[3, 4] = m[3, 3] + m[4, 4] + p[2]*p[3]*p[4] = 0 + 0 + 4*1*5 = 20
}

l=3
min {
    m[1, 3] = min {
        k=1: m[1, 1] + m[2, 3] + p[0]*p[1]*p[3] = 0 + 12 + 2*3*1 = 18 -- best
        k=2: m[1, 2] + m[3, 3] + p[0]*p[2]*p[3] = 24 + 0 + 2*4*1 = 32
    },
    m[2, 4] = min {
        k=1: m[2, 2] + m[3, 4] + p[1]*p[2]*p[4] = 0 + 20 + 3*4*5 = 80
        k=2: m[2, 3] + m[4, 4] + p[1]*p[3]*p[4] = 12 + 0 + 3*1*5 = 27 -- best
    }
}

l=4
min {
    m[1, 4] = min {
        k=1: m[1, 1] + m[2, 4] + p[0]*p[1]*p[4] = 0 + 27 + 2*3*5 = 57
        k=2: m[1, 2] + m[3, 4] + p[0]*p[2]*p[4] = 24 + 20 + 2*4*5 = 68
        k=3: m[1, 3] + m[4, 4] + p[0]*p[3]*p[4] = 18 + 0 + 2*1*5 = 28 -- best
    }
}

The optimal cost is 28 and the optimal k value is 3. This means that the optimal way to multiply the matrices is (A1A2A3)A4.



### Dynamic Matrix Chain Multiplication
*Followed algorithm from *Introduction to Algorithms* and this [video](https://www.youtube.com/watch?v=eKkXU3uu2zk)*

The dynamic programming approach of matrix chain multiplication is to find what the 
best order of adding parenthesis to a chain of matrices is. The optimal cost is stored
in one table (m) and the k value that gives the optimal cost is in another (s).

When computing the optimal cost dynamically we start of with an empty table and fill it.
The rows and columns are the number n of matrices in the chain + 1. The diagonal, row 0 and 
column 0 are always 0. We want to find the optimal cost which will be stored in the top 
right (not row 0).

| m | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 |   |   |   |
| 2 | 0 |   | 0 |   |   |
| 3 | 0 |   |   | 0 |   |
| 4 | 0 |   |   |   | 0 |

| s | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 |   |   |   |
| 2 | 0 |   | 0 |   |   |
| 3 | 0 |   |   | 0 |   |
| 4 | 0 |   |   |   | 0 |


### Is there a greedy approach?
According to [wikipedia](https://en.wikipedia.org/wiki/Matrix_chain_multiplication#Hu_&_Shing), 
there is are two greedy approaches. One by Nimbark, Gohel, and Doshi which is for some
matrix chains unfortunately fails to give the optimal solution. Another is by Hu and Shing
which achieves O(nlogn) time complexity.



## Task 2
### Knapsack 0/1
The knapsack 0/1 is a problem where you have a collection of items. Each item has a carry weight and a price. Your goal is to maximize the total price while not going over the max carry
weight. If for example you have 4 items:
| Item   | Weight | Price |
|--------|--------|-------|
| Phone  | 1      | 2     |
| Camera | 2      | 3     |
| Laptop | 3      | 4     |
| TV     | 4      | 5     |

The max carry weight is 6. The optimal solution is to take the phone, camera and laptop, which gives a total price of 9 and a total weight of 6. A greedy solution would be to take the TV and camera, which gives a total price of 8 and a total weight of 6. 

A dynamic programming solution is to store the optimal price for each item and each weight in a table. Then sorting the input p by weight and calculating the optimal price for each row.
The columns are weight and rows are items.

|   | Item   | Weight | Price |
|---|--------|--------|-------|
| 1 | TV     | 4      | 5     |
| 2 | Laptop | 3      | 4     |
| 3 | Camera | 2      | 3     |
| 4 | Phone  | 1      | 2     |

The first row and column is always empty. The second row is the optimal price for the first item for each weight.

row 1. We only have the TV with a weight of 4 and a price of 5.


|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | Optimal Items         |
|---|---|---|---|---|---|---|---|-----------------------|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |                       |
| 1 | 0 | 0 | 0 | 0 | 5 | 5 | 5 | TV                    |
| 2 | 0 | 0 | 0 | 4 | 5 | 5 | 5 | TV                    |
| 3 | 0 | 0 | 3 | 4 | 5 | 7 | 8 | TV, Camera            |
| 4 | 0 | 2 | 3 | 5 | 6 | 7 | 9 | Camera, Laptop, Phone |

With a dynamic approach we can see that the optimal price for the max carry weight is 9.

### Fractional Knapsack
Fractional knapsack is a much simpler problem. It has the same idea as knapsack 0/1, but you
are now allowed to take fractions of items. Meaning if there for instance was a gold bar, 
you could take a part of it and leave the rest. Here a greedy algorithm would be very suitable.

The algorithm would sort the items by what the most is the most valuable per the weight.
It would then take as much as possible of the most valuable items per weight.

| Item       | Weight | Price | Value/Weight |
|------------|--------|-------|--------------|
| Gold bar   | 8      | 400   | 400/8 = 50   |
| Silver bar | 6      | 180   | 180/6 = 30   |
| Bronze bar | 3      | 90    | 90/3 = 30    |
| Iron bar   | 10     | 100   | 100/10 = 10  |

Max carry weight is 12. The optimal solution is to take all the gold + 2/3 of the silver, then leave the rest. This gives a total price of 400 + 120 = 520 and a total weight of 12. This is the optimal solution and a greedy algorithm would find this solution.



## Task 3
*Followed algorithm from *Introduction to Algorithms*
### Greedy solution for coin change

The greedy algorithm iterates through the coins in the list starting at the largest coin. For each coin it adds the coin to the sum and result as long as it does not exceed the target value $N$. When the sum has reached target $N$ it breaks the for loop and returns the resulting list of coins.

### Solution that accomodates any coin system
The bottom-up algorithm uses a list of size $N$ that calculates the smallest amount of steps to reach value every value from $1$ to $N$. At each step "steps[i]", one calculates if the step value at "steps[i-coin] + 1" is lower and in that case set it as the new step value with the current coin stored at "coin_used[i]". Finally the "coin_used" list is used to build the result list. 

### Norwegian coin system
The norwegian coin system is a greedy one, due to the fact that every coin will factor into all coins that are larger than itself i.e. 5 is a factor of 10 and 20, meaning that the largest available coin will always be the best option. This would render the bottomup_coins() excessive in the case of the norwegian coin system, as the greedy algorithm guarantees the optimal solution. One would assume most coin systems are greedy out of convenience.

### Running time
The greedy algorithm iterates through each coin, and enters a while loop that adds to the result list if favorable. We can say that what happens for each coin takes $O(1)$ time, while iteration through coins takes $O(n)$ times, making the run time $O(n)$.
The bottom-up algorithm similarly iterates through each coin, yet does it for value $1$ to $N$. With the amount of coins labeled as $n$, the algorithm runtime is $O(n*N)$.