/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplitArray = function(nums) {
    let prefixSum = [0];
    let suffixSum = [0];
    let ans = 0;
    for (let i = 0; i < nums.length; i++){
        prefixSum.push(prefixSum[i] + nums[i]);
        suffixSum.push(suffixSum[i] + nums[nums.length -1 -i]);
    }
    for (let i = 0; i < nums.length - 1; i++){
        if (prefixSum[i+1] >= suffixSum[nums.length - 1 - i]){
            ans += 1;
        }

    }
    return ans;
};