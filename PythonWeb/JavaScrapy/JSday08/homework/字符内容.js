var year = prompt('请输入年份');
var rain = year % 400 == 0 || (year / 4 == 0  && year / 100 == 0);
console.log(rain);

var str = prompt("请输入字符");
var num = Number(str);
console.log('数字：', num);

var st = ('a' <= str && str <= 'z') || ('A' <= str && str <= 'Z');
console.log('字母：', st);
var zh = '\u4e00' <= str.toString(16) && str.toString(16) <= '\u9fa5';
console.log('中文：', zh);


document.write('<span>闰年：</span>', rain);
document.write('<span>数字：</span>', num);
document.write('<span>字母：</span>', st);
document.write('<span>数字：</span>', zh);
