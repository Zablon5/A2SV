/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    let ans = 0;
    for (let i = 0; i < words.length; i++){
        if (isPrefix(pref, words[i])){
            ans++;
        }
    }
    function isPrefix(pref, word){
        if (pref.length > word.length){
            return false;
        }
        else{
            return pref == word.substring(0, pref.length);
        }
    }
    return ans;
};