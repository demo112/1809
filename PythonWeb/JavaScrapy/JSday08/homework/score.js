var score = prompt('成绩');
var stage =
    score >= 90 ? "A" :
    score >= 80 ? "B" :
    score >= 70 ? "A" :
    score >= 60 ? "D" : "E";

document.write(stage);
