/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function(words, queries) {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let valid = [];
    let ans = [];
    let presm = [];
    function check(word){
        let n = word.length;
        if (vowels.includes(word[0]) && vowels.includes(word[n-1])){
            valid.push(word);
            return true;
        }
        
    }
   
    for (let i = 0; i < words.length; i++){
       if (check(words[i])){
         if (i==0){
           presm.push(1);
         }
         else{
            presm.push(1+presm[i-1])
         }

       }else if (i==0){
        presm.push(0)
       }
       else{
        presm.push(presm[i-1])
       }
    }
    for (let j = 0; j < queries.length; j++){
        let l = queries[j][0];
        let r = queries[j][1]
        if (valid.includes(words[l])){
            ans.push(1+presm[r]-presm[l])
        }else{
            ans.push(presm[r]-presm[l])
        }
    }
   
    return ans;
};