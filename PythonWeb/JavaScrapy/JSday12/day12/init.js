function $(tagName){
	//返回节点
	var elem = document.getElementsByTagName(tagName)[0];
	return elem;
}
function $2(tagName){
	//返回节点数组
	var elems = document.getElementsByTagName(tagName);
	return elems;
}