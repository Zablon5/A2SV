/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
var findAndReplacePattern = function(words, pattern) {

    let ans = [];
    for (let i = 0; i < words.length; i++){
        if (check(words[i], pattern)){
            ans.push(words[i]);
        }
    }

    function check(word, pattern){
        let mp1 = {};
        let mp2 = {};
        for (let i = 0; i < word.length; i++){
            if (!(word[i] in mp1) && !(pattern[i] in mp2)){
                mp1[word[i]] = pattern[i]
                mp2[pattern[i]] = word[i]
            } 
            else{
                if (mp1[word[i]] != pattern[i] || mp2[pattern[i]] != word[i]){
                    return false;
                }
            }
            
        }
        return true;
    }
    return ans;
};