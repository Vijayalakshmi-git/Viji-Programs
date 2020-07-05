// Function to check if the two given strings are an anagram of each other
var anagram = function(str1, str2) {

// if the length of two strings is same then the strings are anagrams else print false and return
    if (str1.length != str2.length) {
      console.log("anagram(" + str1 + "," + str2 + ") => false");
      return false;
    }

// splitting two strings, sorting and comparing
    str3 = str1.split("").sort().join("");
    str4 = str2.split("").sort().join("");

// check if each character of the two strings match each other else print false and return
    for (var i = 0; i < str3.length; i++) {
        if ((str3.charAt(i)) != (str4.charAt(i))) {
          console.log("anagram(" + str1 + "," + str2 + ") => false"); 
          return false;
        }
    }

// if each characters of each string matches with the other return true
    console.log("anagram(" + str1 + "," + str2 + ") => true");
    return true;
};

// calling function anagram with passing arguments
anagram("triangle","integral");
anagram("wool","howl");