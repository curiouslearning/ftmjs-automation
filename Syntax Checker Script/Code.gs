function applyConditionalFormattingToSheets() {
  
 var spreadsheetIds = [
"1YzUqpj_ufTEU7d5yZSw0mdiVAfb9ohvuVT-DpEfU-R8",
"13WBY_oV_n1IlFKVZePIFU4CwQOoQcWywNqlbmw4AA0c",
"1uH4LSm9STsdjdK5B6Ve7we7TAub03qEY7dk0w_AweBI",
"1YlIFh-EYsfJ4boyMPy1qAigg2BRSwhUTq7Pl25OnX4M",
"1C_ulOSv7ZD9_z34MCZnZzxEyNjh7eyZDNuwT4rzl9Ao",
"1YoEqg_4S9PdJ8cJieszpQLXnm6kSVYxLoTEiGrBhmA4",
"1maGdcI2Ezz5Stld8OyHvTE-TeH2PiE_f8VRvcETSOOk",
"14GsDAQuo9eCr4VjbEK8EFi4OkGo5Hc-vRMz--ZjBAsQ",
"18wqbTN6CTxrM4OiPNLNuC1tiDjrolSkF3zocJTxil4s",
"1kNEpOaaJSk8AQaZQFFCRKw5DWTcR97euYvjIBtYKZNQ",
"1uehinoyQ5I4C01_RPt7bDkXg7cZxxWe3kFR6WRHRO50",
"1M8FHFtr1qh3pXGSb4vK1TKWWXyI7p2jfApVifkJtvfM",
"1Kr_EKMi9thIoMKUAIvqUEhJjcQmENAcTFqKhT5CjDyY",
"1AJ1hNSerM61GbJ9ytarojRe6_yhKHYMGqXBWNG4A7Qk",
"1AFHmCUeR6lsCQkMW0c_YQRhbNzvqbpY_EWPh8GEbAMs",
"1TpJ0x_mwRXd3kaXldAztQ3rKo0WxelQ43lTpt2f3hr8",
"16spQyKIcpSy0LCcECWvSDu9RoQX0tY248k37D1ZUVLY",
"1j6VEqx9rAJDvphd9peiPIQ5YwgixSCEmLgTrRRAJ06I",
"18PFjBL0zr6RvWOk629-sgRiTUuRxiQGykTSlnLHUjNg",
"1sFjQI7cQEBB6qgNYKKkKaRg_Tu-CrTB-JChXNl_Mohk",
"1wxGseq2_BI73OKOrFs2nJLNqcfkC1Q58HLo_VRHxRDs",
"1yNjw1NH-dQ1_C_PZkpUM5g6yeSwr5B2wr_Qkjy6y5ZE",
"13UpaHeyR-5-2wBfPex7xYXyQCoZZylv0My6llQjFHY8",
"1bi_rnXleqDoqhc8OOmYOSxdaMdFRFUNQSZl1DSwpFZQ",
"1ATwIeJ2UMue6DqF31r0tKIxNvV34ZhEilMzROR8V8fA",
"11rzGW7T5EpL86378bs9DGUgPOsItNSzRlGqMUYjMVCY",
"1SYe6bFNcn5WDIcmm92EOCnD7oFdAjVXe3ZsZC9wt7QI",
"1tVlve2A6kpbLKvoQkzcJF6_OQVdG8awFmJzCyRBLnlE",
"1koAhTJ28dswZIS4egQNLVgEpkaWcAm8LorxOXoL4V2k",
"1qvLYofQ0PoqmOuoGSOIyITDFjWmHl1esJKjtyCMiYy8",
"1q6PRyw7rEut1Z2DDrAj53YVBCDp5OLmeTtHcJjUMbRw",
"1obmaEUEBbzmCz4R1wg13dM4zBMHayZUR-BG43XITH_E",
"1y0xAipExBFdjCGsyCYws5IwvDFMXU2Hvkb2SA1jfFPs",
"1fbwQNIoOFr-gRbCO153k_vX4OJ-h8kGXVkWTKYcj6BI",
"1fyoTCdbL65XiCwBeFu-lA4Q95nc5DDpOBsszxasLbSA",
"1oToDddK-nQeBbtPI1Mt-DX99kVEW7NFjlQfohfrsBfk",
"1-Tjzk2rjXOGw98yMCOjSrRDmS0m5Zk5XnLUAGXCSdHs",
"1CWIi_QYJLN7NEnTF64WKbi497d8Ssf1uIShI4sw1OCY",
"18-R4XVDI-CA47R7MhyNyt7TFFBUjfnxZR3jB3pCYGk4",
"1eU0RC7M6wN1tCEiH6O9a3imJOefKMBL2FyNbJAYP-qc",
"1vmtYR7_QzJC-ghe1Z4CR9Q8jhPPwuNUJsuLBoQGYy-8",
"1UIVvsADgwQRzD2y2soX5Qe12KqqCBgSTsxEIa1Wvu7w",
"1wHZLnQ6mN_N98eoN1-S8dB3IhM7ZluWwmJ3M2Nj_Vuk",
"1vHN14tyDCikJFijXU6fxnrL-A-9Ob8m4ls_QotJyR0Q",
"1koEiOXZwpZatutckw6Dqu5Qhk48Eua_thwzqrZVRodI",
"1zxe5-KzFJehXfzn-Q4GwM5U4quY7EMbzfmn-O_OR-84",
"1IAj3kcPna9Ug0Md1HK8S9SaCVfEkvz4X6MOOjqy3sC8",
"16Ch79DEsJpnduOAGnEpK-beWJxbEoP2w7Oqy9ARaHTA",
"1xcg2eNkZ0xEx_uvGT0NUD8Ki5GpkQk6wV4FLsMhBggQ",
"19xxKRlGEC4nz6sQDceD01aSq2pJ2ustGnHOPrf9g7no",
"16fyjRUip_P-4PtBylNxi3e-pb7L1fVI8CmPdh3zAHO8",
"1rALKTQZdC6-WrV7WDlD6WUib6aLa-xp6ZH6YfC4Vng8",
"1--KPLJ0L1JXj93eCZoXazsal1abkz6klCRHlv27fyvY",
"1ofIsdhAg_P3Dm3aTlur3cDmeSWMwwJ0N_Pqpd6O5XME",
"1xzPI6NrOJwTQcG0Uo83lGZOHxzv9CujEtEDO3ETL5ek",
"1BDuLS-EdVTJhtRIz69sCixhdX4Ml_hFQP056Y5LgI5g",
"1NSJgAYdBamIiUBf9ixAb0YA_jYSrvrD6_VgZbTTLe1I",
"1gZA5nkQUDk4zPkzLVxfWJM_v_nQvBL5cEESLGTQ5IWI",
"1R1jjhAYj6safonUctJFoIea2OyjU1B6VCbjC2O7tvPs",
"1eqwz4v_h_ohKpq_yhjlHzkTnXxmXZG7QnXmyNBeM8Sw",
"1fX8xJsCza25OqnTcWxPJwBn763y6mroH9k9Q5ske9AQ",
"1QL6ktPpFGKiQ2Rr-Sldr1h-DN4vYfjsvYcwbtxMshhU",
"1TQDAHcHMWILLpv5UBY0EZ-FaoxhCJ6TpANbMiJ1MMv8",
"1re9-5PRBEdwuaeobbL2DCRei3mCePiBte5L023tMJgo",
"1s7Shaor124xlyFNdyT31yhwajSO-GQLzJqEG5IZh8xo",
"1zlIfu5f7__Cqu2KrUhKa45WgLBfbN-hi54UukXZEoIc"
  ];
  for (var i2 = 0; i2 < spreadsheetIds.length; i2++){
  var spreadsheet = SpreadsheetApp.openById(spreadsheetIds[i2]);
  var sheets = spreadsheet.getSheets();
  
  var sheet = sheets[0];
  var spreadsheetName = spreadsheet.getName();
  console.log("SheetName   "+spreadsheetName);

  var lastColumn = sheet.getLastColumn();
  if(lastColumn<=0)
    continue;
  var columnToCheck = 1;
  // Get all the data in the specified column
  var dataRange = sheet.getRange(1, columnToCheck, sheet.getLastRow(), 1);

  var cellValues = dataRange.getValues();
  
  var lastRow = sheet.getLastRow();

  // Define the columns to check
  var columnB = sheet.getRange("B1:B" + lastRow).getValues();
  var columnA = sheet.getRange("A1:A" + lastRow).getValues();
  // var columnC = sheet.getRange("C1:C" + lastRow);
  console.log("cellvalues      " + cellValues.length);
  for (var j = 0; j < cellValues.length; j++) {
    var cellB = columnB[j][0];
    var cellA = columnA[j][0];
    var cellValue = cellValues[j][0];
    var numCommas = (cellValue.match(/,/g) || []).length;
    var words = cellValue.split(/\s*,\s*/).filter(Boolean);
    var numWords = words.length;

    if (numCommas !== 4) {
      sheet.getRange(j + 1, 1, 1, lastColumn).setBackground("red");
    } else if (numWords !== 5) {
      sheet.getRange(j + 1, 1, 1, lastColumn).setBackground("red");
    }
    else if (cellB === "matchfirst" && !isValidParentheses(cellA)) {
      // columnC.getCell(j + 1, 1).setValue("Error: Invalid parentheses1");
      sheet.getRange(j + 1, 1, 1, sheet.getLastColumn()).setBackground("red");
    }
    else if (cellB === "matchfirst" && !hasMoreThanOnePairOfParentheses(cellA)) {
      // columnC.getCell(j + 1, 1).setValue("Error: Invalid parentheses2");
      sheet.getRange(j + 1, 1, 1, sheet.getLastColumn()).setBackground("red");
    }
    else if (!doesContainUppercaseLetter(cellA)) {
      sheet.getRange(j + 1, 1, 1, sheet.getLastColumn()).setBackground("red");
    }
    else if (!checkSquareBrackets(cellA)) {
      sheet.getRange(j + 1, 1, 1, sheet.getLastColumn()).setBackground("red");
    }
    else if(cellB !== "matchfirst" && !doesContainParentheses(cellA)){
      sheet.getRange(j + 1, 1, 1, sheet.getLastColumn()).setBackground("red");
    }
    else {
      sheet.getRange(j + 1, 1, 1, lastColumn).setBackground(null);
    }
  }
}
}
function doesContainParentheses(str){
  for(let i=0;i<str.length;i++){
    if(str.charAt(i)==='(' || str.charAt(i)=== ')')
    return false;
  }
  return true;
}
function isValidParentheses(str) {
  var stack = [];
  var hasWord = false; 

  for (var i = 0; i < str.length; i++) {
    var char = str.charAt(i);
    if(i==0 && char !=='(')
    return false;
    if (char === '(') {
      stack.push(char);
    }
    else if(char === '['){
      stack.push(char);
    } else if (char === ')' && stack[stack.length - 1]==='(') {
      if (stack.length === 0) {
        return false; // Mismatched closing parenthesis
      }
      stack.pop();
    }else if (char === ']' && stack[stack.length - 1] ==='[') {

      if (stack.length === 0) {
        return false; // Mismatched closing parenthesis
      }
      stack.pop();
    }
    else if(stack.length > 0 &&char !== ' ' && char !== ''){
      hasWord = true;
    }
  }
  return stack.length === 0 && hasWord;
}

function isValidSquareBrackets(str) {
  var stack = [];
  for (var i = 0; i < str.length; i++) {
    var char = str.charAt(i);
    if (char === '[') {
      stack.push(char);
    } else if (char === ']') {
      if (stack.length === 0) {
        return false; // Mismatched closing parenthesis
      }
      stack.pop();
    }
  }
  return stack.length === 0;
}
function checkSquareBrackets(str) {
  var strArr = str.split(/\s*,\s*/).filter(Boolean);

  for (var i = 0; i < strArr.length; i++) {
    var count = 0;
    var temp = strArr[i];
    if (!isValidSquareBrackets(temp))
      return false;
  }
  return true;
}

function hasMoreThanOnePairOfParentheses(str) {

  var strArr = str.split(/\s*,\s*/).filter(Boolean);

  for (var i = 0; i < strArr.length; i++) {
    var count = 0;
    var temp = strArr[i];
    if (!isValidParentheses(temp))
      return false;
    for (let j = 0; j < temp.length; j++) {
      if (temp.charAt(j) === '(')
        count++;
    }
    if (count !== 1)
      return false;
  }
  return true; // Found more opening parentheses than closing ones
}

function doesContainUppercaseLetter(cellValue) {
  if (/[A-Z]/.test(cellValue)) {
    return false;
  } else {
    return true;
  }
}


function doGet() {
  applyConditionalFormattingToSheets();  // Call the function that processes the sheets
  return ContentService.createTextOutput("Cells Highlighting Completed!"); // Returns a response after triggering
}