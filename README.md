[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11681141&assignment_repo_type=AssignmentRepo)
# CMPS 2200  Recitation 01

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):** Amara Midouhas 

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**For Linear Search, It would a key that is at the end of the list or do not exist at all. For example: [1,2,3,4,5] = 5 (5 is at the end) and [1,2,3,4,5] = 6 (6 is not in the list). This would be O(n). For Binary Search, the worst key would be if it was at the very beginning of the list or very end because that means there would be much time tken up doing comparisons, since you start in the middle. This would be O(logN)**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: For Linear Search, the best case would be if the key is at the beginning of the list so O(1) since the search only has to do one comparison.For example, [1,2,3,4,5] = 1 (1 is at the beginning). For Binary Search, the best case would be if the key was in the middle. For example, [1,2,3,4,5] = 3 (3 is in the middle). This would be O(1) because there is only one comparison**

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO: |        n |   linear |   binary |
        |----------|----------|----------|
        |       10 |    0.004 |    0.002 |
        |      100 |    0.004 |    0.003 |
        |     1000 |    0.042 |    0.005 |
        |    10000 |    0.566 |    0.016 |
        |   100000 |    4.595 |    0.024 |
        |  1000000 |  113.789 |    0.041 |
        | 10000000 | 1082.887 |    0.046 |**

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**They do match my results. For Linear Search, when n, the size, increases, the time increases as well. The running time is correlated with the size of n. When n was small, there was better running time. For Binary Search, when n increased, time increases as well but not as much or proportional with the size like in linear search. Therefore, even with a large dataset, binary search is the best because the time complexity is low compared to the time for large datasets like for linear search.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **It will be O(k*n) because O(n) is the worst-case time because it has to make many comparisons and since we are iterating over the list k times to makes those comparisons, you multiply the k*n**
  + For binary search? **It will be O(k*log2(n)) because the worst-case time complexity to divide and conquer a list is O(log2(n)) and since we are going through the list, you will multiply the number of times, k, by the worst-time complexity**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **Sorting then doing binary search is much more efficient then doing linear search without sorting because size and time are proportional. If you perform k>1 searches, the time complexity will be longer because it consantly has to look through an unsorted list. Doing binary search on a sorted list is much more effienct because previous k searches does not affect the time complexity the same. Doing k>1 searches, will increase the time but at a slower rate comparedc to linear search on a unsorted array. **

  

