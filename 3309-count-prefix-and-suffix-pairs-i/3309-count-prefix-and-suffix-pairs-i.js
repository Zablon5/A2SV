/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) {
    let ans = 0;
    function isPrefix(str1, str2){
        let n = str1.length;
        let m = str2.length;
        if (n > m){
            return false;
        }
        for (let i = 0; i < n; i++){
            if (str1[i]!=str2[i]){
                return false;
            }
        }
        return true;

    }

    function isSuffix(str1, str2){
        let n = str1.length;
        let m = str2.length;
        if (n > m){
           
            return false;
        }
        
        for (let i = 0; i < n; i++){
            
            if (str1[n-1-i]!=str2[m-i-1]){
                    
                return false;
            }

        }
        return true;
    
        
    }

    for (let i = 0; i < words.length; i++){
        for (let j = i+1; j < words.length; j++){
            if (isPrefix(words[i], words[j]) && isSuffix(words[i], words[j])){
                ans++;
            }
        }
    }

    console.log(isSuffix("a","abb"));
    return ans;
    
};