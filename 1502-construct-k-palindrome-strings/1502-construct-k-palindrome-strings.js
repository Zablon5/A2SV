/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var canConstruct = function(s, k) {

    if (k > s.length){
        return false;
    }
    let counterMap = {};
    for (let i = 0; i < s.length; i++){
        if (s[i] in counterMap){
            counterMap[s[i]] += 1;
        }else{
            counterMap[s[i]] = 1;
        }
    }

    let oddCount = 0;
    for (c in counterMap){
        if (counterMap[c]%2 != 0){
            oddCount++;
        }
    }
    if (oddCount > k){
        return false;
    }
    else{
        return true;
    }
};