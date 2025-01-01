/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    let zeroes = 0;
    let ones = 0;
    let n = s.length;
    let ans = 0;
    for (let i = 0; i < n; i++){
       
        if (s[i] == '1') 
        {
   
            ones+=1
        }
    }
    
    for (let i = 0; i < n-1; i++){
        if (s[i] == '0'){
            zeroes+=1
            
        }else{
            ones-=1
        }
        ans = Math.max(ans,zeroes+ones)
       
    
    }
   
    return ans;
    
};