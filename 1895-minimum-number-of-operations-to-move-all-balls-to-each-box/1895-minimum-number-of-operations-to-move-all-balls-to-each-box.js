/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
    let ans = [];
    for (let i = 0; i < boxes.length; i++){
        ans.push(0);
    }
    for (let i = 0; i < boxes.length; i++){
        for (let j = 0; j < boxes.length; j++){
            if (boxes[j] == '1'){
                ans[i]+=Math.abs(j-i);
            }
        }
    }
    return ans;
    
};