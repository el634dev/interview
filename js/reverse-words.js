// Reverse Words in a String

// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

// Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only 
// have a single space separating the words. 
// Do not include any extra spaces.


const reverseWords = function(s) {
    // Assign the length of s to start(our variable)
    let start = s.length;
    // Assign the 0 to end(our variable)
    let end = 0;
    // Assign the "" to reversed(our variable)
    let reversed = "";

    // Loop through while start does not equal end
    while (start !== end) {
        // Assign end with the value of start decremented by 1
        end = --start;
        // Loop through while end is greater than or equal to 0 and
        // return a new string at the given index if the type and value is equal to an empty string
        while (end >= 0 && s.charAt(end) === " ") {
            // Decrement end by 1
            end--;
        }

        // Assign start to end
        start = end;
        // Loop through while start is greater than 0 and
        // return a new string at the given index if the type and value does not equal to an empty string
        while (start >= 0 && s.charAt(start) !== " ") {
             // Decrement start by 1
            start--;
        }
        // Add the value returned from the partfrom the start index up to and excluding the end index, 
        // incremented by 1 and an empty string to reversed (" ")
        reversed += s.substring(++start, ++end) + " ";
    }

    // Trim or remove the whitespace
    return reversed.trim();
};