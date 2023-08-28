/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (value)=>{
            if (val!==value) throw new Error("Not Equal");
            else return true;
        },
        notToBe: (value)=>{
            if (val=== value) throw new Error("Equal");
            else return true;
        }
    }
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
