package one;

import java.util.Arrays;

public class test {
    public static String getType(Object test){
        return test.getClass().getName().toString();
    }
    public static void main(String[] args) {
        exam sum = new exam();
        int[] nums ={2, 7, 11, 15};
        int target = 9;
        int[] res = sum.twoSum(nums, target);
        System.out.printf(Arrays.toString(res));



    }
}
