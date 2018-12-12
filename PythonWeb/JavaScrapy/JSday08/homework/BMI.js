var weight = prompt("请输入体重");
var high = prompt("请输入身高");
var bmi = weight / (high * high);
    bmi = bmi.toFixed(2);
document.write("体重指数是", bmi);
var stage =
    bmi >= 23.9 ? "过大" :
    bmi >= 18.5 ? "适中" : "过轻";

document.write("体重指数", stage);

