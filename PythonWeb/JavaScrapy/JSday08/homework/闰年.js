var year = prompt('请输入年份');
var rain = year % 400 == 0 || (year / 4 == 0  && year / 100 == 0);
console.log(rain);
