//Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

//       Return your answer as a number.
package Java;

import java.util.ArrayList;
import java.util.List;

public class MixedSum {
    /*
     * Assuming input will be only of Integer o String type, first we have to transform all the string elements in int
     elements and store them in a new list (.add method)
     */
    public int sum(List<?> mixed) {
        ArrayList<Integer> newList = new ArrayList<>();
        int i;
        // since we don't know which element is a string or an int, we are going to go through the list
        for (i = 0; i < mixed.size(); i++) {
            //transforming string items on the list in int items
            if (mixed.get(i) instanceof String) {
                int j = Integer.parseInt((String) mixed.get(i));
                newList.add(j);
                // the else condition is for the items which already are int
            } else {
                newList.add((Integer) mixed.get(i));
            }
        }
        // finally, we are going to sum all the numbers in the list
        int total = newList.stream().mapToInt(Integer::intValue).sum();
        return total;

    }
}

