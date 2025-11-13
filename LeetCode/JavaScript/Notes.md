##### Kadane's Algorithm #####

Kadane's algorithm returns the maximum sum of a contiguous subarray. This means an array nested within an array. This algorithm is taking a subset of integer
values within the array, testing them against each other to find the subarray with the maximum sum instide of it.

In this example, were passing in a parameter nums thats the parent array. We define two arrays. The Max found so far, and the current maximum from add operations.
We're going to start at the beginning of the array, looping through every element in the array with a for loop. It's going to take i element from the array, add it to the CurrentMax, and append it as the value for MaxThusFar if its greater than the current MaxThusFar. The function then returns the highest value found within the array.

An example use case of this algorithm is to find the maximum sum of a contiguous subarray within an array.

######

var maxSubArray = function(nums) {
    let MaxThusFar = nums[0];
    let CurrentMax = nums[0];
    for (let i = 1; i < nums.length; i++) {
        CurrentMax = Math.max(nums[i], CurrentMax + nums[i]);
        MaxThusFar = Math.max(MaxThusFar, CurrentMax);
    }

    return MaxThusFar;
};

######

In this problem, we are tasked to find two numbers that complement each other to achieve a specific sum within an array. In this code, we are creating a map to store the values. We're then looping through every item in the array, defining the complement as the target number subtracted by the value at the array indice. We check the map for the complement, if it has it, we return it, move to the next array indice. If the map doesn't contain our number, we set it, then return it. If the array doesn't contain any complementary numbers for the goal, we return an empty list. 

###### Complimentary Sum ######

var twoSum = function(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return[map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
};


#####

##### Adding Two Linked-Lists ######

This code is a snippet example of how to add two different limked lists. We start my defining the list, getting the node values, initializing them, setting them to zero if they're undefined. After we grab the first node, we check the next node, if its null we stop, if not we move to the next one. We're grabbing the two linked lists in addTwoNumbers. We create a dummy head, initialize it to the first object in ListNode. Make the current node the DummyHead and make the carry for addition zero. While l1, l2, and carry aren't null values, add them. When l1 and l2 are empty, we initialize carry to the sum / 10 to carry over numbers for addition. We calculate our digit, add it to the current node, move to the next and repeat until the proess is done.

#####

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var addTwoNumbers = function(l1, l2) {

    let dummyHead = new ListNode(0);
    let current = dummyHead;
    let carry = 0;

    while (l1 !== null || l2 !== null || carry !== 0) {
        let sum = carry;

        if (l1 !== null) {
            sum += l1.val;
            l1 = l1.next;
        }

        if (l2 !== null) {
            sum += l2.val;
            l2 = l2.next;
        }

        carry = Math.floor(sum / 10);
        const digit = sum % 10;

        current.next = new ListNode(digit);
        current = current.next;
    }

    return dummyHead.next;
   
};

#####

##### Longest Substring Without Repeating Charcters #####



#####

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let SubStringMap = new Map();
    let left = 0;
    let maxLen = 0;
    let bestLen = 0;

    for (right = 0; right < s.length; right++) {
        const currItem = s[right];

        if (SubStringMap.has(currItem)) {
            left = Math.max(left, SubStringMap.get(currItem) + 1);
        }

        SubStringMap.set(currItem, right)

        const winLen = right - left + 1;
        if (winLen > bestLen) {
            bestLen = winLen;
            bestStart = left;
        }
    }

    return bestLen;
};

#####


#####

var findMedianSortedArrays = function(nums1, nums2) {
    const mergedArrays = nums1.concat(nums2);
    mergedArrays.sort((a, b) => a - b);
    const mid = Math.floor(mergedArrays.length / 2);

    if (mergedArrays.length % 2 === 0) {
        const number = (mergedArrays[mid - 1] + mergedArrays[mid]) / 2;
        return number;

    } else {
        const number = mergedArrays[mid];
        return number;
    }
};

#####

